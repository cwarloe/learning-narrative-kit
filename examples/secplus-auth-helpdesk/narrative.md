# Portland Desk — Prove Who You Are

*A Security+ identity-and-authentication precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Tuesday rain again. East-side glass, same opinions. I am Ethan, still week-something at the [[help_desk|help desk]], and today the queue is not ports — it is people proving they are who they say they are.

Jules has already claimed the whiteboard. Bike helmet on the monitor arm. One sticky under *which decision?* now says *which factor?* She is not running a class. She is running a shift.

"Cards in the drawer are for ports," she says when I reach for a blank one. "Identity is habits. Someone will swear two passwords are multifactor. Your job is to talk the habit into a decision."

I open the queue. Coffee. Portland doing Portland. The first [[ticket|ticket]] is already yelling in all caps.

## Nora and the policy that keeps changing the locks

Nora in finance cannot reset. She has tried her old favorite three times. The portal says no.

"I always rotate the season and the year," she says on the phone. "Spring2024!, Summer2024! — that used to work everywhere. Now it hates me. Also it wants sixteen characters. Who remembers sixteen?"

I pull the account. [[password_age|Password age]] is ninety-one days. Policy max is ninety. Her last change slid under the wire last quarter; today the portal is enforcing [[password_expiration|password expiration]] before it will talk about a reset path.

"Expiration is why I'm calling," Nora says. "Every ninety days I invent a worse password and write it on a sticky. My cousin's home lab uses a [[passphrase|passphrase]] — four words, no sticky. Is that allowed, or do we still need the symbol salad?"

Jules leans in just enough to be heard. "Ask what we are optimizing for."

"[[password_length|Length]] and uniqueness," I say. "[[password_complexity|Complexity]] rules still exist here — upper, lower, digit, symbol — but a long passphrase that clears length usually beats a short spicy one. And no [[password_reuse|password reuse]] across work and the streaming account you use at lunch. That Spring2024 pattern is reuse with a costume."

Nora snorts. "Costume. Fine. What do I type?"

We walk a passphrase she will actually remember, not a movie quote she has posted on socials. I remind her the company [[password_manager|password manager]] will store a unique [[password|password]] for every app so she is not inventing seasons. She groans about another vault, then admits her browser already offered to save three variants of the same secret.

"Manager wins," she says. "Sticky loses." Ticket note: length + uniqueness, not theater.

## Ken and the MFA that is not MFA

Next up: Ken in sales. Locked out of the CRM after a phone wipe. He wants a quick fix.

"I already have multifactor," Ken says. "[[password|Password]] plus a [[pin|PIN]] on the laptop. Two things. That is MFA, right? My old shop said so."

I feel the flashcard reflex and almost agree because the sentence has two nouns.

Jules's sticky is visible from my chair. *which factor?*

"[[identification|Identification]] is you typing your username," I say slowly. "[[authentication|Authentication]] is proving it. MFA means two different factor *types*. Password is [[something_you_know|something you know]]. PIN is also something you know. Same bucket. That is [[single_factor|single-factor]] with extra typing — not [[mfa|multifactor authentication]]."

Ken is quiet for a second. "So what counts as the second thing?"

"[[something_you_have|Something you have]] — phone app, hardware token, security key. Or [[something_you_are|something you are]] — fingerprint, face. Location can be [[somewhere_you_are|somewhere you are]], a context signal, not a substitute for a second factor when policy asks for MFA."

"Password plus PIN was a house rule, then," he mutters. "Not a definition. Okay. Enroll me for real."

## Soft tokens, SMS, and the Approve reflex

Enrollment [[ticket|ticket]] for Ken turns into a hallway class for two other people who "just need the code thing."

I start with the [[authenticator_app|authenticator app]]. Soft path: a [[soft_token|soft token]] on the phone that shows [[totp|TOTP]] codes — six digits, thirty seconds, clock-bound. We scan the QR at his desk, not at the coffee bar. I mention [[shoulder_surfing|shoulder surfing]] once; he angles the screen like he is hiding a high score.

"What about texts?" Ken asks. "SMS is easier. I do not want another app."

"[[sms_otp|SMS OTP]] is still a second factor," I say, "but it is the weaker possession story — SIM swap, intercepted texts. Policy allows it as a backup, not as the primary. App first."

He installs the app. We generate [[backup_codes|backup codes]] and he puts them in the password manager, not in a Notes file titled codes. Push is next: the IdP offers [[push_notification|push notification]] approve/deny.

Jules walks past with a granola bar. "Tell him about fatigue before he trains his thumb."

"[[mfa_fatigue|MFA fatigue]]," I say. "If you get a push you did not start, tap Deny and call us. Attackers spam Approve until someone gets bored. Convenience is not a personality trait; it is a habit someone else can use."

Ken nods like a man who has tapped through terms of service. "Deny if I did not ask. Got it."

Across the aisle, Rita from marketing wants the same enrollment but "without the phone, I lose phones." We issue a loaner [[hard_token|hard token]] for her travel week and schedule a [[security_key|security key]] once procurement finishes arguing about USB-C. Hardware when soft will not stick.

## Lockout, biometrics, and the laptop that thinks it knows a face

Mid-morning: Dev from engineering, [[account_lockout|account lockout]] after a script retried a stale secret forty times. He is embarrassed and late for a stand-up.

"I pointed a job at the old service password," Dev says. "It hammered. Now I cannot even get in to fix the hammer."

