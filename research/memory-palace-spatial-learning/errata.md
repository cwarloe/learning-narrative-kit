# Errata for the architecture document

[`cognitive-spatial-technical-learning-architecture.md`](cognitive-spatial-technical-learning-architecture.md) is an unedited export of the Google Doc. The two protocol metaphors in section 5 should be read as follows. The export itself is left unchanged unless the Drive original is revised and re-exported.

**TCP Reset (RST):** An emergency brake cord on *that* transit car. When pulled, that connection's pending buffers drop and the TCB is torn down immediately (no FIN handshake). Other sessions on the same host keep running.

A RST aborts that TCP connection (RFC 9293 §§3.5.3, 3.10.7.4). It does not drop every session on the host.

**TLS SNI (Server Name Indication):** In classic TLS, the server name is the cleartext address written on the outside of an opaque envelope: anyone handling the envelope can see where it is going, even if they cannot read the contents. Encrypted Client Hello (ECH), when it is in use, hides that name from on-path observers.

Classic SNI in the ClientHello is cleartext (RFC 6066). Encrypted Client Hello hides the server name from on-path observers when it is negotiated.
