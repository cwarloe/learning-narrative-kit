# Portland Desk — Trust on Paper

*A Security+ cryptography / PKI precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

The first [[ticket|ticket]] of the morning was already negotiating with a calendar. Jules had a sticky under *which decision?* that said *is this encryption, hashing, or cosplay?*

"[[encryption|Encryption]] hides. [[hashing|Hashing]] fingerprints. [[encoding|Encoding]] reshapes for travel," she said when I reached for a blank card. "If you confuse those three, you will soothe the wrong panic. Respect the warning. Check the name. Never treat Base64 like a vault, and never treat a board deck as a reason to click Advanced."

I opened the [[help_desk|help desk]] queue.

```ticket
id: HD-4502
priority: High
status: Open
queue: Help Desk
from: Maya (Accounting)
opened: Tue 08:06
subject: Site says not secure — board deck in 10 — can I click Advanced?
```

## Maya and the warning that wants to be ignored

Maya from accounting shared her screen. The dialog was red in the way browsers only bother with when they mean it. She had already hovered *Advanced*, which is a muscle people build in airports.

```gui
kind: cert-warning
chrome: https://vendor-portal.example
heading: Your connection isn't private
error: NET::ERR_CERT_DATE_INVALID
issued_to: vendor-portal.example
issued_by: Vendor TLS R3
valid: Jan 12, 2025 – Jan 12, 2026
status: Expired yesterday
actions: Back to safety | Advanced
---
Attackers might be trying to steal your information from vendor-portal.example. The [[certificate|certificate]] expired. The [[browser_padlock|padlock]] is gone on purpose.
```

"It worked yesterday," she said. "Also the padlock is missing and my stomach knows. The board deck is in ten minutes and this is the only portal the vendor uses for the numbers."

I checked the details. Vendor portal. [[expired_cert|Expired certificate]]. The date in the dialog was not a suggestion. I almost said *we can click through for ten minutes* because her meeting was real and the portal had been theirs last week. I did not, because Jules was two cubes away and because the dialog is the part of [[tls|TLS]] the user is allowed to see.

"Do not click through," I said. "TLS is how [[https|HTTPS]] proves the channel and encrypts the session. An expired cert means validation failed on purpose. We open a ticket to the vendor and to our web team. We do not teach the browser that warnings are optional, and we do not teach the board that Advanced is a calendar feature."

Maya exhaled. "So the meeting…?"

"Phone bridge. Hotspot. Cheaper than sending [[plaintext|plaintext]] passwords to a site your browser already refused."

She ran the meeting on a phone bridge and was late, and she sent me a message afterward that the vendor had "just forgotten to renew." Jules, from two cubes away: "Expired is the friendly failure. Name mismatch and untrusted issuer are the siblings. Same rule. Stop."

## Encoding cosplay and the 'encrypted' spreadsheet

Ken from sales pasted a string into chat that looked like alphabet soup and captioned it *encrypted vendor token — keep safe!!!* The exclamation points were doing more work than the math.

I decoded it in a safe scratch pad, not because I am dramatic, but because Slack is not a vault and I have already watched one token travel farther than its owner meant.

```console
caption: scratch pad · decode
PS C:\scratch> [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("aHR0cHM6Ly9hcGkuLi4="))
https://api.vendor.example/v1/token=sk_live_8f3c…   # URL + API key, reversible on purpose
```

```table
caption: Costume versus vault
| What Ken called it | What it was | What would actually hide it |
| --- | --- | --- |
| Encrypted vendor token | [[base64|Base64]] [[encoding|encoding]] | [[encryption|Encryption]] with a key, producing [[ciphertext|ciphertext]] |
| Keep safe!!! | A secret in a costume | Vault or a ticket, not Slack |
```

"That is encoding," I said. "Reversible on purpose. Anyone can undo it. Encryption would need a key and would produce ciphertext you cannot casually reverse. What you pasted is luggage labeling. The luggage still has your name on it."

Ken looked betrayed by the alphabet. "So I just pasted a password into Slack."

"You pasted a secret in a costume," I said. "Rotate the key. Next time: vault or ticket. I will stay on this until the rotation is real, because 'I'll do it after the demo' is how costumes travel."

He rotated it after a second ping from me. While we were on vocabulary, a developer asked whether renaming variables was "crypto enough" for a client demo script.

"[[obfuscation|Obfuscation]]," Jules said, still typing. "Makes reading annoying. Does not make it confidential. If the client can unzip it, it was never a vault."

## Symmetric, asymmetric, and the package metaphor

Network drew on the whiteboard like a person who had given this talk too many times and had accepted that they would give it again. I copied it down because I am still the person who will be asked to translate it at 4 p.m.