"Lockout is doing its job," I say. "Failed [[authentication|authentication]] budget spent. I unlock after we rotate the secret in the vault, not before — otherwise the script just spends the budget again."

While Dev waits on the unlock timer, Lila from HR stops by with a laptop lid and a face.

"Windows Hello says my face," she says. "Is that real [[biometrics|biometrics]], or theater? Also can I turn off MFA if the laptop unlocks me?"

"Biometrics are [[something_you_are|something you are]]," I say. "Fine for device unlock. Company apps still want MFA at the [[identity_provider|identity provider]]. Unlocking the lid is not the same as proving you to every SaaS tile."

She looks relieved. "So I keep the app. Face is just the door, not the whole building."

## Offboarding leftovers and the admin sticky

Afternoon starts with HR pinging [[offboarding|offboarding]] for a contractor who left Friday. Badge returned. Laptop wiped. Access… not so much.

Jordan from IT ops shares screen. The contractor still has a license on the design tool, a shared mailbox membership, and — Jules makes a noise — a line in a wiki with a [[shared_admin_account|shared admin account]] password last rotated "sometime before the rebrand."

"That is not a password," Jules says. "That is a campfire story."

We treat it as a [[deprovisioning|deprovisioning]] failure, not a trivia moment. Disable the cloud login. Pull group memberships. Kill the API token someone minted "temporarily" in March. For the shared admin: move the secret into [[vaulting|vaulting]], rotate it, and stop pretending six people can share one identity and still have [[accounting|accounting]] that means anything.

"[[provisioning|Provisioning]] was fine on day one," Jordan says. "We created the account, put them in the contractor role, shipped the laptop. Day last is where we get sloppy."

"[[least_privilege|Least privilege]] on the way in," Jules says. "Least leftover on the way out. Same muscle."

I open a follow-up [[ticket|ticket]] to map the contractor role in [[rbac|RBAC]] so the next person inherits a bundle we can revoke in one motion — not a scavenger hunt across five admin consoles.

## Privileged shortcuts and break-glass myths

Network drops into the same thread. Jared — still proud of last week's SSH rewrite — wants a standing domain admin for "closet emergencies."

"I have a Pi at home that is basically god mode," he says. "At work I still type a normal user password and wait. If the [[identity_provider|IdP]] hiccups, how do we get in?"

"[[privileged_access|Privileged access]] is not a lifestyle," Jules says. "It is a checkout."

We walk the desk-level [[pam|PAM]] story without turning it into a product pitch: vault the break-glass path, do not laminate it. [[break_glass|Break-glass]] exists for when MFA and IdP paths are actually down — sealed, monitored, painful on purpose. Day to day, Jared requests [[just_in_time|just-in-time]] elevation for the change window, does the work, loses the rights when the window closes. [[authorization|Authorization]] for admin actions should not be a permanent personality trait on his account.

Jared sighs. "Fine. Checkout beats sticky. I will stop naming shared accounts after the street food cart."

## SSO ticket: the app that wants its own password

Late afternoon. Vendor portal for facilities. Ticket title: *need password for EnergyDash*. Description: *IT please create a login.*

I call. Dana — same truck energy as the FTP week — is between buildings.

"The portal has a Sign in with company button," Dana says. "Also a Register. Register asked me for a new password. I made one. Now Finance says that is wrong."

"[[sso|SSO]]," I say. "We do not want a snowflake password in EnergyDash if we can help it. Our [[identity_provider|IdP]] already authenticated you this morning. The portal should trust a federation assertion, not a new local account."

"They said SAML on the implementation call," Dana offers. "Or OAuth. They used both words like synonyms."

Jules, without looking up: "Desk translation, Ethan."

"[[federation|Federation]] means their app trusts our IdP. [[saml|SAML]] is the enterprise assertion pattern you will see on the wiki checklist. [[oauth|OAuth]] shows up when an app wants a token to call an API without eating your password — related paperwork, different shape. For this [[ticket|ticket]], click Sign in with company, refuse Register, and if Register is the only path, we escalate — local passwords in vendor tools become [[password_reuse|reuse]] magnets and offboarding blind spots."

Dana taps something. "Sign in with company worked. It bounced me through the usual MFA push. I denied the first one because I forgot I had started it. Then I approved the second. That fatigue talk is going to live in my head now."

"Good," I say. "Keep the local register button unemployed."

## Passwordless rumor and the end of the shift

Last ping is not a fire. It is a rumor. Someone in Slack asks when we go [[passwordless|passwordless]] so they can throw their password manager into the river.

Jules types one line: *security keys and device-bound passkeys are on the roadmap; throwing secrets into the river is not a migration plan.*

I add the desk version for the person who will still call: passwordless replaces the knowledge factor with possession and biometrics wired through the IdP — it does not mean no proof. Until then, unique passwords in the manager, MFA that is actually multifactor, and no PIN cosplay.

5:35. Queue noise. Rain louder. I close the last note: Ken enrolled, Nora passphrase, contractor deprovisioned, EnergyDash on SSO, Jared denied standing god mode.

Jules clips her bike lights on. "How many definitions did you memorize?"

"None," I say. "I collected a few bad habits and made a few swaps — factors, not nouns."

She almost smiles. "Good. Tomorrow someone will call password-plus-PIN multifactor again. You already have the line."

I badge into the rain and walk toward the MAX. Portland is still raining. The cards in my drawer are still about ports. Today's decisions were about proof — who you claim to be, how you show it, and what we revoke when the story ends.
