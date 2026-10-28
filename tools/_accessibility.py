"""Accessibility assertions shared by the interactive browser checks.

These verify browser semantics and computed styles, not spoken screen-reader output.
"""

from playwright.sync_api import expect


def check_focus(control):
    # Establish keyboard modality before moving focus to the control under test.
    control.page.keyboard.press("Tab")
    control.focus()
    expect(control).to_be_focused()
    assert control.evaluate("""e => {
        const s = getComputedStyle(e);
        return e.matches(':focus-visible') &&
          ((s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) >= 2) || s.boxShadow !== 'none');
    }"""), "Missing keyboard focus indicator"


def check_deck_accessibility(deck):
    expect(deck).to_have_role("region")
    check_focus(deck)
    expect(deck.locator("[role=status]")).to_be_empty()
    expect(deck.locator("[role=status]")).to_have_attribute("aria-atomic", "true")
    expect(deck.locator("[data-act=flip]")).to_have_attribute("aria-pressed", "false")
    # Keyboard-only flipping must announce the answer and expose only its face.
    deck.press("Enter")
    expect(deck.locator("[data-act=flip]")).to_have_attribute("aria-pressed", "true")
    answer = deck.locator(".lnk-deck__a").text_content()
    expect(deck.locator("[role=status]")).to_contain_text(answer)
    expect(deck.locator(".lnk-deck__face--front")).to_have_attribute(
        "aria-hidden", "true"
    )
    expect(deck.locator(".lnk-deck__face--back")).to_have_attribute(
        "aria-hidden", "false"
    )
    deck.press("Enter")
    expect(deck.locator("[data-act=flip]")).to_have_attribute("aria-pressed", "false")
    # Tab must reach the native navigation buttons, rather than an inactive face.
    deck.press("Tab")
    expect(deck.locator("[data-act=prev]")).to_be_focused()
    check_focus(deck.locator("[data-act=flip]"))


def check_deck_contrast(deck):
    # Badge/counter sit on the dark deck; card tags use the current band background.
    # Check every band's tag as the existing test cycles through all of its cards.
    assert deck.evaluate("""e => {
        const rgb = s => s.match(/[\\d.]+/g).slice(0, 3).map(Number);
        const lum = c => c.map(v => v/255).map(v => v <= .04045 ? v/12.92 : ((v+.055)/1.055)**2.4)
            .reduce((sum,v,i) => sum + v*[.2126,.7152,.0722][i], 0);
        const ratio = (a,b) => (Math.max(lum(a),lum(b))+.05)/(Math.min(lum(a),lum(b))+.05);
        const deckStyle = getComputedStyle(e), background = rgb(deckStyle.backgroundColor);
        // Composite the translucent deck background over the unit surface.
        const alpha = Number(deckStyle.backgroundColor.match(/[\\d.]+/g)[3] ?? 1);
        let parent = e.parentElement;
        while (parent && getComputedStyle(parent).backgroundColor === 'rgba(0, 0, 0, 0)') parent = parent.parentElement;
        const under = parent ? rgb(getComputedStyle(parent).backgroundColor) : [255,255,255];
        const composite = background.map((v,i) => v*alpha + under[i]*(1-alpha));
        for (const el of e.querySelectorAll('.lnk-deck__badge, .lnk-deck__counter')) {
            if (ratio(rgb(getComputedStyle(el).color),composite) < 4.5) return false;
        }
        const count = JSON.parse(decodeURIComponent(e.dataset.deck)).cards.length;
        for (let i=0; i<count; i++) {
            for (const tag of e.querySelectorAll('.lnk-deck__tag')) {
                const style=getComputedStyle(tag);
                if (ratio(rgb(style.color),rgb(style.backgroundColor)) < 4.5) return false;
            }
            e.querySelector('[data-act=next]').click();
        }
        return true;
    }"""), "Flashcard text contrast is below 4.5:1"
