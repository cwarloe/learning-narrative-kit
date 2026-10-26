# Portland Desk — The Name Is Not the Number

*A CompTIA Network+ name resolution precursor • Hover over highlighted terms for technical definitions and triage mechanics.*

A gray March downpour beat against the high double-paned windows of the fourth floor. Seven months on the Portland Operations Center desk had taught me the rhythms of the building: which closet switches ran warm, which departments panicked before payroll cutoff, and how fast a wet morning turned into a ticket surge.

Across the center aisle, Tier 2 systems administrator Lena Chen was already forty minutes into her shift, reviewing remote access logs across our virtual machine clusters. Her headset light glowed steady amber, and her terminal windows were scrolling fast. Jules Brooks sat to my left, finishing her first coffee while auditing overnight firewall changes.

By eight thirty, the incoming ticket board on our wall monitor began flashing amber with nine high-priority incidents. Remote employees working across Multnomah and Washington counties were calling in with identical complaints. They had connected their laptops to our corporate virtual private network without any errors. Yet whenever they tried to open the internal payroll portal or the plant telemetry wiki, their browsers spun endlessly. Some requests timed out completely, while others redirected users to an unfamiliar public domain parking page. Meanwhile, accountants and dispatchers working inside the building were browsing those exact same internal websites without any trouble.

## Jared and the ISP scapegoat

```callout-panel
title: "FIGURE 4.1: SPLIT-HORIZON RESOLVER & HOSTS OVERRIDE"
badge: "DNS Architecture"
caption: "Schematic cutaway: The local DNS resolution path. When the resolver queries 127.0.0.1 and hosts file before recursive forwarders, a stale hardcoded IP sends traffic to a retired server."
prompt: "Clean technical cutaway diagram of a computer desktop screen displaying DNS resolution paths under bright, even lighting. Flowchart lines connect local hosts file to DNS resolver cache and recursive domain controllers. Clean instructional style, crisp fine lines, no text, no words. 16:9 ratio."
```

Jared Vance from network operations walked over from the bullpen holding a paper cup of lukewarm coffee. He had worked around regional fiber plants long enough to remember when frame relay was cutting edge. His first instinct during any distributed outage was to blame the carrier.

"Comcast probably pushed another broken routing update, or a backhoe clipped a conduit in Beaverton," Jared said, gesturing toward the rain with his paper cup. "Remote workers are on domestic broadband lines that flake out whenever the weather turns sour. Have them reboot their cable modems and flush their network stacks."

Lena Chen turned slightly in her swivel chair and lowered her headset microphone. "Rebooting sixty consumer cable modems across three residential providers is not an operational triage plan, Jared. The VPN concentrator shows eighty-two active client tunnels with healthy keepalive handshakes. We have zero packet drops on the transport interface. The encrypted tunnel is staying wide open, but the application payload is landing in the wrong place."

I opened the first ticket from the queue. It was submitted by an accounts payable clerk named Greg who was working remotely from Hillsboro. Greg could not access `payroll.harrowmere.local` to verify morning direct deposits. His browser displayed a generic error stating that the server address could not be found.

Jules took a sip from her ceramic mug and leaned over my cubicle partition. She watched my screen as I initiated a remote assistance session to Greg's laptop. "What is your working hypothesis, Ethan?"

"Jared thinks the residential internet providers are dropping our internal routes," I replied. I brought up a command prompt on Greg's desktop. "I was going to ping the web server name to see where the packets die along the path."

Jules set her coffee mug down with a soft ceramic clink. "If you try to ping a domain name that cannot be resolved, ping will not tell you anything about routing health. It will simply tell you that your operating system has no idea what destination address to put into the packet header. When a user tells you a website is down, remember that the name is not the number. Trace who answers the question before you assume the wire is broken."

## The contractor's forgotten shortcut

I leaned forward and examined the terminal window on Greg's remote screen. Instead of running ping sweeps, I executed `ipconfig /displaydns` to inspect the contents of his local operating system resolver cache. Hundreds of routine web records scrolled past. Mixed among them were cached intranet entries that looked thoroughly garbled.

"Look at the IP address Greg's machine tried to reach for the payroll portal," I murmured. I highlighted a line in the terminal dump. "The cache shows an entry for `payroll.harrowmere.local` mapped to `192.168.1.50`. Our actual corporate payroll cluster sits in the datacenter on `10.100.20.14`."

