# PreserveMy.World x TechRealm Internship: AI-Based 3D Scene Reconstruction

**Shahram Shafiq | Certificate ID TRN-58990 | Issued August 28, 2026**

---

## The short version

Between June and August 2026 I did a real internship on PreserveMy.World's AI-Based 3D Scene Reconstruction track: a non-profit that uses AI, 3D capture, photography, and storytelling to digitally preserve cultural heritage sites before they're lost. This repo is the actual record of that work, not a highlight reel. It has a real Structure-from-Motion test that failed and why, a monocular 3D reconstruction I validated three separate ways, a mesh-building bug I spent real time debugging instead of hiding, a from-scratch neural network checked against Keras, a full-stack web app, two short films, a group heritage-preservation page I led a team on, and every honest limitation I found along the way written down instead of quietly fixed and forgotten.

**Live final showcase:** [shahramshafiq.github.io/preservemy.world-internship](https://shahramshafiq.github.io/preservemy.world-internship/), one page tying together everything below.

---

## About me

**Shahram Shafiq**, CS sophomore at FAST NUCES Islamabad (CGPA 3.66). I teach Python to school students aged 8 to 16 at JuniorCoderz. Before this internship I'd built multi-agent AI systems, custom data structures in C++, and a full Hotel Management system in JavaFX, but 3D reconstruction was new territory. It turned out to connect directly to computer vision and ML fundamentals I already had, which is most of why the pivot in Week 3 (below) worked at all.

- GitHub: [github.com/shahramshafiq](https://github.com/shahramshafiq)
- LinkedIn: [linkedin.com/in/shahramshafiq](https://linkedin.com/in/shahramshafiq)
- Email: shahramshafiqgoraya4363@gmail.com
- Portfolio: [shahramshafiq-portfolio.vercel.app](https://shahramshafiq-portfolio.vercel.app)
- Team: EchoFrame Labs, "Rebuilding the Past. Designing the Future."

---

## How this internship actually went

### Getting started

I set up a working portfolio and repo, ran a first 3D-learning script, and hit my first real lesson early: a research pull request sat unmerged on a branch for over a week, meaning the work was invisible to anyone just browsing the repo. I caught it during a strict self-audit in Week 1, merged it, and rewrote the README to actually reflect the repo's real scope. That single habit, checking that finished work is actually visible and actually true rather than just done, ended up running through the entire internship.

### The reconstruction that mattered most

The track's core question was whether I could turn footage of a heritage site into a real 3D digital record. The textbook plan was Structure from Motion (SfM): match features across multiple photos, triangulate, get a point cloud, the same approach COLMAP uses. I had 6 real, individually-sourced photos of Badshahi Mosque in Lahore, so I tested SfM on them properly before assuming it would work: ORB feature detection and RANSAC-verified matching across 3 photo pairs. The result was 12 to 17 geometrically consistent matches out of 2,000+ keypoints per photo, consistently weak across every pair. That is not enough overlap for real triangulation, and later research tied this back to a cited heritage-photogrammetry source: reliable multi-view reconstruction needs roughly 66% photo overlap and 10 to 15 degree camera spacing, which 6 photos taken by different photographers with no shared capture plan were never going to have.

I did not force a point cloud out of weak matches. Instead I pivoted to a monocular reconstruction of a different, single photo (the Jaulian Buddhist monastery ruins at Taxila), built a heuristic depth estimate from image brightness and edge structure, and hand-wrote a real `.ply` point cloud exporter directly against the file format spec rather than pulling one from a library. Validated it three separate ways before calling it done: re-parsed the file to confirm every line was well-formed, reloaded it from disk (not from the in-memory arrays that built it) and re-rendered it to confirm the shape survived the round trip, and cross-checked that render against an earlier module's equivalent visualization. Final result: 13,375 points, 436 KB, opens correctly in MeshLab, CloudCompare, or Blender.

That reconstruction became the spine of the rest of the internship. It got quantitative QA added later (density, outlier detection, color sanity, four-angle rendering, not just one visual check). It got turned into a real triangulated mesh in the program's final stretch, a build that looked visibly wrong on the first attempt despite passing its own validation checks, which took real, measured debugging (not a guess) to actually fix. And it anchored the case study I wrote as my single strongest contribution across the whole track.

### Machine learning, applied to the actual problem

Alongside the reconstruction work, I worked through the youthxAI curriculum end to end: Python fundamentals applied to perspective projection and point clouds, linear regression from scratch checked against scikit-learn and applied to predicting reconstruction time, logistic regression applied to a genuine "is this photo usable" classifier plus the real public Kaggle Titanic dataset, and a neural network (Keras, 784-128-64-10) trained on the full 70,000-image MNIST dataset to 97.18% test accuracy, backed by a from-scratch numpy rebuild of the same architecture landing in the same range, the actual proof the from-scratch version works and not just a claim that it should.

### Two short films, honestly made

I built two videos from real project artifacts rather than stock footage standing in for things that didn't exist: a 75-second short on the Taxila reconstruction assembled from the actual point cloud, the actual ML renders, and procedurally synthesized original audio (no licensed music, even under real pressure to use one), and a personal storytelling piece, "Twenty Guys and a Bus Ride," about three years at Cadet College Hasan Abdal's hostel, narrated with my own recorded voice-over over real photos and published to YouTube. Both had real bugs I caught by actually watching the output rather than trusting a clean render, including one where three-digit zero-padded frame filenames broke alphabetical sort past 999 frames and scrambled the entire video's order.

### Team Taxila: leading a group sprint alongside the individual track

Separate from my individual work, I was team lead for Team Taxila, a cross-institute group building a live location page and presentation on Taxila and the Gandhara learning route, aimed at history students, Buddhist heritage tourists, and museum visitors. The active roster ended up being three of us: **Ruwaida Shakeel** (Air University), **Rabeea Iman** (SADA NUST), and me. I missed the team's one live planning session due to a scheduling conflict, so Rabeea and Ruwaida moved ahead without me, Rabeea built the team's Canva presentation, and Ruwaida built and published a genuinely strong live page.

Ruwaida's page covers the real, current UNESCO warning over cement restoration damaging original stonework at Mohra Moradu and Sirkap (I independently checked the central claim against multiple real news outlets before trusting it), an interactive 3D reconstruction toggle, a client-side tool that lets a visitor turn their own photo into a point cloud using the same monocular heuristic built for this internship, a Gandhara learning-route map, and 13 specific, checkable sources rather than a generic reading list. I contributed a standalone interactive showcase page (a live, drag-to-rotate Three.js viewer of the actual `.ply` reconstruction, now archived in this repo under [`pmw-heritage-showcase-archive/`](pmw-heritage-showcase-archive/) after the internship wrapped) and additional content via a pull request into her live page's repo. Later, for the individual track's own Final Sprint 3, I came back and wrote a full, checked peer review of her page (clarity, evidence, presentation, accuracy, impact, every citation link actually tested against real HTTP requests), and used one real lesson from that review, that an honest caveat should sit next to the thing it describes, to revise my own mesh write-up with real before/after commits.

### Falling short, then catching up: the Extension Sprints

Partway through, my dashboard showed I hadn't logged enough verified hours against the program's original schedule, and TechRealm opened a cohort-wide two-week extension for exactly this. Rather than treat it as busywork, I used it to make seven real, evidence-backed improvements to work that already existed: quantitative point-cloud QA, a cited and independently-verified research source log, a 22-case pytest suite for an API that had zero tests before, a self-audit that caught a real recurring documentation gap (the root README had gone stale again, the exact failure mode an earlier audit had already flagged once), a polish pass on the live showcase itself, a public blog-style write-up of the whole reconstruction journey, and finally a certificate evidence pack indexing every deliverable to a real link. Each sprint had to show a genuine before-and-after, not a new link added just to look busy.

### The last stretch: Final 10-Hour Sprint

After reaching 40 verified hours, the program unlocked one final stage: four 2.5-hour modules over four days to reach the 50-hour certificate threshold. I used them for a project case study on the point cloud reconstruction (with a fresh, independently re-executed verification, not just a link back to old evidence), a real build task that turned the point cloud into a triangulated mesh (including a full, honest debugging log when the first version looked visibly wrong despite passing its own checks), the peer review and revision described above, and a final curated portfolio page tying the whole internship together. That last module also caught the evidence pack's staleness a fourth time and a handful of leftover formatting issues in older files during a full-repo audit, the same "check it's actually still true" habit from Week 1, still running at the very end.

### The certificate

The internship concluded with a **Certificate of Appreciation** from TechRealm, certificate ID **TRN-58990**, issued **August 28, 2026**, recognizing verified contribution in AI-Based 3D Scene Reconstruction, in partnership with Digital Software Market, Home Collective, MagnificentH, and Youth x AI (the same youthxAI curriculum referenced throughout this repo). Signed by Waleed Ajmal, Founder and CEO of TechRealm, who was also my program manager for the whole internship.

---

## What's actually in this repo

```
preservemy.world-internship/
├── README.md                          <- you are here
├── index.html                         <- live final showcase (GitHub Pages)
├── week1-ai-review.md                 <- strict repo audit, merge fix, prompt reflection, revised in Extension Sprint 4
├── portfolio/
│   └── index.html                     <- personal HTML portfolio page
├── 3d-learning/
│   ├── point_cloud_basics.py          <- Python script: 3D reconstruction concepts
│   └── experiment_notes.md            <- what I tried, what worked, what didn't
├── blog-post/
│   ├── medium_draft.md                <- blog post content (posted on Dev.to)
│   └── 3d_reconstruction_walkthrough.md  <- Extension Sprint 6: public write-up
├── research/
│   ├── 3d_methods_comparison.md       <- COLMAP vs NeRF vs 3DGS vs MiDaS
│   ├── depth_map_demo.py              <- monocular depth simulation script
│   ├── depth_output.png               <- generated output
│   └── source_log_3d_methods.md       <- Extension Sprint 2: 5 live-verified, cited sources
├── footage-research/
│   ├── badshahi-mosque-multiangle.md  <- sourced, cited, multi-angle footage write-up
│   └── images/                        <- 6 verified real photos of Badshahi Mosque
├── heritage-writing/
│   └── mohenjo-daro.md                <- researched, cited heritage write-up
├── ml-viz-ar-capture3d/
│   ├── capture_to_3d_pipeline.py      <- ML features, AR lines, capture-to-3D on a real photo
│   └── output/                        <- 3 generated visualizations
├── week3-3d-reconstruction/
│   ├── sfm_feasibility_test.py        <- real ORB+RANSAC test of multi-view SfM viability
│   ├── build_ply_reconstruction.py    <- exports a real, validated .ply point cloud
│   ├── point_cloud_qa.py              <- Extension Sprint 1: quantitative point-cloud QA
│   └── output/                        <- jaulian_monastery_taxila.ply + verification renders
├── week3-logistic-regression/
│   ├── youthxai_logistic_regression.ipynb  <- logistic regression + real Kaggle Titanic pipeline
│   ├── data/titanic.csv               <- real, verified Titanic training set (891 rows)
│   └── output/                        <- classifier plot + Kaggle-format submission CSV
├── week3-story-film/
│   ├── script.md                      <- written story and script
│   ├── build_video.py                 <- builds a real MP4 from real project artifacts
│   └── output/taxila_preserved_in_3d.mp4  <- the final 75-second video
├── week4-neural-networks/
│   ├── youthxai_neural_networks.ipynb <- Keras MNIST classifier + from-scratch numpy cross-check
│   ├── visualisation_deck.html        <- self-contained results deck
│   └── output/                        <- training curves, confusion matrix, sample digits
├── week4-home-story/
│   ├── script.md                      <- personal storytelling script
│   ├── build_video.py                 <- builds the video from real photos + own voice-over
│   └── output/twenty_guys_and_a_bus_ride.mp4  <- the final video
├── week4-video-qa-followup/
│   └── README.md                      <- structured QA pass on the storytelling video, bugs found and fixed
├── heritage-api/
│   ├── app.py                         <- Flask REST API (7 endpoints)
│   ├── templates/index.html           <- HTML frontend
│   ├── react-app/index.html           <- React dashboard
│   ├── tests/test_app.py              <- Extension Sprint 3: 22-case pytest suite, 0 tests before
│   └── screenshots/                   <- evidence the app runs
├── iris-hacks-interest/
│   └── README.md                      <- Iris Hacks IV interest form confirmation
├── pmw-heritage-showcase-archive/
│   ├── index.html                     <- Team Taxila's standalone live 3D viewer, formerly its own repo
│   └── assets/                        <- its self-contained copies of the photo, pipeline renders, and .ply
├── certificate-evidence-pack/
│   └── README.md                      <- full evidence index, every deliverable mapped to a link
├── case-study/
│   └── README.md                      <- Final Sprint 1: project case study on the Jaulian .ply reconstruction
├── final-sprint2-mesh-reconstruction/
│   ├── build_mesh.py                  <- Final Sprint 2: turns the point cloud into a real triangulated mesh
│   ├── render_mesh_qa.py              <- reloads the exported mesh from disk and renders QA views
│   └── output/                        <- jaulian_monastery_mesh.ply + QA renders
├── final-sprint3-peer-review/
│   └── README.md                      <- Final Sprint 3: peer review of a teammate's page, before/after revision
├── final-sprint4-portfolio-certificate/
│   └── README.md                      <- Final Sprint 4: curated final portfolio and certificate evidence page
├── youthxai_python_colab.ipynb        <- Kaggle Python course applied to 3D reconstruction
├── youthxai_linear_regression.ipynb   <- linear regression + Kaggle Intro to ML
└── youthxai-regression-output/        <- generated plots from the regression notebook
```

**A note on the repo's name:** this was originally built and submitted as `PMW-day1`, and every module above was reviewed and graded under that name. It was renamed to `preservemy.world-internship` after the certificate was issued and every submission had already been marked, GitHub automatically redirects the old repository URLs to this one, so nothing that was ever submitted is broken.

---

## Portfolio

My portfolio lives at [`portfolio/index.html`](portfolio/index.html). It's a single-file static site built with pure HTML, CSS, and JavaScript (no frameworks, no build step). Features include:

- Animated sparkle particle background on the hero section
- Scroll-reveal animations
- Working contact form via Web3Forms
- Mobile responsive with hamburger navigation
- Live at [shahramshafiq-portfolio.vercel.app](https://shahramshafiq-portfolio.vercel.app)

> Note: `img.png` (my photo) needs to sit in the same folder as `index.html` to render correctly locally. The deployed Vercel version has it included.

---

## 3D Reconstruction: What I Learned

I started from near zero on this. Here's my honest understanding, built up over the internship:

**The core problem:** you have a flat 2D photo and want to recover the 3D structure of whatever was photographed. It's under-constrained: infinitely many 3D scenes could produce the same 2D image.

**How photogrammetry solves it:** take many photos from different angles, find matching feature points across images (SIFT, ORB), triangulate those features into 3D coordinates. This is Structure from Motion (SfM), and the output is a sparse point cloud.

**Dense reconstruction:** run Multi-View Stereo (MVS) after SfM to fill in the gaps and get millions of points instead of thousands.

**What NeRF does differently:** instead of matching features, a Neural Radiance Field trains a small network to learn what the scene looks like from any angle, taking (x, y, z, viewing direction) and outputting (color, density). Rendering means ray marching through the network. Slow to train, photorealistic results.

**Gaussian Splatting:** newer than NeRF, represents the scene as millions of small 3D Gaussian blobs, renders in real time. Likely what PreserveMy.World uses for its actual "explorable worlds" product.

**Why this matters for heritage:** a historic site can be reconstructed from drone or phone footage and stored forever as a 3D model, explorable even after the physical site is damaged, demolished, or made inaccessible.

**My Python experiment:** [`3d-learning/point_cloud_basics.py`](3d-learning/point_cloud_basics.py) simulates a photogrammetry pipeline from scratch using numpy and matplotlib: depth, projection, and point cloud generation for a heritage building corner. I tried Open3D first, hit a GLIBC version issue on my setup, and documented the fallback in the experiment notes instead of hiding it.

---

## Blog Post

Full post: [`blog-post/medium_draft.md`](blog-post/medium_draft.md)

My learning journey with 3D reconstruction and how I planned to apply it at PreserveMy.World, written early in the internship.

---

## Research: Comparing 3D Reconstruction Methods

Full comparison: [`research/3d_methods_comparison.md`](research/3d_methods_comparison.md)

**Environment used:** Python 3.11 (Anaconda), Git, VS Code, gh CLI. AI coding assistant (Cursor) used for boilerplate and syntax help, all logic read, understood, and verified manually before committing.

Compared four methods: COLMAP, NeRF, 3D Gaussian Splatting (3DGS), and Monocular Depth Estimation (MiDaS), each entry covering inputs, outputs, hardware needs, difficulty, and where it fits the PMW pipeline.

[`research/depth_map_demo.py`](research/depth_map_demo.py) simulates monocular depth estimation: generates a synthetic depth map of a heritage building (pillars, facade, arched doorway), converts it to a 3D point cloud via back-projection, and saves a 3-panel visualization at [`research/depth_output.png`](research/depth_output.png).

**Key finding:** for PMW's "explorable worlds" feature, the full production pipeline is likely capture footage, run COLMAP for camera poses and a sparse point cloud, feed that into 3D Gaussian Splatting for real-time navigable output, and optionally run NeRF (Nerfstudio) for high-quality archival renders. Monocular depth (MiDaS) fills in when only a single photo of a site exists, exactly the situation the Week 3 reconstruction ended up in.

**Tutorials watched:** Computerphile's "How does 3D Scanning Work?" and "Neural Radiance Fields," "Structure from Motion explained," Open3D documentation, Nerfstudio documentation.

---

## Python Fundamentals Applied to 3D Reconstruction

Notebook: [`youthxai_python_colab.ipynb`](youthxai_python_colab.ipynb)

Covers the 7 Kaggle Python course topics (variables, functions, conditionals, lists, loops, strings/dicts, libraries), each applied directly to 3D reconstruction: perspective projection, point cloud generation, and camera view rendering for heritage sites (Lahore Fort, Rohtas Fort, Mohenjo-daro, Badshahi Mosque).

---

## Heritage Reconstruction API

Full app: [`heritage-api/`](heritage-api/)

A full-stack Flask and React web app modeling the actual PMW reconstruction pipeline: a Flask REST API with 7 endpoints serving data for 4 real Pakistani heritage sites, two frontends (a Flask-rendered HTML reference page and a React dashboard with an animated 3D point cloud), and a reconstruction job simulator. Tested via curl, Postman, and a direct LAN IP hit. Full setup and API docs in [`heritage-api/README.md`](heritage-api/README.md).

---

## Repo Audit and Prompt Engineering

Full write-up: [`week1-ai-review.md`](week1-ai-review.md)

Ran a strict AI-assisted audit against my own GitHub work instead of asking for generic feedback. The top finding was real: a pull request merging research into `main` had been open for over a week without being merged, meaning that work was invisible to anyone browsing the default branch. Fixed it, rewrote the README to reflect the true scope of the repo, and documented what worked and failed about the prompting process itself. Revisited twice more later in the internship (see Extension Sprint 4 below) when the same failure mode quietly recurred.

---

## Multi-Angle Footage: Badshahi Mosque

Full write-up: [`footage-research/badshahi-mosque-multiangle.md`](footage-research/badshahi-mosque-multiangle.md)

Sourced, downloaded, and individually verified 6 real photos of Badshahi Mosque covering distinct angles (front facade, aerial, interior, wide front view with garden, minaret side angle, elevated panorama), then wrote a technical piece auditing what the footage set does and does not cover for an actual 3D reconstruction pipeline. This is the same photo set the Week 3 SfM feasibility test later ran on, and honestly failed on.

---

## Heritage Write-up: Mohenjo-daro

Write-up: [`heritage-writing/mohenjo-daro.md`](heritage-writing/mohenjo-daro.md)

A 451-word researched piece on Mohenjo-daro: what it is, why it matters, what a visitor should notice. Every historical fact, construction date, population, UNESCO status, the salinity threat, the 2012 and 2022 conservation warnings, checked against Wikipedia and cross-verified against a second independent source before being written down.

---

## Linear Regression and Kaggle Intro to ML

Notebook: [`youthxai_linear_regression.ipynb`](youthxai_linear_regression.ipynb)

Linear regression implemented from scratch with gradient descent and checked against scikit-learn (both converge on the same slope and intercept), applied to predicting reconstruction time from photo count. Followed by the core Kaggle Intro to ML lessons (data exploration, first model, validation, underfitting/overfitting, random forests) applied to a simulated 220-job heritage reconstruction dataset. Every cell executed and verified before committing, generated plots in [`youthxai-regression-output/`](youthxai-regression-output/).

---

## ML Visualizations, AR Lines and Capture-to-3D

Pipeline and write-up: [`ml-viz-ar-capture3d/`](ml-viz-ar-capture3d/)

One real photo of the Jaulian monastery ruins at Taxila run through three stages: Sobel gradient and Harris corner feature detection, an AR-style line overlay simulating what a heritage app would show live on a phone camera, and a heuristic capture-to-3D colored point cloud. Two real bugs were caught by actually looking at the rendered output rather than trusting that the code ran without errors: the point cloud stage initially treated the sky as a physical surface and warped the whole projection (fixed by measuring this photo's actual sky brightness and masking it out), and the AR line overlay initially produced 271 noisy lines blanketing the frame (fixed by tightening thresholds down to 25 clean, meaningful lines).

---

## Convert Curated Footage to a 3D Reconstruction (.ply)

Write-up: [`week3-3d-reconstruction/`](week3-3d-reconstruction/)

The full technical detail behind the flagship story told above: the real SfM feasibility test (12 to 17 consistent matches out of 2,000+ keypoints per photo, not enough for triangulation), the pivot to a monocular reconstruction of the Jaulian monastery, and the hand-written `.ply` exporter validated three separate ways.

---

## Logistic Regression and Kaggle Titanic

Notebook: [`week3-logistic-regression/`](week3-logistic-regression/)

Logistic regression from scratch, checked against scikit-learn, applied to a genuine reconstruction problem: classifying whether a captured photo is usable, replacing a hand-guessed threshold from an earlier notebook with an actual trained classifier. Followed by the real, public Kaggle Titanic dataset (891 passengers, verified against known statistics before use), cleaned and run through a proper 80/20 train/validation split, then exported as a Kaggle-format submission CSV.

---

## Story, Script, Film and Edit

Write-up: [`week3-story-film/`](week3-story-film/)

A real, playable 75-second MP4 assembled from genuine project artifacts (a real photo, real generated visualizations, a real rotating render of the actual `.ply` point cloud), with a synthesized original audio track, Ken Burns motion, and crossfade dissolves, no voiceover by team decision since only one of three teammates could realistically record one. Caught two real bugs by checking output instead of trusting a clean exit code, including one serious one where the entire video played back scrambled out of order (three-digit zero-padded frame filenames broke alphabetical sort past 999 frames). Fixed and re-verified from scratch: correct scene order across sample timestamps, genuine point cloud rotation, and the audio track checked for silence gaps and clipping rather than assumed to sound right.

---

## Neural Networks: MNIST Digit Classifier

Notebook and deck: [`week4-neural-networks/`](week4-neural-networks/)

A Keras Sequential model (784-128-64-10) trained on the real, full 70,000-image MNIST dataset, 97.18% test accuracy on 10,000 held-out images the model never saw. Backed by a from-scratch numpy rebuild of the same architecture (manual forward pass and backpropagation, no library), landing in the same range on the same test set. Caught a real bug while building this: `matplotlib.use('Agg')` was silently blocking every chart from actually embedding in the executed notebook, caught by checking the saved file's real image data instead of trusting that the plotting cells ran without error.

---

## Individual Storytelling: Twenty Guys and a Bus Ride

Write-up: [`week4-home-story/`](week4-home-story/) &middot; live: [youtu.be/5nhRp_gWVRs](https://youtu.be/5nhRp_gWVRs)

What home means to me: three years at Cadet College Hasan Abdal's hostel, the routine, basketball, away fixtures at sister colleges, and the twenty guys in my wing, told with my own recorded voice-over over real photos of the team, the wing, and the campus gate, plus licensed B-roll for the two beats with no real photo available. Structured QA pass documented separately in [`week4-video-qa-followup/`](week4-video-qa-followup/): four real bugs found and fixed, a voice-over that was technically present but inaudible under the music, audio clipping traced to two distinct causes in the ffmpeg filter chain, caption-to-narration sync drift, and one B-roll clip that turned out to show mismatched footage on closer inspection.

---

## Extension Sprints: Verified Make-up Work

Seven sprints during the cohort-wide two-week program extension, each one a real, evidence-backed improvement to an existing deliverable, not new filler added just to log hours:

- **Sprint 1, quantitative point-cloud QA**: [`week3-3d-reconstruction/point_cloud_qa.py`](week3-3d-reconstruction/point_cloud_qa.py) added density, nearest-neighbor outlier detection, a color sanity check, and 4-angle rendering to the Taxila `.ply` reconstruction, which previously only had a single visual reload check.
- **Sprint 2, cited source log**: [`research/source_log_3d_methods.md`](research/source_log_3d_methods.md), 5 sources on COLMAP, NeRF, 3D Gaussian Splatting, and monocular depth, each independently live-verified, tied directly back to the real Week 3 SfM result instead of left as generic references.
- **Sprint 3, real test suite**: [`heritage-api/tests/test_app.py`](heritage-api/tests/test_app.py), 22 pytest cases covering every endpoint, up from 0 tests before. Proved the suite actually catches regressions by deliberately breaking a rule, watching the test fail, then reverting.
- **Sprint 4, this revision**: reviewed [`week1-ai-review.md`](week1-ai-review.md) against the judging rubric and found the exact failure mode it originally flagged, a stale root README, had quietly recurred (everything from Week 4 onward was missing, including the live showcase). Fixed it and documented the whole before/after.
- **Sprint 5, final artifact improvement**: polished the live showcase itself ([`index.html`](index.html)), adding a mentor note and an Extension Sprints section it had never had, then re-verified every link, image, and video on the deployed page.
- **Sprint 6, public write-up**: [`blog-post/3d_reconstruction_walkthrough.md`](blog-post/3d_reconstruction_walkthrough.md), a public walkthrough of the reconstruction journey, the SfM failure, the pivot, the QA hardening. Caught and corrected a factual error in its own first draft before publishing.
- **Sprint 7, certificate evidence pack**: [`certificate-evidence-pack/README.md`](certificate-evidence-pack/README.md), a single index mapping every deliverable across the internship to its real GitHub link and completion date.

---

## Final 10-Hour Sprint: Certificate Completion Work

Four 2.5-hour modules over the internship's last four days, reaching the 50-hour certificate threshold:

- **Final Sprint 1, project case study**: [`case-study/README.md`](case-study/README.md), a full case study on the strongest personal contribution on this track, the validated Jaulian monastery `.ply` reconstruction, including a fresh, independently re-executed verification rather than just a link back to old evidence.
- **Final Sprint 2, build / research proof**: [`final-sprint2-mesh-reconstruction/`](final-sprint2-mesh-reconstruction/), a real triangulated mesh built on the validated point cloud. The first attempt rendered as a spiky, unusable mess despite passing its own validation checks; measured the actual cause, tried two fixes that didn't work, found the one that did, and documented the real, still-present residual limitation instead of overselling the fix.
- **Final Sprint 3, peer review and revision**: [`final-sprint3-peer-review/`](final-sprint3-peer-review/), a real, checked peer review of Ruwaida Shakeel's live Team Taxila page, plus a genuine revision applied to my own Final Sprint 2 README as a direct result of what the review surfaced, with real before/after commits.
- **Final Sprint 4, portfolio and certificate evidence**: [`final-sprint4-portfolio-certificate/`](final-sprint4-portfolio-certificate/), the final curated portfolio page tying the whole internship together, plus a fix to the Certificate Evidence Pack's staleness and a full-repo audit that caught leftover formatting issues in older files.

---

## Iris Hacks IV

[`iris-hacks-interest/`](iris-hacks-interest/): confirmed interest in Iris Hacks IV, a free virtual AI hackathon for students 13+, with the real confirmation screenshot as evidence.

---

## Mission Connection

PreserveMy.World's core mission is to document and preserve cultural heritage before it disappears. 3D reconstruction is the technical engine that makes this possible, turning footage of a mosque, fort, or old city street into a navigable digital record. Pakistan has hundreds of underdocumented heritage sites. Mohenjo-daro faces active deterioration and sits as a priority site in my heritage-api data model. Taxila, the site of both my individual reconstruction work and Team Taxila's group page, received a real, formal UNESCO warning in 2026 over restoration work damaging original stonework. This wasn't a hypothetical exercise about a mission statement, there was a real, current gap to document.

---

*Portfolio, a validated 3D point-cloud reconstruction with quantitative QA and a real triangulated mesh, three applied ML notebooks (linear regression, logistic regression, a 97.18%-accuracy neural network), a full-stack heritage reconstruction API with a real test suite, two short films, a cited research source log, a self-revising repo audit, a led group heritage-preservation page, and a live final showcase all live in this repo, and all of it led to a real certificate, TRN-58990, issued August 28, 2026.*
