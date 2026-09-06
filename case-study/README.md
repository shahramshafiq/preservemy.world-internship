# Case Study: Turning a Single Photo of the Jaulian Monastery Into a Validated 3D Point Cloud

**Shahram Shafiq | AI-Based 3D Scene Reconstruction Track | Final Sprint 1: Project Case Study (Week 7)**

---

## Problem

PreserveMy.World's core promise is turning footage of a heritage site into an explorable 3D digital record. My job on this track was to actually build a piece of that pipeline, not just read about it: given the footage already curated earlier in the internship (6 real photos of Badshahi Mosque, plus a single photo of the Jaulian Buddhist monastery ruins at Taxila), could I produce a real, verifiable 3D reconstruction, and honestly, which approach would even work with what was actually available?

The naive plan was multi-view Structure from Motion (SfM), the same feature-matching-and-triangulation approach COLMAP uses in production. The real question the project needed answered was whether that plan was viable at all on photos that were sourced by different photographers with no overlap plan, rather than a controlled multi-view capture.

## My Role

This was solo, individually-authored work, not a group deliverable. I wrote every line of the three scripts below myself: [`sfm_feasibility_test.py`](../week3-3d-reconstruction/sfm_feasibility_test.py), [`build_ply_reconstruction.py`](../week3-3d-reconstruction/build_ply_reconstruction.py), and [`point_cloud_qa.py`](../week3-3d-reconstruction/point_cloud_qa.py). The `.ply` point cloud exporter was hand-written directly against the PLY format spec (ASCII header declaring vertex count and per-vertex `x y z red green blue` properties, one line per point), not pulled from a library, specifically so I could actually explain every line of the file it produces. AI assistance (Cursor) was used for boilerplate syntax help while writing OpenCV/numpy calls; the feature-matching logic, the depth heuristic, the PLY writer, and every one of the QA checks below were designed and verified by me before being committed.

## Evidence