"[[symmetric|Symmetric encryption]] is one shared key — fast for bulk disks and big files. [[asymmetric|Asymmetric]] is a [[public_key|public key]] / [[private_key|private key]] pair — publish the public, guard the private with your career."

| | Symmetric | Asymmetric |
| --- | --- | --- |
| Keys | One shared secret | Public you can post, private you cannot |
| Speed | Fast — disks, backups, bulk files | Slow — introductions, signatures |
| Desk failure | Secret leaked in mail | Private key in a ticket attachment |

They sketched [[key_exchange|key exchange]]: strangers agree on a session secret over a noisy network so the heavy lifting can go symmetric afterward. Modern TLS handshakes lean on that story, and when configured for [[perfect_forward_secrecy|perfect forward secrecy]], yesterday's session keys stay boring even if a long-term private key has a bad day later.

I wrote the desk version under the table: users do not pick algorithms. Users notice when the padlock fails. We escalate algorithm drama; we coach warning manners. The whiteboard is for us. The dialog is for Maya.

## Signatures, hashing, salt, integrity

Sam forwarded a "signed" invoice PDF that his laptop would not trust. He had already asked three people whether the hash in the email was "the same religion."

"It says the signature is invalid," he said. "Also someone told me the file hash should match the email. I do not know which red I am supposed to believe."

"Same neighborhood," I said. "A [[digital_signature|digital signature]] uses a private key so anyone with the public key can check origin and [[integrity|integrity]]. If the file changed or the key is wrong, verification fails — that is the feature, not a broken PDF reader. Separately, a hash of the file is a fingerprint: same file, same digest; change one byte, digest moves. Hashes do not encrypt. They detect tampering."

```table
caption: Why the PDF failed two different tests
| Check | What we fed it | Result |
| --- | --- | --- |
| SHA-256 of vendor email | `9f2c…c41a` | Does not match the file Sam saved |
| SHA-256 of the file on disk | `0aa1…77de` | One byte in the footer is not the vendor's |
| Signature | Vendor public key | Invalid — wrong key, or the file moved |
```

Nora from ops asked, because she had been listening, why password resets talk about salt like cooking.

"[[salting|Salting]]," I said. "Random garnish in the password hash so 'Password1!' does not look identical in every stolen database. Still hashing — not reversible encryption of the password. If someone can 'decrypt your hash,' they are using a different sentence than we are."

Sam's invoice stayed untrusted. Finance used the vendor portal instead, which made Sam late on a deliverable he did not cause. [[non_repudiation|Non-repudiation]] can wait for a key that actually verifies. It is the courtroom cousin of a good signature, not a vibe, and it does not care that the invoice was urgent.

## PKI on paper: CA, chain, CSR

Web team swung by with a renewal drama that had become a desk ticket because users feel it first. They brought a printout. I have learned that printouts of certificates mean someone is already tired.

"Our [[pki|PKI]] is boring until it isn't," the engineer said. "End-entity certificate binds a name to a public key. A [[ca|certificate authority]] signs it. We keep the root cold and use an [[intermediate_ca|intermediate CA]] in the [[certificate_chain|certificate chain]] so browsers can walk from leaf to a root in the [[trust_store|trust store]]."

```chain
caption: What a sober browser walks
- Portland Root CA | trusted | In the trust store. Stays cold.
- Vendor Intermediate | trusted | Presented with the leaf.
- vendor-portal.example | expired | Leaf. Name matches. Date does not.
```

They showed a [[csr|CSR]] sitting in a ticket: public key plus identity fields waiting for a signature. Private key never leaves the [[hsm|HSM]] if we are doing this correctly — hardware that generates and guards keys so [[key_management|key management]] is not a shared drive named `keys_final_FINAL`.

```ticket
id: CHG-118
priority: Medium
status: Waiting on CA
queue: Web / PKI
from: web-ops
subject: CSR for vendor-portal.example — private key in HSM, do not attach
```

"Someone asked for a [[wildcard_cert|wildcard certificate]] for every subdomain because typing is hard," the engineer added. "Convenient. Larger blast radius if stolen. We will be specific unless the architecture earns the star."

I translated for the queue: when users see untrusted issuer, the chain is broken, incomplete, or foreign to our trust store. When they see a lab appliance warning, it is often [[self_signed|self-signed]] — signed by itself, trusted by no one sober. The CSR is the ask. The HSM is the adult in the room. The wildcard is a convenience with a radius.

## Self-signed, pinning, and the app that remembers too hard

Dev from engineering installed an internal tool that had worked on the old hostname and now screamed. He was proud of having "fixed TLS" in the way people are proud of having painted over a crack.

"I generated a cert on the box," he said. "Self-signed. Then I told everyone to click through. Also the mobile app pinned the old cert and now refuses the new one even though I fixed TLS."

