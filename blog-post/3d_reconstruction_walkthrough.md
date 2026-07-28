# building a real 3D reconstruction, including the part where it failed

*Extension Sprint 6 public write-up, PreserveMy.World x TechRealm Internship 2026*

---

I'm a CS student at FAST NUCES Islamabad, on the AI-Based 3D Reconstruction track for PreserveMy.World x TechRealm. PMW's whole point is turning phone footage of heritage sites into navigable 3D digital records before those sites are lost. This is the walkthrough of one specific reconstruction pipeline: a real failed attempt on one photo set, a pivot to a different photo, and a working 13,375-point `.ply` file of the Jaulian Buddhist monastery ruins at Taxila at the end.

---

## what I attempted first, and why it failed

The textbook way to do 3D reconstruction is Structure from Motion (SfM): take many overlapping photos of the same scene, match feature points across them, and triangulate where each point actually sits in 3D space. This is what COLMAP does, and it's the foundation almost every serious pipeline (NeRF, 3D Gaussian Splatting) builds on top of.

I had 6 curated photos of the Badshahi Mosque to work with, the set already sitting in the repo's footage-research folder. Before writing a single line of the reconstruction code, I tested whether SfM was actually viable on this specific set: ran ORB feature detection and RANSAC-verified fundamental matrix estimation across 3 photo pairs. Out of 2,000+ keypoints per photo, only 12 to 17 survived as geometrically consistent matches. That's not enough overlap to triangulate anything meaningful.

I could have quietly lowered my standards and forced a point cloud out of those 17 matches anyway. I didn't, because the output would have been geometrically meaningless, points scattered based on noise, not structure. Later, during one of the extension sprints, I actually went and found the real number that explains this: reliable multi-view reconstruction needs roughly 66% overlap between consecutive photos ([Cultural Heritage Imaging's photogrammetry guide](https://culturalheritageimaging.org/Technologies/Photogrammetry/)), and photos taken every 10 to 15 degrees around the subject. Those 6 photos were taken by different photographers at different times with no overlap plan at all. The test wasn't broken, it was accurately reporting that the input didn't meet the method's own requirements.

## what I built instead

Since multi-view SfM wasn't viable on that dataset, I didn't force it. I pivoted to a completely different photo: a single shot of the Jaulian Buddhist monastery ruins at Taxila, already used in an earlier ML/AR visualization module. On that one photo I built a monocular depth reconstruction, a single-photo heuristic (masking out the sky using the photo's actual brightness profile, then estimating depth from row position and edge strength), extending the same approach I'd already validated in that earlier module, so the depth logic itself wasn't new, only the `.ply` export was.

The part I'm most proud of technically: I wrote the `.ply` file exporter by hand against the actual format spec (ASCII header declaring vertex count, then one line per point with `x y z r g b`), instead of pulling in a library that would hide what was actually happening. That meant I could validate it three separate ways instead of just trusting a clean write: re-parsed the file afterward and checked the declared vertex count matched the real number of data lines exactly, reloaded it from disk (not from the in-memory arrays that built it) and re-rendered it to confirm the shape survived the round trip, and compared that against the earlier visualization module for consistency.

End result: 13,375 real 3D points, each with real color sampled from the source photo.

## catching my own blind spot later

Weeks after I first built this, during an extension make-up sprint, I went back and actually stress-tested the point cloud instead of assuming a validated file stays valid forever. I added real quantitative checks: point density, nearest-neighbor spacing (the standard way to catch outlier or duplicate points), a color sanity check, and renders from 4 different angles instead of the single static check I'd originally done.

One of those 4 angles rendered as a thin, nearly edge-on sliver. My first instinct was that something had broken. It hadn't, that's the geometrically correct result for a single-photo reconstruction viewed from the side perpendicular to the original camera angle, a real and honest limitation of monocular depth that a single "looks fine from the front" screenshot would have hidden. I kept that image in the writeup instead of only showing the angle that looked good.

## what AI helped with, and what I actually verified myself

I worked with Claude throughout this project. It wrote the ORB/RANSAC feasibility test, the `.ply` exporter, the later quantitative QA script, and the visualizations. What it didn't do is decide that a failed test was acceptable to paper over, or that a validated file didn't need re-checking months later. Every claim of "this works" in this project has a specific command behind it I actually ran and looked at the output of: the RANSAC inlier counts printed to a terminal, the re-parsed vertex count compared against the header, the reloaded render compared against the original, the nearest-neighbor distance histogram. I didn't take "it ran without an error" as proof of anything. A script that silently produces the wrong answer still exits with code 0.

## why this matters for PMW specifically

PreserveMy.World's mission only works if the 3D reconstructions people rely on are actually trustworthy, not just visually plausible. A heritage site that gets digitally preserved with fabricated or unvalidated geometry isn't really preserved, it's a guess wearing the appearance of data. The discipline in this project, testing viability before committing to a method, validating output multiple independent ways, and going back later to stress-test something I'd already called "done", is the same discipline PMW needs at scale if its 3D archive of Pakistani heritage sites is going to be something researchers, tourists, and the sites' own communities can actually trust.

## what I'd improve next

The monocular heuristic is a real stopgap, not a long-term answer. The honest next step is a proper trained monocular depth model (MiDaS or similar) instead of a hand-written brightness/row-position heuristic, and a second real capture session for Taxila specifically shot with the 66% overlap and 10-15 degree spacing that real multi-view SfM actually needs, so this site gets a genuine multi-view reconstruction instead of a single-photo estimate.

---

**Full technical detail and code:** [github.com/shahramshafiq/PMW-day1/tree/main/week3-3d-reconstruction](https://github.com/shahramshafiq/PMW-day1/tree/main/week3-3d-reconstruction), QA follow-up in the same folder's [`point_cloud_qa.py`](https://github.com/shahramshafiq/PMW-day1/blob/main/week3-3d-reconstruction/point_cloud_qa.py). Live project showcase: [shahramshafiq.github.io/PMW-day1](https://shahramshafiq.github.io/PMW-day1/).
