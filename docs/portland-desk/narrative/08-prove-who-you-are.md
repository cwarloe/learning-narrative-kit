# Portland Desk — Prove Who You Are

*A Security+ identity-and-authentication precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

The smell of wet wool and radiator steam filled the fourth floor long before the eight o'clock chime. Across the partition, Jules was running a dry-erase marker down a list of ninety-day password expiration notices that had triggered over the weekend.

"Two dozen people locked themselves out between Friday night and seven this Monday morning," Jules said, capping the blue marker with a sharp snap. "Half of them will swear up and down that typing a password and a PIN counts as multifactor. Don't argue with their frustration, Ethan. Separate what they know from what they hold."

On the dispatch display, the first incident ticket was already flashing red.

Jared had called my desk line on Tuesday about an unrelated switch, which he had never done before. He did not mention the Saturday, and neither did I. His tickets came back the same day after that. <!-- date-ok: weekdays of earlier calls, not the chapter's day -->

## Nora and the policy that keeps changing the locks

```callout-panel
title: "FIGURE 8.1: AUTHENTICATION FACTORS & ACCOUNT LOCKOUT"
badge: "Identity & Access"
caption: "Macro technical view: A corporate smartphone on a clean desk displaying rapid push notifications alongside an Active Directory security event log on a monitor."
prompt: "Clean technical illustration of a smartphone on an office desk next to a computer monitor under bright office lighting. The monitor displays security event logs with red warning highlights. Clean instructional manual style, crisp lines, no text, no words. 4:3 ratio."
```

Nora in finance could not reset. She had tried her old favorite three times. The portal said no.

"I always rotate the season and the year," she said on the phone. "Spring2024!, Summer2024! — that used to work everywhere. Now it hates me. Also it wants sixteen characters. Who remembers sixteen?"

I pulled the account. Password age was ninety-one days. Policy max was ninety. Her last change had slid under the wire last quarter; today the portal was enforcing password expiration before it would talk about a reset path.

"Expiration is why I'm calling," Nora said. "Every ninety days I invent a worse password and write it on a sticky. My cousin's home lab uses a [[passphrase|passphrase]] — four words, no sticky. Is that allowed, or do we still need the symbol salad?"

Jules leaned in just enough to be heard. "Ask what we are optimizing for."

"Length and uniqueness," I said. "Complexity rules still exist here — upper, lower, digit, symbol — but a long passphrase that clears length usually beats a short spicy one. And no password reuse across work and the streaming account you use at lunch. That Spring2024 pattern is reuse with a costume."

Nora snorted. "Costume. Fine. What do I type?"

We walked a passphrase she would actually remember, not a movie quote she had posted on socials. I reminded her the company password manager would store a unique password for every app so she was not inventing seasons. She groaned about another vault, then admitted her browser had already offered to save three variants of the same secret.

She set the passphrase. She did not install the manager on the call. "I'll do the vault later," she said. "I have a close." I put *manager still pending* in the ticket and left it open.

## Todd and the MFA that is not MFA

Todd in sales was locked out of the CRM after a phone wipe. He wanted a quick fix.

"I already have multifactor," Todd said. "Password plus a PIN on the laptop. Two things. That is MFA, right? My old shop said so."

I felt the flashcard reflex and almost agreed because the sentence had two nouns.

Jules's sticky was visible from my chair.

"A password and a PIN are both [[something_you_know|something you know]], Todd," I said. "Typing two secrets out of your head is just single-factor twice—not [[mfa|multifactor authentication]]. Real MFA needs two distinct factor types, like combining your password with [[something_you_have|something you have]], like the authenticator app on your phone."

Todd was quiet for a second. "So what counts as the second thing?"

"[[something_you_have|Something you have]] — phone app, hardware token, security key. Or [[something_you_are|something you are]] — fingerprint, face. Location can be somewhere you are, a context signal, not a substitute for a second factor when policy asks for MFA."

"Password plus PIN was a house rule, then," Todd muttered. "Okay. Enroll me for real."

## Soft tokens, SMS, and the Approve reflex

While Todd got his phone out, two other sales reps stopped by my desk to get their authenticator apps set up.

I started with the authenticator app. The soft path is a soft token on the phone that shows [[totp|TOTP]] codes — six digits, thirty seconds, clock-bound. We scanned the QR at his desk, not at the coffee bar. I mentioned shoulder surfing once; he angled the screen.

"What about texts?" Todd asked. "SMS is easier. I do not want another app."