"Self-signed is a lab handshake, not a production welcome mat," I said. "Issue a real cert from our CA path — CSR in, signed cert out, private key in the HSM or the approved store. And [[certificate_pinning|pinning]]: the app remembered a specific cert or key. Strong against some middlepeople. Brittle when you rotate. Coordinate pin updates with cert swaps or you invent an outage shaped like security, which is the kind of outage that trains people to click Advanced."

Dev filed the grown-up CSR. Mobile team scheduled a pin bump. Users stopped receiving "just click Advanced" coaching from engineering Slack, mostly. One person still forwarded the old advice. I replied in the thread with the ticket number and did not add a lecture, because the ticket number is the lecture.

## Steganography, escrow, and the ticket that is actually SOC

A curious intern asked whether hiding a spreadsheet inside a cat GIF was "secure enough for HR." He had the GIF. I did not open it.

"[[steganography|Steganography]] hides existence," I said. "Cute on exams. Not a control for payroll. Use encryption and access control. Cats are not a cryptosystem, and HR is not a puzzle hunt."

Separately, Legal asked whether we could decrypt a departed employee's disk "because key escrow," which is a sentence that wants to be true after the fact.

"[[key_escrow|Key escrow]] means a copy of recovery material lives with a trusted party under policy," Jules said. She had put her vendor call on hold to say it, which meant she did not want me improvising. "We either designed for that or we did not. We do not invent escrow after the fact by guessing. If recovery keys exist in the approved vault, Facilities and Security follow the script. If not, that is a leadership decision — not a help-desk miracle, and not a reason to start trying passwords we do not have."

A noisy alert about a site presenting a swapped cert chain got a [[soc|SOC]] handoff. Desk collected screenshots of the [[cert_warning|warning]], hostname, and time. We did not tell users to proceed because the demo was important. The demo moved. The warning stayed.

## Name mismatch, chain gaps, and the appliance in the closet

Afternoon brought three cousins of Maya's expired portal. I put them on one wiki page because they are the same muscle with different red text.

First: a marketing microsite served as `promo.company.example` with a certificate minted for `www.company.example`. The browser was correct to sulk — identity binding failed even though encryption might still have been happening with the wrong nametag.

```gui
kind: cert-warning
chrome: https://promo.company.example
heading: Your connection isn't private
error: NET::ERR_CERT_COMMON_NAME_INVALID
issued_to: www.company.example
status: Name mismatch
actions: Back to safety | Advanced
---
The padlock would be lying if we clicked through. Encrypted to the wrong name is still a failure.
```

Second: a partner upload tool missing the intermediate in what it sent. The leaf looked fine in isolation; the chain did not walk to a root in our trust store. Users saw untrusted issuer. The fix was to serve the intermediate, not to coach Advanced.

```chain
caption: Partner upload tool — what the browser actually got
- Portland Root CA | trusted | In the trust store
- Partner Intermediate | missing | Not presented. Walk stops.
- upload.partner.example | broken | Leaf looks fine alone. Alone is not a chain.
```

Third: a camera NVR in a closet with a factory self-signed web UI. Facilities wanted a ticket titled *make the red go away.* We either put it behind a jump host with a real cert story or accepted that the warning was accurate. We did not train fifty people to ignore red for one appliance. Facilities did not like that answer. The warning stayed, and I wrote *do not click through for cameras either* on the closet door in a Sharpie Jules later replaced with a printed label, which is how closets become policy.

## Key custody theater versus HSM adulthood

A well-meaning admin attached a `.pem` to an email thread named `do_not_share_private_key_but_here_it_is`. I felt my career shorten by a week, which is not a cryptographic term.

```console
caption: mail thread · do not do this
From: admin@company.example
Subject: do_not_share_private_key_but_here_it_is
Attachment: vendor-portal.key.pem   (private key)

# This is the opposite of key management.
# Revoke. Rotate. Never store this in the ticket.
```

"That attachment is the opposite of key management," I said on the bridge. "Private keys do not ride mail. If we need recovery, we use approved escrow or platform recovery — not archaeology in Sent Items. Production keys belong in the HSM or the cloud KMS our architecture already paid for."

They revoked, rotated, and scheduled a short postmortem. I updated the ticket template with one line: *never accept a private key via help-desk attachment — escalate, do not store.* The admin apologized in a way that meant they understood the radius. Jules unmuted long enough to say, "Good. Keep the apology off the wiki. Keep the template."

At 5:40 the queue was quieter. Maya had used the phone bridge and was still annoyed about being late. Ken had rotated the token. Sam's invoice had stayed untrusted. The closet camera was still red. The `.pem` was revoked and I still wanted to wash my hands.

Jules clipped her bike lights on. "Tomorrow someone will forward a 'secure' Base64 password and ask why the padlock looks sad."

I shut the laptop. The padlock on our own wiki was the ordinary color. I went out into the rain.
