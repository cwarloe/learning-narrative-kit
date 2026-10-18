# Portland Desk — The Name Is Not the Number

*A CompTIA Network+ name resolution precursor • Hover over highlighted terms for technical definitions and triage mechanics.*

A steady March downpour had been drumming against the high double-paned windows since six in the morning. I was five months into my tenure at the Portland Operations Center. That was long enough to know which switches ran hot in the telecom closets, and which departments panicked over forgotten passwords. The index cards I once carried in my shirt pocket now sat inside my center desk drawer. My morning routine remained largely unchanged.

Jules Mercer pedaled in around eight fifteen. She shook sheets of water from her yellow cycling jacket before draping it across the back of her chair. Her battered steel commuter bike was already locked downstairs in the basement cage. Its fenders were coated in gritty road spray. Her black helmet hung from the lower mounting arm of her secondary display. On the lower right bezel of her primary monitor, a faded yellow sticky note read *Which decision?* Its edges curled slightly under the steady breeze from the ceiling vent.

Across the center aisle from our row, Tier 2 systems administrator Maya Chen was already reviewing directory logs. Maya managed our regional identity services, virtual machine clusters, and remote access gateways. She was usually quiet during the first hour of a shift. This morning, however, her headset light was glowing amber and her keyboard clattered with steady, rhythmic keystrokes.

By eight thirty, the incoming ticket board on our wall monitor began flashing amber with nine high-priority incidents. Remote employees working across Multnomah and Washington counties were calling in with identical complaints. They had connected their laptops to our corporate virtual private network without any errors. Yet whenever they tried to open the internal payroll portal or the plant telemetry wiki, their browsers spun endlessly. Some requests timed out completely, while others redirected users to an unfamiliar public domain parking page. Meanwhile, accountants and dispatchers working inside the building were browsing those exact same internal websites without any trouble.

## Jared and the ISP scapegoat

Jared Vance from network operations walked over from the bullpen holding a paper cup of lukewarm coffee. He had worked around regional fiber plants long enough to remember when frame relay was cutting edge. His first instinct during any distributed outage was to blame the carrier.

"CenturyLink has a backhoe problem out in Beaverton, or Comcast pushed another broken routing update," Jared announced. He gestured vaguely toward the rain-streaked windows with his paper cup. "The office runs on a dedicated synchronous fiber loop with static routes. Those remote workers are sitting on domestic broadband connections that drop packets whenever the weather turns sour. Tell them to reboot their residential cable modems and flush their network stacks."

Maya Chen turned slightly in her swivel chair and lowered her headset microphone. "Rebooting sixty consumer cable modems across three residential providers is not an operational triage plan, Jared. The VPN concentrator shows eighty-two active client tunnels with healthy keepalive handshakes. We have zero packet drops on the transport interface. The encrypted tunnel is staying wide open, but the application payload is landing in the wrong place."

I opened the first ticket from the queue. It was submitted by an accounts payable clerk named Greg who was working remotely from Hillsboro. Greg could not access `payroll.portland-ops.local` to verify morning direct deposits. His browser displayed a generic error stating that the server address could not be found.

Jules took a sip from her ceramic mug and leaned over my cubicle partition. She watched my screen as I initiated a remote assistance session to Greg's laptop. "What is your working hypothesis, Ethan?"

"Jared thinks the residential internet providers are dropping our internal routes," I replied. I brought up a command prompt on Greg's desktop. "I was going to ping the web server name to see where the packets die along the path."

Jules set her coffee mug down with a soft ceramic clink. "If you try to ping a domain name that cannot be resolved, ping will not tell you anything about routing health. It will simply tell you that your operating system has no idea what destination address to put into the packet header. When a user tells you a website is down, remember that the name is not the number. Trace who answers the question before you assume the wire is broken."

## The contractor's forgotten shortcut

I leaned forward and examined the terminal window on Greg's remote screen. Instead of running ping sweeps, I executed `ipconfig /displaydns` to inspect the contents of his local operating system resolver cache. Hundreds of routine web records scrolled past. Mixed among them were cached intranet entries that looked thoroughly garbled.

"Look at the IP address Greg's machine tried to reach for the payroll portal," I murmured. I highlighted a line in the terminal dump. "The cache shows an entry for `payroll.portland-ops.local` mapped to `192.168.1.50`. Our actual corporate payroll cluster sits in the datacenter on `10.100.20.14`."

"A `192.168.1.50` address is private non-routable space that belongs on a domestic local network," Maya pointed out. She wheeled her chair into our row. "Check the local static configuration files before you do anything else."

