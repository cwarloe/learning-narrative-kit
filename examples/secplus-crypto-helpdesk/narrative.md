# Portland Desk — Trust on Paper

*A Security+ cryptography / PKI precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

The first [[ticket|ticket]] of the morning was *Site says not secure — board deck in 10 — can I click Advanced?* Jules had a sticky under *which decision?* that said *is this encryption, hashing, or cosplay?*

"[[encryption|Encryption]] hides. [[hashing|Hashing]] fingerprints. [[encoding|Encoding]] reshapes for travel," she said when I reached for a blank card. "If you confuse those three, you will soothe the wrong panic. Respect the warning. Check the name. Never treat Base64 like a vault."

I opened the [[help_desk|help desk]] queue.

## Maya and the warning that wants to be ignored

Maya from accounting shared her screen. A big [[cert_warning|certificate warning dialog]]. Red. Words like *expired* and *do not proceed*. She had already hovered *Advanced*.

"It worked yesterday," she said. "Also the [[browser_padlock|padlock]] is missing and my stomach knows."

I checked the details. Vendor portal. [[expired_cert|Expired certificate]].

"Do not click through," I said. "[[tls|TLS]] is how [[https|HTTPS]] proves the channel and encrypts the session. An expired cert means validation failed on purpose. We open a ticket to the vendor and to our web team. We do not teach the browser that warnings are optional."

Maya exhaled. "So the meeting…?"

"Phone bridge. Hotspot. Cheaper than sending [[plaintext|plaintext]] passwords to a site your browser already refused."

She ran the meeting on a phone bridge and was late. Jules, from two cubes away: "Expired is the friendly failure. Name mismatch and untrusted issuer are the siblings. Same rule. Stop."

## Encoding cosplay and the 'encrypted' spreadsheet

Ken from sales pasted a string into chat that looked like alphabet soup and captioned it *encrypted vendor token — keep safe!!!*

I decoded it in a safe scratch pad. It was a URL and an API key in [[base64|Base64]].

"That is encoding," I said. "Reversible on purpose. Anyone can undo it. Encryption would need a key and would produce [[ciphertext|ciphertext]] you cannot casually reverse."

Ken looked betrayed by the alphabet. "So I just pasted a password into Slack."

"You pasted a secret in a costume," I said. "Rotate the key. Next time: vault or ticket."

He rotated it after a second ping from me. While we were on vocabulary, a developer asked whether renaming variables was "crypto enough" for a client demo script.

"[[obfuscation|Obfuscation]]," Jules said, still typing. "Makes reading annoying. Does not make it confidential."

## Symmetric, asymmetric, and the package metaphor

Network drew on the whiteboard like a person who had given this talk too many times.

"[[symmetric|Symmetric encryption]] is one shared key — fast for bulk disks and big files. [[asymmetric|Asymmetric]] is a [[public_key|public key]] / [[private_key|private key]] pair — publish the public, guard the private."

They sketched [[key_exchange|key exchange]]: strangers agree on a session secret over a noisy network so the heavy lifting can go symmetric afterward. Modern TLS handshakes lean on that story, and when configured for [[perfect_forward_secrecy|perfect forward secrecy]], yesterday's session keys stay boring even if a long-term private key has a bad day later.

I wrote the desk version: users do not pick algorithms. Users notice when the padlock fails. We escalate algorithm drama; we coach warning manners.

## Signatures, hashing, salt, integrity

Sam forwarded a "signed" invoice PDF that his laptop would not trust.

"It says the signature is invalid," he said. "Also someone told me the file hash should match the email. Those feel like different religions."

"Same neighborhood," I said. "A [[digital_signature|digital signature]] uses a private key so anyone with the public key can check origin and [[integrity|integrity]]. If the file changed or the key is wrong, verification fails — that is the feature. Separately, a hash of the file is a fingerprint: same file, same digest; change one byte, digest moves. Hashes do not encrypt. They detect tampering."

Nora from ops asked why password resets talk about salt like cooking.

"[[salting|Salting]]," I said. "Random garnish in the password hash so 'Password1!' does not look identical in every stolen database. Still hashing — not reversible encryption of the password."

Sam's invoice stayed untrusted. Finance used the vendor portal instead. [[non_repudiation|Non-repudiation]] can wait for a key that actually verifies. It is the courtroom cousin of a good signature, not a vibe.

## PKI on paper: CA, chain, CSR

Web team swung by with a renewal drama that had become a desk ticket because users feel it first.

