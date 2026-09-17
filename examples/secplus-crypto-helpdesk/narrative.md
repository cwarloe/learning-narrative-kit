# Portland Desk — Trust on Paper

*A Security+ cryptography / PKI precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Tuesday rain has opinions again. I am Ethan, still week-something at the [[help_desk|help desk]], and today the queue is not doors or radios — it is trust on paper, padlocks that lie, and math that users only meet as a scary dialog.

Jules has a sticky under *which decision?* that says *is this encryption, hashing, or cosplay?* Bike helmet on the monitor arm. She is not teaching number theory. She is keeping people from clicking through a warning because the meeting started.

"Crypto at the desk is mostly triage," she says when I reach for a blank card. "[[encryption|Encryption]] hides. [[hashing|Hashing]] fingerprints. [[encoding|Encoding]] reshapes for travel. If you confuse those three, you will soothe the wrong panic. Your job is the decision — respect the warning, check the name, escalate the broken chain, and never treat Base64 like a vault."

I open the queue. Coffee. Portland doing Portland. First [[ticket|ticket]] subject: *Site says not secure — board deck in 10 — can I click Advanced?*

## Maya and the warning that wants to be ignored

Maya from accounting — door-politeness alumnus — shares her screen. Big [[cert_warning|certificate warning dialog]]. Red. Words like *expired* and *do not proceed*. She has already hovered *Advanced* like it owes her a favor.

"It worked yesterday," she says. "Also the [[browser_padlock|padlock]] is missing and my stomach knows."

I check the details. Vendor portal. [[expired_cert|Expired certificate]]. Calendar does not negotiate.

"Do not click through," I say. "[[tls|TLS]] is how [[https|HTTPS]] proves the channel and encrypts the session. An expired cert means validation failed on purpose. We open a ticket to the vendor and to our web team — we do not teach the browser that warnings are optional."

Maya exhales. "So the meeting…?"

"Phone bridge. Hotspot. Embarrassing delay. Cheaper than sending [[plaintext|plaintext]] passwords to a site your browser already refused."

Jules adds, from two cubes away: "Expired is the friendly failure. Name mismatch and untrusted issuer are the siblings. Same rule: stop."

## Encoding cosplay and the 'encrypted' spreadsheet

Ken from sales pastes a string into chat that looks like alphabet soup and captions it *encrypted vendor token — keep safe!!!*

I decode it in a safe scratch pad. It is a URL and an API key in [[base64|Base64]].

"That is [[encoding|encoding]]," I say. "Reversible on purpose. Anyone can undo it. [[encryption|Encryption]] would need a key and would produce [[ciphertext|ciphertext]] you cannot casually reverse. What you have is luggage labeling."

Ken looks betrayed by the alphabet. "So I just pasted a password into Slack."

"You pasted a secret in a costume," I say. "Rotate the key. Next time: vault or ticket, not cosplay."

While we are on vocabulary, a developer asks whether renaming variables is "crypto enough" for a client demo script.

"[[obfuscation|Obfuscation]]," Jules says. "Makes reading annoying. Does not make it confidential. Do not sell annoyance as encryption."

## Symmetric, asymmetric, and the package metaphor

Lunch-hour hallway class because Tuesday allows it. Network draws on the whiteboard like a person who has given this talk too many times.

"[[symmetric|Symmetric encryption]] is one shared key — fast for bulk disks and big files. [[asymmetric|Asymmetric]] is a [[public_key|public key]] / [[private_key|private key]] pair — publish the public, guard the private with your career."

They sketch [[key_exchange|key exchange]]: strangers agree on a session secret over a noisy network so the heavy lifting can go symmetric afterward. Modern [[tls|TLS]] handshakes lean on that story, and when configured for [[perfect_forward_secrecy|perfect forward secrecy]], yesterday's session keys stay boring even if a long-term private key has a bad day later.

I write the desk version: users do not pick algorithms. Users notice when the padlock fails. We escalate algorithm drama; we coach warning manners.

## Signatures, hashing, salt, integrity

Sam — contractor, USB historian — forwards a "signed" invoice PDF that his laptop will not trust.

"It says the signature is invalid," he says. "Also someone told me the file hash should match the email. Those feel like different religions."

"Same neighborhood," I say. "A [[digital_signature|digital signature]] uses a private key so anyone with the public key can check origin and [[integrity|integrity]]. If the file changed or the key is wrong, verification fails — that is the feature. Separately, a [[hashing|hash]] of the file is a fingerprint: same file, same digest; change one byte, digest moves. Hashes do not encrypt. They detect tampering."

Nora from ops asks why password resets talk about salt like cooking.

"[[salting|Salting]]," I say. "Random garnish in the password hash so 'Password1!' does not look identical in every stolen database. Still hashing — not reversible encryption of the password."

Jules taps the sticky: *signatures prove; hashes check; salts frustrate rainbow tables; none of that is 'click through the red page.'*

Sam's invoice stays untrusted. Finance uses the vendor portal instead. Non-repudiation can wait for a key that actually verifies — [[non_repudiation|non-repudiation]] is the courtroom cousin of a good signature, not a vibe.

## PKI on paper: CA, chain, CSR

Web team swings by with a renewal drama that has become a desk ticket because users feel it first.

"Our [[pki|PKI]] is boring until it isn't," the engineer says. "End-entity [[certificate|certificate]] binds a name to a public key. A [[ca|certificate authority]] signs it. We keep the root cold and use an [[intermediate_ca|intermediate CA]] in the [[certificate_chain|certificate chain]] so browsers can walk from leaf to a root in the [[trust_store|trust store]]."

