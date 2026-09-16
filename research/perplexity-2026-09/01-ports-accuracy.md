# 1 ports accuracy
Model used: Best (auto-selected; Sonar was not listed in the picker)
URL: https://www.perplexity.ai/search/c490bf48-5bf6-4f6c-b62a-1ef37d5a33eb

## Insecure vs secure pairs (common ports and transports)

| Insecure / baseline | Common port(s)/transport | Why risky | Secure replacement | Official objective vs community-guide status / disputes |
|---|---|---|---|---|
| HTTP vs HTTPS | HTTP 80/TCP; HTTPS 443/TCP | HTTP traffic is unencrypted, exposing credentials and data. | HTTPS with TLS (often still called SSL in older material). | Secure HTTPS is named in objective language; 80/443 are widely accepted and not materially disputed in guides. |
| FTP vs SFTP/FTPS | FTP 20/21/TCP; SFTP 22/TCP; FTPS commonly 989/990 | FTP sends credentials and data in plaintext. | SFTP (SSH-based) on 22, or FTPS. | FTP and secure alternatives are common study-guide material. FTPS is a frequent port-number trap: implicit FTPS is commonly 989/990, while explicit FTPS commonly uses control 21 with TLS; guides vary. |
| Telnet vs SSH | Telnet 23/TCP; SSH 22/TCP | Telnet transmits credentials and session data in plaintext. | SSH on 22/TCP. | Telnet/SSH contrast is common exam prep; 23 and 22 are widely accepted. |
| Plain SMTP vs TLS-protected SMTP | SMTP 25/TCP; submission 587/TCP; SMTPS 465/TCP | Plain SMTP is exposed to interception; STARTTLS can be misconfigured or downgraded if not enforced. | STARTTLS on 25/587 or implicit TLS on 465. | Port use appears in study guides and operational references; exact 465/587 mapping varies by guide and deployment. |
| Unsecured DNS vs DoT/DoH | DNS 53/UDP (and TCP); DoT 853/TCP; DoH over HTTPS 443/TCP | Ordinary DNS is unauthenticated and can be spoofed or observed. | DNS-over-TLS (853) or DNS-over-HTTPS (443). | 53 is the standard baseline; DoT/DoH are commonly discussed in guides, but are not necessarily enumerated as SY0-701 objective port memorization. |
| Direct RDP vs protected RDP access | RDP 3389/TCP (and UDP in modern implementations) | Internet exposure invites brute-force, credential attacks, and interception risk. | VPN/private access, or RDP with TLS plus strong authentication and access controls. | 3389 is common guide material; the objective emphasis is secure implementation rather than a guarantee that 3389 must be memorized. |

### Notes
CompTIA objective language is higher-level (implement secure protocols / secure network services) and does not constitute a complete official port-number table. Exam-focused materials frequently list 80/443, 20/21, 22, 23, 25, 53, and 3389 as core. Treat auxiliary mappings and “official” claims cautiously: community guides often extend the list, and implicit vs explicit FTPS is the clearest disputed case. Port numbers can be implementation-dependent, so verify against IANA/RFC/vendor documentation for production work.

Sources surfaced by the answer included Professor Messer study material, SecPlusMastery’s port cheat sheet, and CyberKraft Training’s ports-and-protocols guide. The answer displayed 10 sources; citations were rendered as source labels rather than a full bibliography in the visible response.
