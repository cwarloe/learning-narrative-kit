import os

os.chdir(r"C:\Users\charl\learning-narrative-kit")

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        elif old.replace("\n", "\r\n") in content:
            content = content.replace(old.replace("\n", "\r\n"), new.replace("\n", "\r\n"))
        elif old.replace("\r\n", "\n") in content:
            content = content.replace(old.replace("\r\n", "\n"), new.replace("\r\n", "\n"))
        else:
            print(f"WARNING: substring not found in {path}:\n  {old[:60]}...")
            
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Successfully processed {path}")

# ==============================================================================
# EPISODE 08 NARRATIVE
# ==============================================================================
ep08_narrative_replacements = [
    (
        "It had been raining on the east glass since before I sat down. Jules had already claimed the whiteboard. A bike helmet hung off her monitor arm, and the sticky under *which decision?* now said *which factor?*\n\n\"Cards in the drawer are for ports,\" she said when I reached for a blank one. \"Someone will swear two passwords are multifactor. Talk the habit into a decision.\"\n\nThe first ticket in the help desk queue was already yelling in all caps.",
        "The smell of wet wool and radiator steam filled the fourth floor long before the eight o'clock chime. Across the partition, Jules was running a dry-erase marker down a list of ninety-day password expiration notices that had triggered over the weekend.\n\n\"Two dozen people locked themselves out between Friday night and seven this morning,\" Jules said, capping the blue marker with a sharp snap. \"Half of them will swear up and down that typing a password and a PIN counts as multifactor. Don't argue with their frustration, Ethan. Separate what they know from what they hold.\"\n\nOn the dispatch display, the first incident ticket was already flashing red."
    ),
    (
        '"I already have multifactor," Ken said.',
        '"I already have multifactor," Todd said.'
    ),
    (
        '"A password and a PIN are both [[something_you_know|something you know]], Ken," I said.',
        '"A password and a PIN are both [[something_you_know|something you know]], Todd," I said.'
    ),
    (
        "Ken was quiet for a second.",
        "Todd was quiet for a second."
    ),
    (
        '"Password plus PIN was a house rule, then," he muttered. "Okay. Enroll me for real."',
        '"Password plus PIN was a house rule, then," Todd muttered. "Okay. Enroll me for real."'
    ),
    (
        "While Ken got his phone out, two other sales reps stopped by my desk to get their authenticator apps set up.",
        "While Todd got his phone out, two other sales reps stopped by my desk to get their authenticator apps set up."
    ),
    (
        '"What about texts?" Ken asked.',
        '"What about texts?" Todd asked.'
    ),
    (
        'Ken nodded like a man who had tapped through terms of service.',
        'Todd nodded like a man who had tapped through terms of service.'
    ),
    (
        "Ken is insisting Password plus PIN is multifactor",
        "Todd is insisting Password plus PIN is multifactor"
    )
]

# ==============================================================================
# EPISODE 09 NARRATIVE
# ==============================================================================
ep09_narrative_replacements = [
    (
        "Wednesday started with a subject line in all caps and Jules rewriting the sticky under *which decision?* It now said *who benefits if I hurry?*\n\n\"They are not breaking our crypto,\" she said when I reached for a blank card. \"They are borrowing our manners. Notice which manners got borrowed.\"\n\nThe first ticket in the help desk queue read *URGENT — mailbox locked, verify now.*",
        "Wednesday morning smelled of wet pavement and burnt French roast. I was hanging my rain jacket behind workstation fourteen when Jules spun her chair around to block the aisle.\n\n\"Social engineering isn't about breaking cryptography, Ethan,\" Jules said, her voice cutting through the hum of the HVAC blowers. \"Attackers borrow our manners, our hierarchy, and our panic. Notice which manners got borrowed before you click a single link.\"\n\nThe wallboard chimed: a high-priority ticket flagged *URGENT — mailbox locked, verify now.*"
    ),
    (
        "The tone was HR-casual, which Ken trusts more than HR-formal.",
        "The tone was HR-casual, which Todd trusts more than HR-formal."
    ),
    (
        'Ken muttered, "I almost clicked because it said my teammates already finished."',
        'Todd muttered, "I almost clicked because it said my teammates already finished."'
    ),
    (
        'Pull the raw RFC 5322 MIME headers, trace the originating IP,',
        'Pull the raw email headers, trace the originating IP,'
    )
]