"A `192.168.1.50` address is private non-routable space that belongs on a domestic local network," Maya pointed out. She wheeled her chair into our row. "Check the local static configuration files before you do anything else."

I navigated immediately to `C:\Windows\System32\drivers\etc\` and opened the local [[hosts_file|hosts file]] in an elevated text editor. Right beneath the default commented loopback entries, someone had manually appended three hardcoded lines during the previous autumn:

```text
# Temporary development override - DO NOT REMOVE
192.168.1.50    payroll.harrowmere.local
192.168.1.51    wiki.harrowmere.local
```

"A contract software developer had this machine out in a staging trailer last September," I said. "They must have hardcoded those static mappings to point to a portable test server on their switch. Nobody ever cleaned the file before reissuing the laptop to accounting."

"The operating system checks the local cache and the static file before it ever asks an external server," Jules remarked. She crossed her arms. "Remove those obsolete entries and flush the resolver cache. Let us see what happens when the computer actually asks for directions."

I deleted the three hardcoded lines, saved the file, and executed `ipconfig /flushdns` in the command prompt. The utility confirmed that the DNS resolver cache had been successfully purged. I then launched Greg's web browser and refreshed the payroll portal tab. I fully expected the login screen to appear so I could close the ticket.

Instead, the browser spun for five seconds, timed out, and displayed a connection failure: `DNS_PROBE_FINISHED_NXDOMAIN`. The browser reported that the server IP address could not be found.

"The bad static file was masking a deeper failure," I said. I felt the initial rush of confidence drain away. "Even with the local override removed, the machine is still failing to resolve the internal domain."

## The server that answered the question

The help desk phone lines were lighting up with six more incoming calls from field supervisors and remote inspectors. All of them reported the exact same symptom. Their web browsers could not open internal corporate resources over the VPN. Two users claimed that navigating to `wiki.harrowmere.local` had redirected them to an external search engine.

"This is why you never stop at the first anomaly you find," Jules said calmly. "A single dirty configuration file explains one laptop. It does not explain eighteen tickets originating from six different neighborhoods. Go back to first principles, Ethan. Stop guessing what the computer wants to find. Look at the exact dialogue taking place between the client and the resolver."

I opened a fresh command prompt on Greg's workstation and launched interactive `nslookup`. When I typed `payroll.harrowmere.local` at the prompt, the output appeared almost instantly:

```console
C:\Users\greg.adams> nslookup payroll.harrowmere.local
Server:  router.local
Address:  192.168.1.1

*** router.local can't find payroll.harrowmere.local: Non-existent domain
```

I stared at the first two lines of the terminal response. "Look at the resolving server address. The machine did not query our enterprise domain controller at `10.100.10.2`. It sent the query directly to `192.168.1.1`, which is Greg's personal home Wi-Fi gateway."

"And what does his home router do when a client asks it to resolve an unfamiliar internal host?" Lena asked.

"His home router forwards the query to its upstream [[recursive_resolver|recursive resolver]] at Comcast," I said. "The `.local` domain is reserved for local link device discovery. Comcast's public recursive resolvers don't know our private corporate namespace, so they drop an immediate NXDOMAIN non-existent domain code right back to his machine."

"Now look at what happens when Greg tries to browse the public corporate domain name," Lena said.

I typed `nslookup wiki.harrowmere.com` into the terminal. This time, the query returned a public IP address belonging to a cloud content delivery network. It was accompanied by an alias record indicating that `wiki.harrowmere.com` was registered as a [[cname_record|CNAME record]] pointing to an external hosting provider.

"We use [[split_dns|split-horizon DNS]] for all of our regional infrastructure," Lena explained. She pointed at the two distinct answers on my screen. "When an employee is sitting in this building, our internal name servers intercept the query and return a private `10.100.40.8` address for the plant documentation wiki. But when an external user queries the exact same hostname from the public internet, our public authoritative name servers return an external proxy gateway. If a remote worker's machine queries a public resolver instead of our internal domain controller, they receive the external answer. That external host promptly rejects their internal connection attempt."

## The leak in the tunnel

The diagnostic output laid the entire breakdown bare:

```console
InterfaceAlias               : Wi-Fi
InterfaceIndex               : 14
IPv4Address                  : 192.168.1.105
IPv4DefaultGateway           : 192.168.1.1
DNSServer                    : 192.168.1.1

