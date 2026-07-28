# Week 1 AI Review and Prompt Engineering

**Shahram Shafiq | AI-Based 3D Reconstruction Track | Module 7 (w1d4), revised in Extension Sprint 4**

---

## Revision note (Extension Sprint 4: Review & Revision)

**Old version** (before this revision): [github.com/shahramshafiq/PMW-day1/blob/18dd2f1/week1-ai-review.md](https://github.com/shahramshafiq/PMW-day1/blob/18dd2f15b79c3a49659b40e67868416a9129653d/week1-ai-review.md)
**Revised version**: this file, on `main`
**What changed:** Steps 1 to 5 below are the untouched original review. Steps 6 to 8 are new: a rubric-based review of the original findings against the general judging rubric (clarity, evidence, technical depth, communication, mission fit, accessibility), a real discovery that one of the original findings had quietly recurred, the actual fix, and fresh verification.
**What I learned from the revision:** catching a problem once and fixing it does not mean it stays fixed. The exact same failure mode (a stale root README) came back on its own as the repo grew, because updating the README was never made a habit, just a one-time cleanup. See Step 8 for the actual lesson going forward.

---

## Step 1: What I collected

- GitHub repo: [github.com/shahramshafiq/PMW-day1](https://github.com/shahramshafiq/PMW-day1)
- Branches: `main`, `day2-research` (PR #1, opened but not merged)
- Portfolio: [shahramshafiq-portfolio.vercel.app](https://shahramshafiq-portfolio.vercel.app)
- README.md, blog post draft, 3D learning scripts, research folder, youthxAI notebook, heritage-api app

---

## Step 2: Strict AI audit

**Prompt used (Strict weekly audit, adapted with real links):**

> Act as a strict PMW program reviewer. Review our Week 1 work: github.com/shahramshafiq/PMW-day1 (main and day2-research branches), portfolio at shahramshafiq-portfolio.vercel.app. Score branding, GitHub setup, clarity, consistency, and mission fit. Give the top 5 fixes ranked by impact.

**Findings, ranked by impact:**

1. **PR #1 was open but never merged.** The `day2-research` branch had the entire Day 2 deliverable: the methods comparison research, the depth simulation script, and the youthxAI Colab notebook. None of it was visible to anyone looking at the default `main` branch, which is what a reviewer sees first. This was the single highest-impact problem: real work existed but was not reachable.
2. **README.md was frozen at "Day 1 complete."** It never got updated to reflect Day 2, the Custom Assignment (heritage-api), or the youthxAI notebook, even though all three existed in the repo or on a branch. A reviewer reading top to bottom would think Week 1 stopped after Day 1.
3. **No team identity anywhere in the repo.** The team (EchoFrame Labs) branding work was submitted separately by a teammate, but this personal repo, README, and portfolio never referenced the team name or tagline. Since "Team branding and GitHub workflow are ready for Week 2 work" is a stated grading criterion, this was a real gap.
4. **Leftover AI-tool misattribution and em dashes in the unmerged branch.** The day2-research README section said "AI coding tool used: Claude Code," which is not how I attribute tool usage in this repo (I use Cursor as the listed assistant, consistent with the rest of my commits). Several files also had em dashes I do not normally use.
5. **heritage-api was buried.** It existed as a folder with its own README, but the top-level repo README never linked to it, so a reviewer skimming the root README would not know it was there.

---

## Step 3: The one real improvement

I did not just write "I should merge the branch." I actually did it:

- Ran a merge-tree dry run first to confirm no conflicts (`git merge-tree`)
- Merged `day2-research` into `main` (commit `278a7ed`)
- Rewrote README.md top to bottom to cover the actual full scope of Week 1: portfolio, 3D learning, research comparison, youthxAI notebook, and heritage-api, with a real file tree and working links to each
- Fixed the AI-tool line and em dashes that got pulled in from the unmerged branch
- Pushed to `main` (commit `fbc791f`)
- Confirmed PR #1 auto-closed as merged via the GitHub API (`"state": "closed", "merged": true`)

This is a visible, verifiable second version: anyone opening the repo today sees Day 2 research, the youthxAI notebook, and the heritage-api demo, all linked from one README, none of which was true before this review.

---

## Step 4: Verification I did manually

Using the verification-checklist prompt style, before treating this as done I manually checked:

- **Functional:** re-ran `git log --all --graph` and the GitHub PR API to confirm the merge actually landed and PR #1 shows `merged: true`, not just `closed`
- **Design/consistency:** grepped the entire repo for em dash characters after the merge and found three leftover instances in files I did not originally write (day2-research branch content); fixed all three
- **Spelling and tone:** read the full rewritten README myself, not just the diff, to confirm it still sounds like me and not like generic AI output
- **Originality:** confirmed the merge added real content (research doc, depth script, notebook), not filler
- **Security/scope:** confirmed the merge touched only markdown, a Python script, an image, and a notebook, nothing that could break the running heritage-api Flask app

---

## Step 5: Reflection on prompting

**What worked:** asking for a "strict" review by role (program reviewer) instead of a generic "how does this look" produced concrete, ranked findings instead of vague encouragement. Naming the exact grading criteria in the prompt (branding, GitHub setup, mission fit) meant the findings mapped directly onto what actually gets scored.

**What failed on the first pass:** a softer version of the review prompt (just "check my repo") only surfaced surface-level suggestions like "add more comments." It took explicitly asking for ranked, high-impact issues before the actual structural problem (the unmerged PR) came up as the top finding.

**What I verified manually, not just trusted:** the claim that the merge "worked." I did not just read a success message; I checked the GitHub API directly for PR #1's real merge status and grepped the whole repo for the em dashes and AI-tool line myself, because those are the two mistakes I have made before in this repo and did not want to repeat silently.

**What I will do differently next week:** check GitHub branch and PR state as a first step before starting new work, not as an afterthought. A branch sitting unmerged for a week is an easy thing to miss if I only look at my local `main`.

---

## Step 6 (Extension Sprint 4): rubric review of the original 5 findings

Reviewed each original finding against the general judging rubric dimensions this sprint asks for: clarity, evidence, technical depth, communication, mission fit, and accessibility. Checked each one against the actual current state of the repo, not assumed still true or still false.

| # | Original finding | Status now, checked directly |
|---|---|---|
| 1 | PR #1 unmerged | Still fixed. `state: closed, merged: true` confirmed again via the GitHub API today (Step 8). |
| 2 | README frozen at "Day 1 complete" | **Recurred.** Fixed at the time, but by today the same README had gone stale again, missing everything from Week 4 onward. See below, this is the real finding of this revision. |
| 3 | No team identity anywhere in the repo | Fixed, and it stuck. The current README's opening line names "team EchoFrame Labs" and its tagline directly (verified by grep, Step 8). |
| 4 | Leftover AI-tool misattribution and em dashes | Still fixed, no recurrence found in a fresh grep across the whole repo (Step 8). |
| 5 | heritage-api buried, not linked from root README | Still fixed, still linked (verified by grep, Step 8). |

**Weakness in the original review, judged by this rubric:** it had strong technical depth and evidence (finding 1 in particular, with real git and API verification) but weak accessibility follow-through. The review fixed things once and never checked whether they stayed fixed. A rubric review is supposed to catch exactly this kind of gap, and it did.

---

## Step 7: the recurred problem, found and fixed

Before assuming finding #2 was still resolved, checked it directly by grepping the current root README for every major deliverable added since Week 1:

```
heritage-api: 5 matches
week4-neural-networks: 0 matches
week4-home-story: 0 matches
week4-video-qa-followup: 0 matches
source_log_3d_methods: 0 matches
iris-hacks: 0 matches
shahramshafiq.github.io: 0 matches
```

`heritage-api` was still linked, everything from Week 4 onward, including the live final showcase site at `shahramshafiq.github.io/PMW-day1`, the actual capstone deliverable, was completely absent. This is the exact same failure mode as the original finding #2, a README that stopped reflecting the real repo, just recurred later instead of being a one-time problem.

**The fix:** updated `README.md` directly, not a separate document: added the live showcase link near the top, updated the file tree to include every folder added since Week 3 (`week4-neural-networks/`, `week4-home-story/`, `week4-video-qa-followup/`, `research/source_log_3d_methods.md`, `heritage-api/tests/`, `iris-hacks-interest/`, `index.html`), and wrote full narrative sections for the neural network, the storytelling film, the QA follow-up, all four extension sprints, and Iris Hacks IV, matching the style of the existing sections rather than a bare list.

---

## Step 8: verification

Checked, not assumed:

- Re-ran the same grep check after the fix: all 7 terms now return real matches, including `shahramshafiq.github.io`.
- Checked every internal markdown link in the revised README against the actual filesystem (`os.path.exists` on all 24 relative links), all resolve.
- Re-confirmed finding #1 is still true today, not just at the time of the original review: `curl` to the GitHub API for PR #1 still returns `state: closed, merged: true`.
- Re-confirmed the portfolio link (`shahramshafiq-portfolio.vercel.app`) and the main GitHub repo both return HTTP 200 today.
- Re-confirmed finding #3 (team identity) by grep, not memory: `EchoFrame` appears twice in the current README, both genuinely in context, not just a stray mention.

**The actual lesson from this revision, not the same one from Step 5:** verifying a fix once, at the time you make it, is not the same as the fix holding up. The original review already knew to check things directly instead of trusting a clean result, that part worked. What it did not do was set up any way to notice if a fixed problem quietly came back weeks later. Going forward, a stale-README check belongs in the same category as the clock-in habit from the original Step 5, something to do as a matter of routine, not something to fix once and consider closed.
