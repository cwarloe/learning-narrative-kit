# Prompt 5 — Helpdesk Realism

- **Title:** Realistic help-desk / MSP tickets that force secure-vs-insecure protocol choices
- **Model used:** Best (Sonar was not available in the displayed picker)
- **URL:** https://www.perplexity.ai/search/26977d1c-0691-41b6-bb43-4de1c64c88ff

## Full answer

Telnet vs SSH: ticket asks to enable SSH and disable Telnet; user asks for secure remote access. Correct decision: disable Telnet and require SSH with strong authentication and (preferably) key-based logins. Wrong convenience ask: “Use Telnet for quick testing.” Sources emphasize replacing insecure protocols with secure equivalents and disabling legacy services.

FTP vs SFTP/FTPS: ticket often requests FTP for file transfers; correct: mandate SFTP/FTPS and disable FTP; ensure firewall rules and client support. Wrong ask: “FTP is fine for speed and simplicity.” Guidance notes encryption and credential exposure, recommending SFTP/FTPS.

HTTP vs HTTPS: ticket may request http; correct: force HTTPS with valid TLS, HSTS, and certificate management; disable plain HTTP. Wrong ask: “HTTP is enough for internal use.” Guidance stresses secure web protocols and TLS/HTTPS for confidentiality and integrity.

RDP exposure: ticket might involve exposing RDP to internet; correct: require VPN or RD Gateway with TLS/NLA; disable direct external RDP. Wrong ask: “Open RDP directly to the internet for remote access.” Security guidance recommends VPN/NLA/TLS and gateway approaches.

LDAP vs LDAPS: ticket could involve directory access; correct: use LDAPS or StartTLS; disable LDAP over cleartext. Wrong ask: “LDAP without encryption is fine for internal use.” Guidance highlights need for secure directory access.

SNMP v1/v2c vs SNMPv3: ticket may surface SNMP read/write with community strings; correct: migrate to SNMPv3 with authPriv; rotate/change community strings; disable v1/v2c. Wrong ask: “Use public/community strings for simplicity.” Security notes warn about plaintext communities and exposure.

LDAP/LDAPS and mail protocols: for mail, prefer IMAPS/Submission (587) over plain SMTP/POP with plaintext; disable plaintext submission/IMAP. Wrong: “Use plain mail protocols for ease.” References stress secure mail delivery and authentication.

TFTP, SNMPv1/v2c, and cleartext protocols: common MSP ticket asks for quick config using TFTP or SNMP v1; correct: stop using TFTP; disable TFTP; use secure alternatives and log centralized; rotate credentials. Wrong: “Keep TFTP for device backups.” Plaintext protocols risk exposure.

If you want, I can tailor a practitioner-focused cheat sheet with concrete ticket-origins, decision trees, and vendor KB links.

**Sources:** 10 sources were cited in the answer, including AlgoSec and Exam Preprise source cards.