- **Real commit history across three separate work sessions**, not one squashed commit: [full commit log for this folder](https://github.com/shahramshafiq/preservemy.world-internship/commits/main/week3-3d-reconstruction)
  - [`4858a3f`](https://github.com/shahramshafiq/preservemy.world-internship/commit/4858a3f) &middot; 6 Jul 2026 &middot; original SfM test + monocular `.ply` build
  - [`89077b0`](https://github.com/shahramshafiq/preservemy.world-internship/commit/89077b0) &middot; 21 Jul 2026 &middot; Extension Sprint 1, quantitative point-cloud QA added
  - [`8da5b1c`](https://github.com/shahramshafiq/preservemy.world-internship/commit/8da5b1c) &middot; 22 Jul 2026 &middot; Extension Sprint 2, cited source log tying the SfM result to real literature
- **The reconstruction itself:** [`output/jaulian_monastery_taxila.ply`](../week3-3d-reconstruction/output/jaulian_monastery_taxila.ply), 13,375 vertices, 436 KB, openable in MeshLab, CloudCompare, or Blender.
- **Full technical write-up:** [`week3-3d-reconstruction/README.md`](../week3-3d-reconstruction/README.md)
- **Screenshots / renders proving the work is real, not claimed:**

  ![Four-angle QA render of the point cloud](../week3-3d-reconstruction/output/multi_angle_qa_render.png)
  *Four independent camera angles rendered from the saved `.ply`, three show the recognizable ring-of-walls-around-a-courtyard shape, the fourth is an honest edge-on sliver, explained rather than hidden.*

  ![Nearest-neighbor distance histogram](../week3-3d-reconstruction/output/nn_distance_histogram.png)
  *Nearest-neighbor spacing across 2,000 sampled points, used to flag spatial outliers.*

## Process

1. **Tested feasibility before picking an approach.** Ran ORB feature detection and RANSAC-verified fundamental matrix estimation across 3 photo pairs from the curated Badshahi Mosque set. Result: only 12 to 17 geometrically consistent inliers out of 2,000+ keypoints per photo, consistently weak across all three pairs.
2. **Documented the failure honestly instead of forcing an output.** That match count is not enough overlap for real triangulation. I did not fabricate a point cloud out of it.
3. **Pivoted to a monocular reconstruction** of a different, single photo (the Jaulian monastery ruins at Taxila), extending a heuristic depth approach already validated in an earlier module (row-position-plus-edge depth heuristic, sky/haze brightness masking).
4. **Hand-wrote the `.ply` exporter** against the format spec and validated it three separate ways: re-parsed the file to confirm the declared vertex count matches the real data line count with well-formed fields, reloaded it from disk (not from the in-memory arrays that generated it) and re-rendered it to confirm the shape survives the round trip, and cross-checked that render against the earlier module's equivalent visualization.
5. **Extension Sprint 1: added quantitative QA**, because a visual reload check alone is not proof. Measured real bounding box, centroid, and point density; sampled 2,000 points and measured true nearest-neighbor distance to catch outliers (median + 6x median-absolute-deviation threshold, flagged 60/2000 = 3.00% as outliers, a reasonable rate for a monocular heuristic, not a red flag); confirmed all RGB values are valid and 99.3% of points carry real structural color rather than sky/haze; rendered four independent viewing angles instead of trusting one.
6. **Extension Sprint 2: traced the SfM failure to real literature** instead of leaving it as an unexplained number. [`research/source_log_3d_methods.md`](../research/source_log_3d_methods.md) cites a heritage-photogrammetry source establishing that reliable multi-view reconstruction needs roughly 66% photo overlap and 10 to 15 degree camera spacing, exactly the coverage the 6 available Badshahi photos never had.

## Result

A real, standard `.ply` point cloud (13,375 vertices) of the Jaulian Buddhist monastery ruins at Taxila that:
- Opens correctly in standard point cloud viewers
- Passes a quantitative QA pass (density, outlier rate, color sanity, multi-angle render), not just a single visual check
- Has an honestly documented, literature-backed explanation for why the originally planned multi-view approach was not used, instead of a silently abandoned attempt

## Independent Re-Verification (done for this case study, 6 Aug 2026)

Linking back to old evidence isn't enough on its own, so for this case study I re-ran the verification fresh rather than just re-describing the original results, using two separate methods.

**1. Re-executed [`point_cloud_qa.py`](../week3-3d-reconstruction/point_cloud_qa.py) from a clean run today.** Every number reproduced exactly against what was originally documented in Extension Sprint 1, with no drift:

```
Loaded 13375 points, header count matched data line count exactly.
Bounding box size: [5.2839 1.511  2.0046]
Centroid:          [-0.01552563 -0.38368494  3.49463251]
Point density:     835.7 points per cubic unit
Mean NN distance:   0.0254
Median NN distance: 0.0223
Outlier threshold (median + 6*MAD): 0.0483
Points flagged as spatial outliers: 60 / 2000 (3.00%)
Points with real color variation (structure): 99.3%
```

The regenerated `multi_angle_qa_render.png` and `nn_distance_histogram.png` came out byte-identical to the versions already committed to the repo (confirmed with `git status` and `git diff --stat` immediately after the re-run, both came back empty), meaning this pipeline is genuinely deterministic and not a fluke that happened to look right once.

**2. Cross-checked the `.ply` file with a second, independent parser**, deliberately not reusing `point_cloud_qa.py`'s own loading function, to rule out a bug in one script's parsing logic silently agreeing with itself:

```
File size on disk: 446849 bytes (436 KB, matches the write-up)
Header declares vertex count: 13375
Actual data line count: 13375
Header count matches data line count: True
Malformed lines (not exactly 6 fields): 0
Lines with an out-of-range color channel: 0
```

Two independently written pieces of code, reading the same file two different ways, agree exactly. That is a stronger integrity check than either script proving itself alone.

## What I Learned

- **A failed test is still a real result if you check it properly.** The instinct to force a point cloud out of 12 to 17 shaky matches would have produced geometrically meaningless output. Testing feasibility first, and being willing to report "this does not work" with numbers to back it up, was more valuable than skipping straight to a forced answer.
- **"It loaded without an error" is not validation.** The three-way validation (re-parse, reload-and-re-render, cross-check against another module) and later the Sprint 1 quantitative QA are what actually made this a reconstruction I could defend, not just a file that exists.
- **Multi-view SfM has a concrete, citable coverage requirement** (~66% overlap, 10 to 15 degree spacing), not a vague "need more photos." Knowing the actual number is what let me explain, rather than just observe, why the Badshahi Mosque set didn't work.
- **A monocular heuristic has a real, explainable limitation**, not a hidden one: the thin edge-on render in the 4-angle QA is the geometrically correct outcome for that camera angle, and reporting it honestly is more credible than only showing the three flattering angles.

## Next Improvements

- Replace the row-position-plus-edge depth heuristic with a trained monocular depth network (MiDaS), which the project's own research comparison ([`research/3d_methods_comparison.md`](../research/3d_methods_comparison.md)) already identifies as the right tool for single-photo cases.
- Source a genuine multi-view capture of one heritage site with the ~66% overlap and 10-15 degree spacing the literature says is required, so a real COLMAP-style SfM pipeline can be tested properly instead of on photos that were never planned for it.
- Extend the point cloud to a meshed surface (Poisson reconstruction or similar) so the output can be viewed as a solid model instead of only as points.

---

## Mission connection

Taxila is a real, actively at-risk Pakistani heritage site: Team Taxila's group work this same internship covered a genuine 2026 UNESCO warning about cement restoration damaging structures at Mohra Moradu and Sirkap, both part of the same Gandhara-era complex as the Jaulian monastery reconstructed here. A 3D record of a site like this is only useful if it can be trusted, which is the entire reason this case study leads with validation and an honestly reported failure rather than just a finished-looking file.

---

## What I personally verified while building this case study

- Re-read [`week3-3d-reconstruction/README.md`](../week3-3d-reconstruction/README.md) in full and cross-checked every number in this document (inlier counts, vertex count, outlier percentage, file size) against that source file rather than recalling them from memory.
- Confirmed all three commit hashes cited above against `git log` directly for this folder.
- Confirmed the embedded images above are the actual files committed to the repo, not placeholders.
- Re-ran [`point_cloud_qa.py`](../week3-3d-reconstruction/point_cloud_qa.py) fresh today and independently re-parsed the `.ply` file with a second, separately written script, rather than only re-linking to results from weeks ago, see the "Independent Re-Verification" section above.
