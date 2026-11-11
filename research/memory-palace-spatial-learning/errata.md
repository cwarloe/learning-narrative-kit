# Errata for the architecture document

[`cognitive-spatial-technical-learning-architecture.md`](cognitive-spatial-technical-learning-architecture.md) is an unedited export of the Google Doc. Read the notes below in place of the corresponding lines in the export. The export itself is left unchanged unless the Drive original is revised and re-exported.

## 10 / 25 / 15 pacing (section 3 and the section 9 checklist)

The export says instructional designs must prohibit continuous lectures exceeding 10 minutes, and the checklist says to enforce 10/25/15 and strictly cap instructor presentation at 10 minutes. Do not treat those lines as a rule, and do not justify them with a 10-minute attention span. Reviews of that claim find little support for it (Bradbury 2016; Wilson and Korn 2007; [sources.md](sources.md) #44 and #45).

On 2026-11-11 the maintainer decided that 10/25/15 stays only as a per-hour guide, not a rule, and not as a claim about attention. Plan a break every hour, with about 50 minutes of teaching. The 10 is the size of the explain-and-demonstrate opening, kept small enough that a novice can do the task afterward, because experts underestimate novice time (about 3 to 5 minutes for an expert versus 9 to 12 for a novice). The rest of the hour is guided practice, then solo practice and review.

## Protocol metaphors (section 5)

**TCP Reset (RST):** An emergency brake cord on *that* transit car. When pulled, that connection's pending buffers drop and the TCB is torn down immediately (no FIN handshake). Other sessions on the same host keep running.

A RST aborts that TCP connection (RFC 9293 §§3.5.3, 3.10.7.4). It does not drop every session on the host.

**TLS SNI (Server Name Indication):** In classic TLS, the server name is the cleartext address written on the outside of an opaque envelope: anyone handling the envelope can see where it is going, even if they cannot read the contents. Encrypted Client Hello (ECH), when it is in use, hides that name from on-path observers.

Classic SNI in the ClientHello is cleartext (RFC 6066). Encrypted Client Hello hides the server name from on-path observers when it is negotiated.