"SMS OTP is still a second factor," I said, "but it is the weaker possession story — SIM swap, intercepted texts. Policy allows it as a backup, not as the primary. App first."

He installed the app. We generated backup codes and he put them in the password manager, not in a Notes file titled codes. Push was next: the IdP offered push notification approve/deny.

Jules walked past with a granola bar. "Tell him about fatigue before he trains his thumb."

"[[mfa_fatigue|MFA fatigue]]," I said. "If you get a push you did not start, tap Deny and call us. Attackers spam Approve until someone gets bored."

Todd nodded like a man who had tapped through terms of service. "Deny if I did not ask."

Across the aisle, Rita from marketing wanted the same enrollment but "without the phone, I lose phones." We issued a loaner hard token for her travel week and scheduled a security key once procurement finished arguing about USB-C.

## Lockout, biometrics, and the laptop that thinks it knows a face

Dev from engineering came to my desk in person, which engineers never do, with his laptop open to an [[account_lockout|account lockout]]. A script had retried a stale secret forty times. He was embarrassed and late for a stand-up.

"I pointed a job at the old service password," Dev said. "It hammered. Now I cannot even get in to fix the hammer."

"Lockout is doing its job," I said. "Failed authentication budget spent. I unlock after we rotate the secret in the vault, not before — otherwise the script just spends the budget again."

He waited on the timer. He did not like waiting. The script stayed stopped until the secret lived in the vault.

While Dev waited, Lila from HR stopped by with a laptop lid.

"Windows Hello says my face," she said. "Is that real [[biometrics|biometrics]], or theater? Also can I turn off MFA if the laptop unlocks me?"

"Biometrics are something you are," I said. "On consumer laptops, it's just a local screen unlock. But on our managed enterprise laptops, Windows Hello for Business pairs your biometric gesture with an asymmetric private key locked inside your laptop's TPM chip. That hardware handshake satisfies MFA at the [[identity_provider|identity provider]] without typing codes. If procurement hasn't enrolled your laptop into Hello for Business yet, you still need the soft token app."

She kept the app. She looked like someone who had hoped for a shorter answer.

## Owen and the door that let two people in

Before the lockouts peaked, Owen came up from facilities with a printout of the badge reader log for the east stairwell door. Owen ran the badge system the way Rosa ran Hank's routes in Gresham: he knew every reader and every lock on the building, and he told me up front that Active Directory was not his department.

"Two entries, one badge, eleven seconds apart," he said, tapping the paper. "Door only logged one swipe. Camera shows two people. Somebody held it."

"Tailgating," I said. I had a card for the word in my drawer.

"Call it what you want. The badge is something you have," Owen said. "The person holding the door just let somebody borrow it." He did not know how to tie the badge system to account lockouts, and neither did I. I added the stairwell door to the lockout ticket anyway, as one more place where proof of who you are had been handed to a stranger, and Owen went to ask the camera which badge it was.

## Who You Are, and Who Signs Off

By mid-morning we had found the machine Dev's script was running from by reading the caller computer name on the lockout events. Dev moved the script's credentials into the secrets vault, we cleared the lockout, and the bad-password counter stayed at zero.

Todd called across the aisle. "Sign in with company worked. Push prompt, two digits, straight into the CRM."

"Two different factor types," I said. "That's the point."

Not everyone liked the fixes. Todd's manager had wanted an exception so the sales team could keep PIN-plus-password logins through quarter-end, and I had said no in writing. She forwarded my reply to Jules with one line: *Is this the tone we want from the desk?*

Jules answered her and copied me. The answer was polite and did not move an inch. Then she walked over to my desk. "You were right and you were curt. Next time, be right and give her a date."

The Tier 2 posting closed two weeks later. I did not get it. Jules told me the panel had read the complaint, and that it was not the only reason, but it was one of them. The posting would reopen in December, and promotions from that round would not land until January. <!-- date-ok: January is when promotions land, a forward reference -->

Owen never did get a clean answer from the camera that day. The footage showed the back of a gray jacket, and he said he would keep pulling badge logs when he had time.

## Practice It in the Lab

```bridge-card
title: Portland Desk Lab: Identity, Authentication Factors, & Password Policy Triage
target: workbench/08-prove-who-you-are.md
domain: CompTIA Security+ SY0-701 • Domain 4.2 & 1.3
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
The lab walks through the incident from this chapter step by step, with the answer shown, and then gives you one new problem that works the same way.
```