I navigated immediately to `C:\Windows\System32\drivers\etc\` and opened the local [[hosts_file|hosts file]] in an elevated text editor. Right beneath the default commented loopback entries, someone had manually appended three hardcoded lines during the previous autumn:

```text
# Temporary development override - DO NOT REMOVE
192.168.1.50    payroll.portland-ops.local
192.168.1.51    wiki.portland-ops.local
```

"A contract software developer had this machine out in a staging trailer last September," I said. "They must have hardcoded those static mappings to point to a portable test server on their switch. Nobody ever cleaned the file before reissuing the laptop to accounting."

"The operating system checks the local cache and the static file before it ever asks an external server," Jules remarked. She crossed her arms. "Remove those obsolete entries and flush the resolver cache. Let us see what happens when the computer actually asks for directions."

I deleted the three hardcoded lines, saved the file, and executed `ipconfig /flushdns` in the command prompt. The utility confirmed that the DNS resolver cache had been successfully purged. I then launched Greg's web browser and refreshed the payroll portal tab. I fully expected the login screen to appear so I could close the ticket.

Instead, the browser spun for five seconds and displayed a bright orange GoDaddy parked domain page. The page announced that `portland-ops.local` was available for purchase or had no active web host configured.

"The bad static file was masking a deeper failure," I said. I felt the initial rush of confidence drain away. "Even with the local override removed, the machine is still failing to resolve the internal domain."

## The server that answered the question

The help desk phone lines were lighting up with six more incoming calls from field supervisors and remote inspectors. All of them reported the exact same symptom. Their web browsers could not open internal corporate resources over the VPN. Two users claimed that navigating to `wiki.portland-ops.local` had redirected them to an external search engine.

"This is why you never stop at the first anomaly you find," Jules said calmly. "A single dirty configuration file explains one laptop. It does not explain eighteen tickets originating from six different neighborhoods. Go back to first principles, Ethan. Stop guessing what the computer wants to find. Look at the exact dialogue taking place between the client and the resolver."

I opened a fresh command prompt on Greg's workstation and launched interactive `nslookup`. When I typed `payroll.portland-ops.local` at the prompt, the output appeared almost instantly:

```console
C:\Users\greg.adams> nslookup payroll.portland-ops.local
Server:  router.local
Address:  192.168.1.1

