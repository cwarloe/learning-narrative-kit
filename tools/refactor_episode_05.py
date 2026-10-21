#!/usr/bin/env python3
"""Refactor Episode 05 into the Interleaved Cliffhanger Handoff Model."""

from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

NARRATIVE_PATH = KIT_ROOT / "portland-desk" / "narrative" / "05-the-wire-has-two-ends.md"
DOCS_NARRATIVE_PATH = KIT_ROOT / "docs" / "portland-desk" / "narrative" / "05-the-wire-has-two-ends.md"

WORKBENCH_PATH = KIT_ROOT / "portland-desk" / "workbench" / "05-the-wire-has-two-ends.md"
DOCS_WORKBENCH_PATH = KIT_ROOT / "docs" / "portland-desk" / "workbench" / "05-the-wire-has-two-ends.md"

NEW_NARRATIVE_END = """## Fifteen thousand ghosts in time-wait

By eleven o'clock the rain had intensified, drumming a steady rhythm against the eastern windows. The bullpen temperature dropped a couple of degrees as cold air seeped through the frames. Jared returned from the server room with fresh tea. He sat down to run a catch-up batch of his backup script across all four hundred municipal field devices. His script was designed to query switches, distribution routers, and environmental sensors across five remote facilities.

After ten minutes of execution, Jared's terminal began spitting out hundreds of crimson error traces. The script aborted abruptly with a socket exception that filled the window.

```console
Unhandled Exception: System.Net.Sockets.SocketException: Only one usage of each socket address 
(protocol/network address/port) is normally permitted.
   at System.Net.Sockets.Socket.DoBind(EndPoint endPointSnapshot, SocketAddress socketAddress)
   at System.Net.Sockets.TcpClient.Connect(IPEndPoint remoteEP)
```

"The archive server crashed again," Jared shouted, kicking his wastebasket against the desk leg. "We restarted the service, and now the server is choking under load. The software cannot handle four hundred switches hitting it at once."

I opened my remote session to `PDX-ARCHIVE01` and inspected the server health. The backup service was running normally. Processor utilization was hovering at twelve percent. The listening socket was still active on port 8443 under Process ID 4112. The server was completely healthy and accepting local test connections without delay.

"The server is running cleanly, Jared," Jules said from her chair, looking over her shoulder without pausing her typing. "Look at your own workstation before you blame the destination. Ethan, run a socket audit on Jared's desktop."

I opened a PowerShell console on Jared's administrative workstation. I ran a count of active TCP sockets grouped by their connection state.

```console
PS C:\\Users\\jvance> netstat -ano | findstr 8443 | measure-object -line

Lines Words Characters Property
----- ----- ---------- --------
15248
```

The terminal returned a count of over fifteen thousand socket records. When I inspected the detailed list, thousands of entries appeared with identical destination parameters. They differed only by their outbound client-side port numbers.

```console
PS C:\\Users\\jvance> netstat -ano | findstr 8443
  TCP    10.100.1.50:49210      10.100.4.20:8443       TIME_WAIT       0
  TCP    10.100.1.50:49211      10.100.4.20:8443       TIME_WAIT       0
  TCP    10.100.1.50:49212      10.100.4.20:8443       TIME_WAIT       0
  TCP    10.100.1.50:49213      10.100.4.20:8443       TIME_WAIT       0
  TCP    10.100.1.50:49214      10.100.4.20:8443       TIME_WAIT       0
```

"Look at the client port column," I said, pointing out the pattern to Jared. "Every single connection originates from your desktop at `10.100.1.50` using an [[ephemeral_port|ephemeral port]] in the dynamic range above 49151. Every one of those sockets is parked in the `TIME_WAIT` state, and the process identifier is zero."

"What did your script do inside that loop, Jared?" Jules asked.

Jared rubbed his forehead, looking at his source code on his left screen. "The script loops through an array of management addresses. For each device, it creates a new TCP client object and connects to the archive server. It posts an eight-kilobyte configuration blob, and then calls the close method before moving to the next device."

"Your script created a separate transport session for every single transaction," I realized, sketching the lifecycle on my pad. "When your script closed the socket, the client operating system initiated an active close. The TCP standard requires the initiating host to hold that socket in `TIME_WAIT` for two maximum segment lifetimes. In Windows, that timer defaults to one hundred and twenty seconds."

Jules wheeled her chair closer, looking from the fifteen thousand frozen sockets on Jared's screen to the blinking backup SLA alert on the dispatch board.

"You have four hundred municipal switches waiting on configuration backups, and our disaster recovery SLA expired two hours ago," Jules said, her voice quiet and direct. "The server is healthy, but Jared's workstation has consumed every dynamic port in its outbound pool. How do you triage this socket exhaustion, reconfigure the operating system TCP recycling timers, refactor the client transport architecture, and prove the fix without losing a single device backup? Call your shot, Ethan."

I looked at the mountain of frozen TIME_WAIT sockets. The wire had two ends, and right now, our own management station was starving itself to death. I needed to isolate the dynamic port depletion, calculate the socket reuse rates, and implement connection pooling before the next scheduled archive sweep failed.

## Vocabulary & Concepts

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[tcp_handshake|TCP Three-Way Handshake]]** | The connection establishment process in Transmission Control Protocol where a client and server exchange SYN, SYN-ACK, and ACK packets to synchronize sequence numbers and allocate resources before data transfer. | The three-step conversation (SYN, SYN-ACK, ACK) required to establish a reliable connection before any application data can flow across the network. |
| **[[socket_state|Socket State]]** | The operational status of a network communication endpoint within the TCP state machine, such as LISTENING, ESTABLISHED, CLOSE_WAIT, or TIME_WAIT. | The current phase of a network connection, showing whether a port is waiting for clients, actively transferring data, or closing down. |
| **[[listening_port|Listening Port]]** | A network port bound by a background server daemon or application process configured to accept incoming connection requests from remote clients. | An open door on a server where a specific background program is actively waiting for incoming client connections. |
| **[[reset_packet|TCP Reset (RST)]]** | A TCP control segment with the RST flag asserted, sent by a host to abruptly terminate a connection or actively reject an inbound packet directed to an unbound port. | An active rejection packet sent by an operating system telling the client that no program is listening on that port, resulting in an immediate 'Connection refused'. |
| **[[ephemeral_port|Ephemeral Port]]** | A dynamic, short-lived transport layer port assigned automatically by a client operating system from a high-numbered range (typically 49152 to 65535) to identify an outbound session. | A temporary port number assigned to a client computer for an outbound connection so the server knows where to send replies. |
| **[[port_exhaustion|Ephemeral Port Exhaustion]]** | A state where a client operating system depletes its entire range of dynamic outbound ports, preventing any new outbound network connections from establishing. | A client-side bottleneck where an application opens and closes connections so rapidly that all available outbound port numbers become trapped in TIME_WAIT. |

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: TCP Sockets, Port States, & Handshake Diagnostics
target: workbench/05-the-wire-has-two-ends.md
domain: CompTIA Network+ N10-008/009 • Domain 1.1, 1.4 & 4.1
badge: Hands-on Lab
---
Take over Ethan's triage console. Diagnose the client-side ephemeral port exhaustion storm in interactive netstat drills, calculate the 2MSL socket recycling rates, configure connection pooling, and submit the Tier 1 Transport Resolution Note.
```
"""