"Our [[pki|PKI]] is boring until it isn't," the engineer said. "End-entity [[certificate|certificate]] binds a name to a public key. A [[ca|certificate authority]] signs it. We keep the root cold and use an [[intermediate_ca|intermediate CA]] in the [[certificate_chain|certificate chain]] so browsers can walk from leaf to a root in the [[trust_store|trust store]]."

They showed a [[csr|CSR]] sitting in a ticket: public key plus identity fields waiting for a signature. Private key never leaves the [[hsm|HSM]] if we are doing this correctly — hardware that generates and guards keys so [[key_management|key management]] is not a shared drive named `keys_final_FINAL`.

"Someone asked for a [[wildcard_cert|wildcard certificate]] for every subdomain because typing is hard," the engineer added. "Convenient. Larger blast radius if stolen. We will be specific unless the architecture earns the star."

I translated for the queue: when users see untrusted issuer, the chain is broken, incomplete, or foreign to our trust store. When they see a lab appliance warning, it is often [[self_signed|self-signed]] — signed by itself, trusted by no one sober.

## Self-signed, pinning, and the app that remembers too hard

Dev from engineering installed an internal tool that had worked on the old hostname and now screamed.

"I generated a cert on the box," he said. "Self-signed. Then I told everyone to click through. Also the mobile app pinned the old cert and now refuses the new one even though I fixed TLS."

"Self-signed is a lab handshake, not a production welcome mat," I said. "Issue a real cert from our CA path — CSR in, signed cert out, private key in the HSM or the approved store. And [[certificate_pinning|pinning]]: the app remembered a specific cert or key. Strong against some middlepeople. Brittle when you rotate. Coordinate pin updates with cert swaps or you invent an outage shaped like security."

Dev filed the grown-up CSR. Mobile team scheduled a pin bump. Users stopped receiving "just click Advanced" coaching from engineering Slack, mostly. One person still forwarded the old advice. I replied in the thread with the ticket number.

## Steganography, escrow, and the ticket that is actually SOC

A curious intern asked whether hiding a spreadsheet inside a cat GIF was "secure enough for HR."

"[[steganography|Steganography]] hides existence," I said. "Cute on exams. Not a control for payroll. Use encryption and access control."

Separately, Legal asked whether we could decrypt a departed employee's disk "because key escrow."

"[[key_escrow|Key escrow]] means a copy of recovery material lives with a trusted party under policy," Jules said. "We either designed for that or we did not. We do not invent escrow after the fact by guessing. If recovery keys exist in the approved vault, Facilities and Security follow the script. If not, that is a leadership decision — not a help-desk miracle."

A noisy alert about a site presenting a swapped cert chain got a [[soc|SOC]] handoff. Desk collected screenshots of the warning, hostname, and time. We did not tell users to proceed because the demo was important.

## Name mismatch, chain gaps, and the appliance in the closet

Afternoon brought three cousins of Maya's expired portal.

First: a marketing microsite served as `promo.company.example` with a certificate minted for `www.company.example`. The browser was correct to sulk — identity binding failed even though encryption might still have been happening with the wrong nametag.

Second: a partner upload tool missing the intermediate in what it sent. The leaf looked fine in isolation; the chain did not walk to a root in our trust store. Users saw untrusted issuer. The fix was to serve the intermediate, not to coach Advanced.

Third: a camera NVR in a closet with a factory self-signed web UI. Facilities wanted a ticket titled *make the red go away.* We either put it behind a jump host with a real cert story or accepted that the warning was accurate. We did not train fifty people to ignore red for one appliance. Facilities did not like that answer. The warning stayed.

I pasted all three into the wiki as TLS failure modes the desk actually sees.

## Key custody theater versus HSM adulthood

A well-meaning admin attached a `.pem` to an email thread named `do_not_share_private_key_but_here_it_is`.

"That attachment is the opposite of key management," I said on the bridge. "Private keys do not ride mail. If we need recovery, we use approved escrow or platform recovery — not archaeology in Sent Items. Production keys belong in the HSM or the cloud KMS our architecture already paid for."

They revoked, rotated, and scheduled a short postmortem. I updated the ticket template with one line: *never accept a private key via help-desk attachment — escalate, do not store.*

At 5:40 the queue was quieter. Maya had used the phone bridge. Ken had rotated the token. Sam's invoice had stayed untrusted. The closet camera was still red.

Jules clipped her bike lights on. "Tomorrow someone will forward a 'secure' Base64 password and ask why the padlock looks sad."

I shut the laptop. The padlock on our own wiki was the ordinary color. I went out into the rain.
