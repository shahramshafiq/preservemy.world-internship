# Curated Footage to 3D Reconstruction

**Shahram Shafiq | AI-Based 3D Reconstruction Track | PreserveMy.World x TechRealm 2026**

**Archive note:** this was originally its own standalone repo and live GitHub Pages site, built specifically to be a fully public, login-free page for Team Taxila's group review. Now that the internship is complete and this repo has been consolidated into one place, the standalone repo and its live page no longer exist separately, everything below is preserved here exactly as it was, folder structure and all.

---

## What this is

A single, self-contained web page for **Team Taxila** that curates the strongest footage and reconstruction work into one narrative: a real photo of the Jaulian monastery ruins at Taxila, the actual feature-detection and depth math behind reconstruction, and a genuine, live, drag-to-rotate 3D point cloud running in the browser via Three.js, not a screenshot or a mockup.

Everything shown is real work already built and verified in [`shahramshafiq/preservemy.world-internship`](https://github.com/shahramshafiq/preservemy.world-internship), pulled into this dedicated repo so it can be a clean, fully public, login-free web page, and scoped specifically to Taxila rather than mixing in unrelated sites from other individual modules.

---

## Structure

```
PMW-heritage-showcase/
├── index.html              <- the whole page, single file
└── assets/
    ├── taxila/               <- Jaulian monastery ruins photo
    ├── pipeline/             <- ML feature map, AR overlay, capture-to-3D renders
    └── ply/
        └── jaulian_monastery_taxila.ply   <- the real point cloud, loaded live
```

---

## The live 3D viewer

Built with Three.js (loaded via CDN, no build step) and `PLYLoader`. It loads the actual `.ply` file, the same one hand-validated in the original build (13,375 points, vertex count and colors verified in-browser before shipping this page). Drag to rotate, scroll to zoom, matches the honest documentation already written for this reconstruction: a monocular depth heuristic, not multi-view Structure from Motion (that was tested first and ruled out on a curated multi-angle photo set from another module, only 12-17 geometrically consistent matches out of 2,000+ keypoints per photo pair, documented on the page itself).

---

## Why a separate repo

The portal's own review feedback flagged login-gated links as a real weakness elsewhere in this internship. A GitHub Pages site is the opposite of that: fully public, no account needed, loads directly. This repo exists specifically to be that kind of artifact.