*** router.local can't find payroll.portland-ops.local: Non-existent domain
```

I stared at the first two lines of the terminal response. "Look at the resolving server address. The machine did not query our enterprise domain controller at `10.100.10.2`. It sent the query directly to `192.168.1.1`, which is Greg's personal home Wi-Fi gateway."

"And what does his home router do when a client asks it to resolve an unfamiliar internal host?" Maya asked.

"His home router forwards the request upstream to its configured [[recursive_resolver|recursive resolver]] at Comcast," I explained. I traced the query path mentally. "The public recursive servers walk the internet root servers and the top-level domain authorities looking for `.local`. But `.local` is a private, non-delegated internal namespace that does not exist in public root zone files. The public resolver immediately returns a non-existent domain code."

"Now look at what happens when Greg tries to browse the public corporate domain name," Maya said.

I typed `nslookup wiki.portland-ops.com` into the terminal. This time, the query returned a public IP address belonging to a cloud content delivery network. It was accompanied by an alias record indicating that `wiki.portland-ops.com` was registered as a [[cname_record|CNAME record]] pointing to an external hosting provider.

"We use [[split_dns|split-horizon DNS]] for all of our regional infrastructure," Maya explained. She pointed at the two distinct answers on my screen. "When an employee is sitting in this building, our internal name servers intercept the query and return a private `10.100.40.8` address for the plant documentation wiki. But when an external user queries the exact same hostname from the public internet, our public authoritative name servers return an external proxy gateway. If a remote worker's machine queries a public resolver instead of our internal domain controller, they receive the external answer. That external host promptly rejects their internal connection attempt."

## The leak in the tunnel

The core puzzle was why a workstation connected to our secure corporate VPN tunnel was sending internal queries to a domestic broadband router in the first place.

"The VPN client is supposed to assign our internal name servers when the tunnel establishes," I said. I pulled up the network interface settings on Greg's laptop. I ran `Get-NetIPConfiguration` in PowerShell to inspect both active adapters side by side.

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

"Look at the interface binding order and gateway metrics," Maya observed. She spotted the configuration discrepancy immediately. "The client VPN profile was updated during last night's maintenance window to enable split-tunneling. That was intended to keep remote employees from pushing video streaming traffic across our corporate circuits. But whoever updated the XML connection profile forgot to configure the domain suffix search list. They also left the virtual adapter metric set higher than the physical Wi-Fi interface."

"A textbook [[dns_leak|DNS leak]]," Jules observed. She took another sip of coffee. "Modern Windows operating systems query all available network interfaces simultaneously under multi-homed resolution. The physical Wi-Fi adapter responds in four milliseconds, while the encrypted tunnel takes twenty. The home router answers first with an authoritative NXDOMAIN failure. The Windows resolver accepts the fastest negative response. The client never even waits for the internal domain controller to answer through the VPN."

"To make matters worse, look at the negative response caching," I added. I checked the record properties. "The local resolver caches those failed lookups according to the zone [[dns_ttl|DNS TTL]]. That means even if the employee restarts their browser or reconnects the tunnel, the operating system keeps feeding them the cached failure for the next fifteen minutes."

Maya pulled up the centralized VPN gateway management console on her workstation. "I can push a mandatory client configuration profile update to the VPN gateway right now. We will force the virtual adapter metric to a lower priority number. We will also enable the DNS domain suffix binding for `portland-ops.local`, and enforce tunnel-only resolution for all internal zones. But every user currently stranded on the queue will need to flush their resolver cache once the profile updates."

"I will handle the queue," I said. I opened our mass notification template. "We can give them the exact three-step fix: disconnect the VPN client, reconnect to pull the revised profile from the gateway, and run `ipconfig /flushdns` in their command prompt to wipe the stale negative cache."

Maya initiated the profile deployment across the cluster. Within twelve minutes, the gateway logs confirmed that seventy-five remote endpoints had downloaded the corrected configuration. I called Greg back in Hillsboro. I walked him through the reconnection and cache flush, and watched his screen over remote control as he refreshed the browser.

The bright orange registrar landing page vanished immediately. It was replaced by the green-and-white portal header of our internal payroll application. Greg let out an audible sigh of relief over the telephone line. He muttered that he could finally submit his department's morning timesheets, and thanked us before hanging up. One by one, the remaining seventeen tickets on the board were updated, verified, and resolved.

Jared walked back past our row with a fresh cup of coffee. He glanced at the green status board, and gave a brief, sheepish shrug before heading back toward the network closet. He did not say another word about CenturyLink backhoes.

Jules smiled faintly and set her empty mug down on the edge of the partition. She unclipped her helmet from the display arm. "You spent two hours chasing down someone else's bad configuration, Ethan, but you did not spend it guessing. Remember this shift the next time someone tells you an application is broken. The application is almost never broken. Most of the time, the client is just asking the wrong stranger for directions."

I wrote her words down in my technical journal. I saved the ticket escalation notes for Maya's post-incident review, and turned back to the queue as the rain outside softened into a quiet, steady mist.

## Vocabulary & Concepts

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[split_dns|Split-Horizon DNS]]** | A name resolution configuration where separate authoritative DNS servers or zone views provide different IP addresses for the same hostname based on client network location. | Internal staff on the corporate network resolve private `10.x.x.x` addresses, while external internet users resolve public gateway or CDN IPs for the same domain name. |
| **[[dns_leak|DNS Leak]]** | A networking anomaly where DNS lookups from a VPN-connected client bypass the encrypted tunnel and are sent in cleartext to local or ISP resolvers. | A remote worker's home Wi-Fi router answers corporate queries with failure errors before the corporate domain controller on the other end of the tunnel can respond. |
| **[[hosts_file|Hosts File]]** | A plain-text operating system file that maps hostnames directly to static IP addresses, taking precedence over DNS server queries during resolution. | A legacy manual override file that developers and contractors often forget to clean up, silently redirecting modern traffic to dead or obsolete test servers. |
| **[[recursive_resolver|Recursive Resolver]]** | A DNS server that performs the iterative process of querying root, TLD, and authoritative name servers on behalf of a client stub resolver to return an answer. | The intermediate server (such as an ISP or public DNS provider) that tracks down the final IP address for a computer that does not know where to go. |
| **[[dns_ttl|DNS TTL]]** | A 32-bit integer in a DNS resource record determining the duration in seconds that intermediate resolvers and client caches may retain the record before re-querying. | The expiration timer that tells your laptop how long to remember a good or bad answer; if set too high, it traps users on stale or broken addresses after an outage. |
| **[[cname_record|CNAME Record]]** | A DNS Canonical Name resource record that establishes an alias from one domain name to another fully qualified domain name rather than to an IP address. | An alias pointer that routes a friendly hostname (like `wiki.portland-ops.com`) to an external cloud or vendor URL where the real web application lives. |

```bridge-card
title: Portland Desk Workbench: DNS Plumbing, Name Resolution Triage, & Split-Horizon Analysis
target: workbench/04-the-name-is-not-the-number.md
domain: CompTIA Network+ N10-008 • Domain 1.0 & 4.0
badge: Hands-On Lab
---
Step onto Ethan's shift with live command-line artifacts, inspect split-horizon nslookup outputs, hunt down rogue hosts file overrides, master the Commit Before You Touch prediction gate, and submit a Tier 1 DNS resolution ticket.
```
