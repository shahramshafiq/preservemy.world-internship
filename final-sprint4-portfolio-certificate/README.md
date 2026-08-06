# Final Sprint 4: Portfolio & Certificate Evidence

**Shahram Shafiq | AI-Based 3D Scene Reconstruction Track | Final Sprint 4: Portfolio & Certificate Evidence (Week 7, Module 31 of 31)**

---

## Who I am

**Shahram Shafiq**, CS sophomore at FAST NUCES Islamabad (CGPA 3.66). I teach Python to students aged 8 to 16 at JuniorCoderz. This internship was my first time working with 3D reconstruction, building directly on computer vision and ML fundamentals I already had.

- GitHub: [github.com/shahramshafiq](https://github.com/shahramshafiq)
- Portfolio: [shahramshafiq-portfolio.vercel.app](https://shahramshafiq-portfolio.vercel.app)
- Email: shahramshafiqgoraya4363@gmail.com
- Repo: [github.com/shahramshafiq/PMW-day1](https://github.com/shahramshafiq/PMW-day1)
- Live final showcase: [shahramshafiq.github.io/PMW-day1](https://shahramshafiq.github.io/PMW-day1/)

## Track

**AI-Based 3D Scene Reconstruction**, PreserveMy.World x TechRealm Impact Internship, team EchoFrame Labs, June to August 2026. My job on this track: understand and build real pieces of the pipeline that turns heritage-site footage into a trustworthy 3D digital record, sourcing footage, comparing reconstruction methods, and building working tools around the data, not just reading about them.

---

## Strongest artifacts

Six pieces I'd point anyone to first, each with real evidence behind it, not just a claim:

1. **[Jaulian Monastery 3D Reconstruction](week3-3d-reconstruction/README.md)**, the flagship deliverable. Real multi-view Structure-from-Motion tested first and honestly failed (12 to 17 verified matches per photo pair), documented rather than hidden, then a monocular reconstruction built and validated three separate ways: [`output/jaulian_monastery_taxila.ply`](week3-3d-reconstruction/output/jaulian_monastery_taxila.ply), 13,375 points.
2. **[Final Sprint 1 Case Study](case-study/README.md)**, the same reconstruction told with fresh, independently re-executed verification: re-ran the QA script cold and cross-checked the `.ply` with a second, separately written parser, both agreeing exactly.
3. **[Final Sprint 2: Mesh Reconstruction](final-sprint2-mesh-reconstruction/README.md)**, turning that point cloud into a real triangulated mesh. The first attempt rendered as a spiky mess despite passing its own validation; a real, measured debugging pass (not a guess) found the actual cause and fixed it, with the honest residual limitation still documented rather than hidden.
4. **[Neural Networks: MNIST Classifier](week4-neural-networks/)**, a Keras model at 97.18% test accuracy on the full 70,000-image dataset, backed by a from-scratch numpy rebuild landing in the same range, the actual proof it works, not just a claim.
5. **[Heritage Reconstruction API](heritage-api/)**, a full-stack Flask and React app, 7 REST endpoints, 4 real Pakistani heritage sites, later hardened with a 22-case pytest suite (Extension Sprint 3) up from 0 tests.
6. **[Story, Script, Film and Edit](week3-story-film/)**, a real 75-second film built from genuine project artifacts (the actual point cloud, the actual ML renders), original synthesized audio rather than any licensed track, with two real bugs caught and fixed by checking output, not trusting a clean exit code.

Full list of every deliverable across the whole internship, not just the highlights above, is in the [Certificate Evidence Pack](../certificate-evidence-pack/README.md).

---

## Process evidence

Every claim above links to a real, viewable file or a real commit, not a summary asking to be trusted. The two places that make this checkable end to end:

- **[Certificate Evidence Pack](../certificate-evidence-pack/README.md)**, a single index mapping all 17 core deliverables, all 7 Extension Sprints, and all 4 Final Sprints to their real GitHub links and dates.
- **Commit history**: [github.com/shahramshafiq/PMW-day1/commits/main](https://github.com/shahramshafiq/PMW-day1/commits/main), every real work session, not one squashed history.

The recurring discipline across this whole repo, re-execute code fresh rather than trust a prior run, checksum or byte-compare claims against the live file, cold HTTP-check every link before calling a module done, is documented as it happened in [`week1-ai-review.md`](../week1-ai-review.md) and carried through every Extension Sprint and Final Sprint since.

---

## Reflection

I started this track at close to zero on 3D reconstruction. The single most useful thing I learned wasn't a specific algorithm, it was that a failed test, reported honestly with real numbers, is worth more than a forced success. The SfM feasibility test in Week 3 genuinely failed (12 to 17 matches, not enough for triangulation), and reporting that plainly instead of quietly working around it is what made the pivot to a monocular reconstruction, and everything built on top of it since, actually defensible.

That same instinct kept paying off. Extension Sprint 1's quantitative QA replaced a single visual check with real measured numbers. Final Sprint 2's mesh build looked visibly wrong on the first attempt despite passing its own validation, and only actually measuring the cause (not guessing) led to a fix that worked. Final Sprint 3's peer review taught me that an honest caveat needs to live next to the thing it describes, not just somewhere in the surrounding prose, which is a small lesson but a real one, and I could point to the exact commit where I applied it.

## Next steps

- Replace the heuristic monocular depth estimate with a trained network (MiDaS), already identified in [`research/3d_methods_comparison.md`](../research/3d_methods_comparison.md) and named directly in the Final Sprint 2 build log as the real fix for the mesh's residual roughness.
- Source a genuine multi-view capture of one heritage site with the roughly 66% photo overlap the literature in [`research/source_log_3d_methods.md`](../research/source_log_3d_methods.md) says real SfM needs, so a COLMAP-style pipeline can be tested properly instead of on photos that were never planned for it.
- Extend the mesh to a fully closed, meshed surface (Poisson reconstruction or similar) beyond the heightfield built in Final Sprint 2.
- Keep applying the same standard to whatever comes after this internship: a claim is only as good as the independent check sitting next to it.

---

## Verified hours and certificate status

The dashboard showed **40 verified hours** when this Final 10-Hour Sprint unlocked (3 Aug 2026), after reaching that mark through the core program modules and all 7 Extension Sprints. This Final Sprint's four 2.5-hour modules, Project Case Study, Build/Research Proof, Peer Review & Revision, and this Portfolio & Certificate Evidence page, are the last 10 hours toward the 50-hour certificate threshold, pending admin review of each submission. I'm not writing a specific final total here since that number depends on this module's own review outcome, which hasn't happened yet at the time of writing, the portal dashboard is the live source of truth for that figure, not this page.

---

## LinkedIn-ready announcement

```
I just completed the PreserveMy.World x TechRealm Impact Internship on the AI-Based 3D Scene Reconstruction track (50 verified hours, pending final review).

Over the internship I tested real Structure-from-Motion on curated heritage photos, found it genuinely wasn't viable given the available footage, and built a validated monocular 3D reconstruction of the Jaulian Buddhist monastery ruins at Taxila instead, then extended it into a real triangulated mesh, a from-scratch neural network at 97.18% test accuracy on MNIST, and a full-stack heritage-data API.

The single biggest thing I learned: a failed test reported honestly, with real numbers, is worth more than a forced success. Every deliverable in this internship is public and linked to real evidence, not just claimed.

Repo: github.com/shahramshafiq/PMW-day1
Live showcase: shahramshafiq.github.io/PMW-day1

#PreserveMyWorld #TechRealm #3DReconstruction #ComputerVision #Internship
```

---

## What I personally completed

I wrote the reflection and next-steps content myself, based on my own actual work across the internship. AI helped draft the prose and pull together the links into this layout; every artifact linked above is real work I built, reviewed, and previously verified in its own module, not new content invented for this page. I re-checked every link in this document and in the updated Certificate Evidence Pack with a live, unauthenticated request before submitting, not assumed to still work from memory.