# ==============================================================================
# EPISODE 10 NARRATIVE
# ==============================================================================
ep10_narrative_replacements = [
    (
        "Thursday's first subject line was already in all caps, which at this desk means either a real fire or someone whose standup starts in twelve minutes. Jules had rewritten the sticky under *which decision?* It now said *does this need to leave the network?*\n\n\"Malware is a category,\" she said when I reached for a blank card. \"Your job is the decision — quarantine the file, isolate the box, escalate the weird outbound. Do not negotiate with a padlock, and do not hunt Latin names while the machine is still talking to the floor.\"\n\nI opened the help desk queue.",
        "A fierce October squall was rattling the fourth-floor casement windows when the red beacon on the dispatch board lit up. Jules didn't look up from her terminal, but her knuckles were white on her pen.\n\n\"Malware isn't a theory in a textbook, Ethan,\" Jules said, tracking an alert across the network operations dashboard. \"Your job is containment: quarantine the dropper, isolate the host, and protect the shared drives. Do not hunt Latin names or argue with a ransom note while the box is actively beaconing across the subnet.\"\n\nI clicked into the high-priority queue."
    ),
    (
        "Ken unplugged. He still had a file mid-copy and he said so, twice, because the file was for a client who bills in hours. I told him the copy could wait",
        "Todd unplugged his laptop. He still had a proposal deck mid-copy and he said so, twice, because the deck was for a client whose account was up for renewal. I told him the copy could wait"
    )
]

# ==============================================================================
# EPISODE 11 NARRATIVE
# ==============================================================================
ep11_narrative_replacements = [
    (
        "The first ticket of Friday was *Can't join CorpWifi — worked yesterday — board meeting in 20.* Jules's sticky under *which decision?* said *which SSID am I actually on?*\n\n\"Wired has a cable you can point at,\" she said when I reached for a blank card. \"Wireless has manners and math. Verify the network. Prefer enterprise over café vibes. Escalate anything that looks like a twin.\"\n\nI opened the help desk queue.",
        "Friday morning opened with the whine of the vacuum cleaner in the hallway and Maya Lin already standing at the front counter holding an iPad.\n\n\"Wired connections have physical copper you can trace with your fingers,\" Jules said, stepping out of the server closet with a handheld spectrum analyzer. \"Wireless is invisible friction. Verify the BSSID, enforce 802.1X enterprise authentication over convenience, and treat any sudden open twin as hostile.\"\n\nThe board dinged with Maya's ticket: *Can't join CorpWifi — worked yesterday — executive meeting in 20.*"
    ),
    (
        '"And WEP?" Ken asked.',
        '"And WEP?" Todd asked.'
    ),
    (
        'Ken muttered something about customer politics and connected the VPN on the hotel portal network. He did not join the WEP scanner. He said the warehouse tour would have to live without his laptop.',
        'Todd muttered something about customer politics and connected the VPN on the hotel portal network. He did not join the WEP scanner. He said the customer tour would have to live without his laptop.'
    )
]

# Run narrative updates on both portland-desk and docs/portland-desk
for prefix in ["docs/portland-desk/narrative/", "docs/portland-desk/narrative/"]:
    update_file(prefix + "08-prove-who-you-are.md", ep08_narrative_replacements)
    update_file(prefix + "09-dont-click-that.md", ep09_narrative_replacements)
    update_file(prefix + "10-something-on-the-box.md", ep10_narrative_replacements)
    update_file(prefix + "11-the-air-is-shared.md", ep11_narrative_replacements)

print("All narrative prose updates complete.")