InterfaceAlias               : Portland-Corporate-VPN
InterfaceIndex               : 22
IPv4Address                  : 10.200.15.42
IPv4DefaultGateway           : 
DNSServer                    : 10.100.10.2, 10.100.10.3
```

"Look at the interface binding order and gateway metrics," Lena observed. She spotted the configuration discrepancy immediately. "The client VPN profile was updated during last night's maintenance window to enable split-tunneling. That was intended to keep remote employees from pushing video streaming traffic across our corporate circuits. But whoever updated the XML connection profile forgot to configure the domain suffix search list. They also left the virtual adapter metric set higher than the physical Wi-Fi interface."

"A textbook [[dns_leak|DNS leak]]," Jules observed. She took another sip of coffee. "Modern Windows operating systems query all available network adapters simultaneously under Smart Multi-Homed Name Resolution. The physical Wi-Fi adapter's local router responds in four milliseconds with an NXDOMAIN code, while the encrypted tunnel takes twenty. Because the virtual adapter's metric is set higher than the physical interface, the resolver prioritizes the local negative response, and the client never establishes the connection through the VPN."

"To make matters worse, look at the negative response caching," Lena added, pulling up the resolver cache. "Windows aggressively caches that NXDOMAIN using the negative TTL defined in the upstream SOA record. So even if the employee restarts their browser or reconnects the tunnel, the operating system keeps serving the failure until the negative cache expires or you flush it."

Jules set her mug down and leaned over the cubicle partition, her eyes scanning the board where eighteen tickets continued to flash amber.

Jules picked up her phone to intercept another incoming call from finance. "We have eighty-two tunnels open and seventy remote workers locked out of payroll while Jared is ready to yell at Comcast. The XML profile fix has to push cleanly, the adapter metrics need to prioritize the tunnel, and that negative cache trap has to clear without rebooting eighty laptops in the middle of their shift."

She looked back over her monitor. "You have fifteen minutes before accounting calls the Director, Ethan. Fix the plumbing."

I looked at the terminal output and the dual adapter configuration. The tunnel was wide open, but the packets were flying blind. I needed to isolate the DNS leak, calculate the corrected adapter metrics, and draft the infrastructure escalation before the morning payroll deadline expired.

## Vocabulary & Concepts

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[split_dns|Split-Horizon DNS]]** | A name resolution configuration where separate authoritative DNS servers or zone views provide different IP addresses for the same hostname based on client network location. | Internal staff on the corporate network resolve private `10.x.x.x` addresses, while external internet users resolve public gateway or CDN IPs for the same domain name. |
| **[[dns_leak|DNS Leak]]** | A networking anomaly where DNS lookups from a VPN-connected client bypass the encrypted tunnel and are sent in cleartext to local or ISP resolvers. | A remote worker's home Wi-Fi router answers corporate queries with failure errors before the corporate domain controller on the other end of the tunnel can respond. |
| **[[hosts_file|Hosts File]]** | A plain-text operating system file that maps hostnames directly to static IP addresses, taking precedence over DNS server queries during resolution. | A legacy manual override file that developers and contractors often forget to clean up, silently redirecting modern traffic to dead or obsolete test servers. |
| **[[recursive_resolver|Recursive Resolver]]** | A DNS server that performs the iterative process of querying root, TLD, and authoritative name servers on behalf of a client stub resolver to return an answer. | The intermediate server (such as an ISP or public DNS provider) that tracks down the final IP address for a computer that does not know where to go. |
| **[[dns_ttl|DNS TTL]]** | A 32-bit integer in a DNS resource record determining the duration in seconds that intermediate resolvers and client caches may retain the record before re-querying. | The expiration timer that tells your laptop how long to remember a good or bad answer; if set too high, it traps users on stale or broken addresses after an outage. |
| **[[cname_record|CNAME Record]]** | A DNS Canonical Name resource record that establishes an alias from one domain name to another fully qualified domain name rather than to an IP address. | An alias pointer that routes a friendly hostname (like `wiki.harrowmere.com`) to an external cloud or vendor URL where the real web application lives. |

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: DNS Plumbing, Name Resolution Triage, & Split-Horizon Analysis
target: workbench/04-the-name-is-not-the-number.md
domain: CompTIA Network+ N10-008 • Domain 1.0 & 4.0
badge: Hands-On Lab
---
Take over Ethan's workstation. Triage the multi-homed VPN DNS leak in interactive terminal drills, correct the interface metrics and domain suffix bindings, wipe the stale negative cache, and draft the Tier 2 Infrastructure Escalation Note.
```