WORKBENCH_EPILOGUE = """

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 5.2: RESOLVED TRANSPORT LAYER ARCHIVE"
badge: "Shift Epilogue"
caption: "Operations center: At 01:45 PM, thin bands of autumn sunlight illuminate the Marquam Bridge as the backup archive engine streams municipal switch configurations without a dropped socket."
prompt: "Clean graphic novel cutaway panel of a network management operations bullpen in the Pacific Northwest. Large windows show breaking clouds over an industrial bridge. On a multi-monitor desk, clean terminal windows display green successful backup synchronization logs. A ceramic coffee mug sits beside neatly arranged diagnostic notebooks. Ligne Claire style, sharp technical ink lines, no text, no words. 16:9 ratio."
```

With the root cause of the socket depletion isolated, Jared leaned back in his chair, exhaling slowly through his teeth. "My own machine starved itself because I tore down the sockets too fast."

"You built an engine that buys a new telephone for every phone call, speaks for two seconds, and drops the phone into a bucket that takes two minutes to empty," Jules said dryly. "Modify your script to use connection pooling with persistent HTTP keep-alive sessions. That way you reuse an established socket across hundreds of sequential requests instead of discarding it."

Jared updated his script logic to reuse existing connections through a shared connection pool of sixteen concurrent sockets. At the same time, I adjusted the Windows registry value `TcpTimedWaitDelay` on his workstation from one hundred and twenty seconds down to thirty seconds, allowing the operating system to recycle dormant sockets four times faster during heavy administrative runs.

When Jared executed the refactored script five minutes later, the performance difference was remarkable. The batch job processed all four hundred network devices in less than three minutes. The script maintained a compact pool of sixteen established connections that transferred configurations seamlessly without dropping a single packet.

By two o'clock in the afternoon, the storm clouds had begun to break apart over the river. Thin bands of pale autumn sunlight illuminated the wet asphalt of the parking garage below. The morning ticket surge had subsided, and the status boards across the room showed steady green. Jared had finished his configuration archive run and was documenting connection pooling in our engineering wiki.

I sat back at my desk and pulled my technical notebook toward me. I drew the four-stage lifecycle of a transport socket alongside the handshake flags.

Jules wheeled her chair over to my desk with a printed network diagram of the Gresham annex. "What was the most important diagnostic distinction you made today, Ethan?"

"The difference between an active rejection and a silent drop," I answered without hesitation. "When an application throws an immediate connection refused error, the network infrastructure is working. The target host is sending back an explicit reset because no service is listening. But when an application hangs in a timeout, packets are dropping into a void caused by a dead route or a packet-filtering firewall."

"And what about Jared's script?" Jules asked with a faint smile.

"Capacity belongs to both ends of the wire," I replied. "A client can paralyze itself through ephemeral port exhaustion if it opens and closes connections faster than the transport stack can recycle them. You have to verify both the listener on the destination and the source socket pool on the client."

"Keep that page in your notebook," Jules said, tapping the paper with her pen. "Next month when someone insists the network is broken because an application cannot connect, you will not waste your morning opening emergency firewall tickets. You will check whether anyone is listening first."

She wheeled her chair back to her desk and unhooked her bicycle helmet from the monitor arm as the afternoon shift technicians began logging into the queue. I saved my ticket notes into the service management portal, closed my terminal sessions, and turned back to the incoming queue with the quiet confidence of an engineer who knows how to listen to the wire.
"""

def update_narrative():
    raw = NARRATIVE_PATH.read_text(encoding="utf-8")
    part1 = raw.split("## Fifteen thousand ghosts in time-wait")[0].strip()
    full_new = part1 + "\n\n" + NEW_NARRATIVE_END
    NARRATIVE_PATH.write_text(full_new, encoding="utf-8")
    DOCS_NARRATIVE_PATH.write_text(full_new, encoding="utf-8")
    print(f"Updated narrative in {NARRATIVE_PATH} and {DOCS_NARRATIVE_PATH}")

def update_workbench():
    wb = WORKBENCH_PATH.read_text(encoding="utf-8")
    if "## 6. Shift Resolution Epilogue" not in wb:
        wb = wb.strip() + "\n" + WORKBENCH_EPILOGUE
        WORKBENCH_PATH.write_text(wb, encoding="utf-8")
        DOCS_WORKBENCH_PATH.write_text(wb, encoding="utf-8")
        print(f"Appended Epilogue to {WORKBENCH_PATH} and {DOCS_WORKBENCH_PATH}")

if __name__ == "__main__":
    update_narrative()
    update_workbench()