They show a [[csr|CSR]] sitting in a ticket: public key plus identity fields waiting for a signature. Private key never leaves the [[hsm|HSM]] if we are doing adulthood correctly — hardware that generates and guards keys so [[key_management|key management]] is not a shared drive named `keys_final_FINAL`.

"Someone asked for a [[wildcard_cert|wildcard certificate]] for every subdomain because typing is hard," the engineer adds. "Convenient. Larger blast radius if stolen. We will be specific unless the architecture earns the star."

I translate for the queue: when users see untrusted issuer, the chain is broken, incomplete, or foreign to our trust store. When they see a lab appliance warning, it is often [[self_signed|self-signed]] — signed by itself, trusted by no one sober.

## Self-signed, pinning, and the app that remembers too hard

Dev from engineering installs an internal tool that worked on the old hostname and now screams.

"I generated a cert on the box," he says proudly. "Self-signed. Then I told everyone to click through. Also the mobile app pinned the old cert and now refuses the new one even though I fixed TLS."

"Self-signed is a lab handshake, not a production welcome mat," I say. "Issue a real cert from our CA path — CSR in, signed cert out, private key in the HSM or the approved store. And [[certificate_pinning|pinning]]: the app remembered a specific cert or key. Strong against some middlepeople. Brittle when you rotate. Coordinate pin updates with cert swaps or you invent an outage shaped like security."

Dev files the grown-up CSR. Mobile team schedules a pin bump. Users stop receiving "just click Advanced" coaching from engineering Slack. Jules sends a thank-you react that feels like a performance review.

## Steganography, escrow, and the ticket that is actually SOC

Late day, a curious intern asks whether hiding a spreadsheet inside a cat GIF is "secure enough for HR."

"[[steganography|Steganography]] hides existence," I say. "Cute on exams. Not a control for payroll. Use encryption and access control. Cats are not a cryptosystem."

Separately, Legal asks whether we can decrypt a departed employee's disk "because key escrow."

"[[key_escrow|Key escrow]] means a copy of recovery material lives with a trusted party under policy," Jules says carefully. "We either designed for that or we did not. We do not invent escrow after the fact by guessing. If recovery keys exist in the approved vault, Facilities and Security follow the script. If not, that is a leadership decision — not a help-desk miracle."

A noisy alert about a site presenting a swapped cert chain gets a [[soc|SOC]] handoff. Desk collects screenshots of the [[cert_warning|warning]], hostname, and time. We do not tell users to proceed because the demo is important.


## Name mismatch, chain gaps, and the appliance in the closet

Afternoon brings three cousins of Maya's expired portal.

First: a marketing microsite served as `promo.company.example` with a certificate minted for `www.company.example`. Browser is correct to sulk — identity binding failed even though [[encryption|encryption]] might still be happening with the wrong nametag.

Second: a partner upload tool missing the intermediate in what it sends. Leaf looks fine in isolation; the [[certificate_chain|chain]] does not walk to a root in our [[trust_store|trust store]]. Users see untrusted issuer. Fix is serve the intermediate, not coach "Advanced."

Third: a camera NVR in a closet with a factory [[self_signed|self-signed]] web UI. Facilities wants a ticket titled *make the red go away.* We either put it behind a jump host with a real cert story or accept that the warning is accurate. We do not train fifty people to ignore red for one appliance.

I paste all three into the wiki as "TLS failure modes the desk actually sees." Jules adds: *ciphertext to the wrong name is still a failure.*

## Key custody theater versus HSM adulthood

A well-meaning admin attaches a `.pem` to an email thread named `do_not_share_private_key_but_here_it_is`. I feel my career shorten by a week.

"That attachment is the opposite of [[key_management|key management]]," I say on the bridge. "[[private_key|Private keys]] do not ride mail. If we need recovery, we use approved escrow or platform recovery — not archaeology in Sent Items. Production keys belong in the [[hsm|HSM]] or the cloud KMS our architecture already paid for."

They revoke, rotate, and schedule a short shame-free postmortem. I update the ticket template with one line: *never accept a private key via help-desk attachment — escalate, do not store.*

## The line that sticks

5:40. Queue quieter. Rain still editorializing. I rewrite the wiki blurb the desk will actually keep:

Encryption hides with keys; hashing fingerprints; encoding is Base64 cosplay; obfuscation is camouflage without math strength. Symmetric shares one key; asymmetric shares public, guards private; key exchange sets up the session; PFS keeps old sessions dull after theft. Signatures and hashes serve integrity; salts save password dumps from being boring. PKI is CA plus intermediate plus chain plus trust store; CSR asks; HSM holds; wildcards are convenience with blast radius. Respect TLS warnings — expired, self-signed, broken chain, pin mismatch. Steganography is hide-and-seek; escrow is policy, not improv.

Jules clips her bike lights on. "How many algorithms did you memorize?"

"None," I say. "I collected a few decisions — warning versus meeting panic, encoding versus encryption, self-signed versus CA, pin versus rotate — and a few shapes the sticky needs: [[encryption|encryption]], [[hashing|hashing]], [[digital_signature|signature]], [[certificate|certificate]], [[ca|CA]], [[tls|TLS]], [[expired_cert|expired]]."

She nods once. "Trust is paperwork with math underneath. Tomorrow someone will forward a 'secure' Base64 password and ask why the padlock looks sad."

I shut the laptop. The [[browser_padlock|padlock]] on our own wiki glows the ordinary color. That, for Tuesday, is enough.
