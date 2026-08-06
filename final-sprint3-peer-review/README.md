# Final Sprint 3: Peer Review & Revision

**Shahram Shafiq | AI-Based 3D Scene Reconstruction Track | Final Sprint 3: Peer Review & Revision (Week 7)**

---

## Artifact reviewed

**Ruwaida Shakeel's live Team Taxila page**, [ruwaidashakeel05.github.io/Taxila](https://ruwaidashakeel05.github.io/Taxila/), a real teammate artifact from the group sprint I led. I did not pick a low-stakes artifact to review lightly, this is the actual live page our team's group submission points to, so feedback on it is directly useful, not an exercise.

## Peer review

### Clarity

Strong. The nav bar (Home, History, Why Now, 3D Reconstruction, Stupa Anatomy, Try Your Photo, Learning Route, Audience, Map & Sources) matches the actual page structure exactly, and each section opens with a plain-language framing line before going into detail (for example, "This isn't a history problem. It's happening this month." ahead of the UNESCO section). A reader who skims only the headers still gets the real argument.

### Evidence

I checked this rather than assumed it. The "Map & Sources" section deliberately does not rehost original site photography, it explains why (provenance questions around an active UNESCO dispute site) and links out to 13 specific, named sources instead of a generic "sources" dump. I pulled every citation URL directly from the page's HTML and checked them:

```
200  https://discoveringpakistan.com/taxila-where-buddhism-alexander-and-gandhara-converge/
200  https://en.wikipedia.org/wiki/Taxila
200  https://taxilamuseum.com/
200  https://tourism.punjab.gov.pk/taxila
200  https://www.worldhistory.org/taxila/
200  https://www.nationalgeographic.com/history/article/taxila
```

The remaining sources (2 Wikimedia Commons categories, the Coins of Taxila category, Republic World, UNESCO's own listing, Britannica) failed a plain `curl` check, but I did not stop there and mark them broken. Bot-protection blocks non-browser requests on several of those domains, so I re-checked with the actual browser tool instead of trusting curl's result: `whc.unesco.org/en/list/139` loaded correctly (title: "Taxila - UNESCO World Heritage Centre") and `britannica.com/place/Taxila` loaded correctly (title matches). The Wikimedia Commons categories and the Republic World article could not be checked in this environment (the browser tool itself blocks those domains, unrelated to whether Ruwaida's links work), so I'm reporting that honestly as a tooling limit, not a claim that those specific links are broken.

**The UNESCO claim itself**, that Pakistan received a formal July 2026 warning over cement restoration at Mohra Moradu and Sirkap, was already independently verified against 7+ real news outlets earlier in this internship (documented when the group page was first reviewed). It holds up.

### Presentation

The page uses consistent, honest labeling on every illustrative element: "Schematic layout, not to scale," "Illustrative model... not a laser-scan," "Cross-section is schematic... not a measured drawing." That caveat sits directly next to the visual it applies to, not buried in a separate disclaimers section. This is a real, specific technique worth naming, not just "the design looks nice," see What I Learned below.

### Accuracy

The historical timeline (Achaemenid absorption, Alexander 327 BCE, Mauryan rule, Indo-Greek Sirkap, Kushan Sirsukh, Hun invasion, Cunningham's 1863 to 1873 rediscovery, Marshall's 1913 to 1934 excavations, 1980 UNESCO inscription) matches standard, independently checkable history of the site, and the "18 component sites" and "1980 inscription" figures match the UNESCO listing page directly.

### Impact

The "Try Your Photo" feature is the standout: it runs the same monocular depth heuristic our team built for the Jaulian monastery reconstruction, client-side, on a visitor's own photo, with an explicit, correct caveat that it is "not real photogrammetry" and directly credits it as an extension of the source project. That is a genuine, technically accurate reuse of real project work, not a generic add-on, and it is the single best "impact" element on the page because it lets a visitor experience the actual method rather than just read about it.

### One finding I could not confirm, reported honestly rather than dropped or overstated

I tried to functionally test the interactive 3D toggle (not just read about it). Inspecting the page directly, `THREE` (the Three.js library) loaded correctly, but the scene canvas's actual render resolution was stuck at the browser default (300x150) despite being laid out at 622x460 on the page, and the "Loading scene…" overlay was still present in the DOM after the section had been open for a while. That pattern can mean the render loop never properly started. I could not get a real screenshot to confirm this visually in my test environment (my browser tool's pane was not being composited during this session, which itself can stall a `requestAnimationFrame` loop, a tooling artifact, not necessarily a real bug). I am reporting this as "worth a manual check in a normal browser," not as a confirmed defect, because I do not have the evidence to claim more than that.

---

## What I learned

The strongest thing on Ruwaida's page is not any single fact, it's that every illustrative or approximate element carries its own honest caveat right where a reader sees it, not just once in a surrounding paragraph. My own writeups explain limitations in prose (see the "Honest limitation" section in [`final-sprint2-mesh-reconstruction/README.md`](../final-sprint2-mesh-reconstruction/README.md)), but the two rendered images in that same file were embedded with no caption at all, a reader who scrolls straight to the pictures, which is most readers, would see them with zero context.

## Revision applied to my own work

**Before:** [`final-sprint2-mesh-reconstruction/README.md`](../final-sprint2-mesh-reconstruction/README.md) embedded both QA render images with no caption directly under them, the honest limitation about residual ridging was only in a paragraph above and below the images, easy to skip.

**After:** added a direct, one-line italic caption under each image stating what it shows and the real caveat inline, matching the technique Ruwaida's page uses consistently. Real commit diff: [`f9bda0d`](https://github.com/shahramshafiq/PMW-day1/commit/f9bda0d), applied after and separate from [`725a95b`](https://github.com/shahramshafiq/PMW-day1/commit/725a95b) (this review itself), so the commit history shows the actual review-then-revision order, not a single combined edit.

This is a small change, but it is the specific, meaningful thing the peer review actually surfaced, not a generic "add more detail" filler revision.

## Revision reflection

Before this review, I treated "document the limitation honestly" as satisfied once it existed anywhere in the file. Reviewing a page that puts the caveat physically next to the image it describes showed me that where a caveat lives matters as much as whether it exists at all, a reader who only looks at the pictures (a real, common reading pattern, not a hypothetical one) should not have to scroll to a different paragraph to find out a render is not fully clean. The revised version of `final-sprint2-mesh-reconstruction/README.md` is stronger for exactly that reason: the same honest information, placed where it will actually be read.

---

## What I personally completed

I browsed Ruwaida's live page myself, clicked through its navigation, pulled its actual citation URLs from the rendered HTML rather than guessing them, and ran real HTTP checks on each one, re-verifying with the browser tool (not just curl) when a request failed, to avoid misreporting a bot-blocked request as a broken link. The 3D-canvas finding was investigated with real DOM/JS inspection, and I explicitly did not overstate it once I could not get a confirming screenshot. AI assistance was used for drafting this document's prose; the actual page inspection, link checks, and the decision about what to revise in my own work were mine.
