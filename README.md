<div align="center">

# PreserveMy.World Internship Portfolio

Monocular 3D heritage reconstruction, a Flask heritage API and applied ML notebooks, built for the PreserveMy.World x TechRealm AI 3D track.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=flat-square&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Live](https://img.shields.io/badge/Showcase-GitHub%20Pages-222222?style=flat-square&logo=github&logoColor=white)

</div>

## Overview

PreserveMy.World is a non-profit that uses 3D capture and storytelling to digitally preserve cultural heritage sites. This repository is the work I produced on its AI-Based 3D Scene Reconstruction track (June to August 2026, run with TechRealm). It starts with a Structure-from-Motion feasibility test on six photos, then builds a monocular reconstruction of the Jaulian monastery ruins at Taxila, exports it as a hand-written ASCII `.ply` point cloud, checks it with quantitative QA and turns it into a triangulated mesh. Around that core sit a Flask and React heritage API with a 22-case test suite, applied ML notebooks, two short films and written research.

## Demo

Live showcase: **[shahramshafiq.github.io/preservemy.world-internship](https://shahramshafiq.github.io/preservemy.world-internship/)**

Watch the storytelling video on [YouTube](https://youtu.be/5nhRp_gWVRs), or open the rendered films in the repo: [week3-story-film/output/taxila_preserved_in_3d.mp4](week3-story-film/output/taxila_preserved_in_3d.mp4) and [week4-home-story/output/twenty_guys_and_a_bus_ride.mp4](week4-home-story/output/twenty_guys_and_a_bus_ride.mp4).

| Point cloud, four QA angles | Point cloud vs. mesh |
|---|---|
| ![Point cloud rendered from four angles](week3-3d-reconstruction/output/multi_angle_qa_render.png) | ![Point cloud and mesh from the same camera angle](final-sprint2-mesh-reconstruction/output/point_cloud_vs_mesh.png) |

| Heritage API, React dashboard | Heritage API, reconstruct simulator |
|---|---|
| ![React dashboard](heritage-api/screenshots/04-react-dashboard-top.png) | ![Reconstruct simulator](heritage-api/screenshots/05-react-reconstruct-simulator.png) |

The reconstruction is a heuristic from a single photo, not a laser scan or a multi-view capture. Treat the surface as an illustration of shape, not measured geometry.

## Key Features

- **SfM feasibility test:** `sfm_feasibility_test.py` runs ORB features, brute-force matching and a RANSAC fundamental-matrix check on three pairs of Badshahi Mosque photos. Only 12 to 17 RANSAC inliers survive among the 60 best candidate matches per pair, so the pipeline does not force a point cloud out of them.
- **Monocular point cloud:** `build_ply_reconstruction.py` estimates depth from image row position and Sobel edge strength, masks sky pixels by brightness, back-projects with a pinhole model and writes 13,375 coloured points.
- **Hand-written PLY exporter:** the ASCII header and vertex lines are written directly against the format spec, with no mesh library involved.
- **Quantitative point-cloud QA:** `point_cloud_qa.py` reports bounding box and density, nearest-neighbour spacing with a median plus 6 MAD outlier threshold, a colour range check, and renders from four angles.
- **Triangulated mesh:** `build_mesh.py` samples the depth field on a coarser, smoothed grid (step 6, Gaussian sigma 3.0) and exports a `.ply` with 1,482 vertices and 2,346 faces, after checks for degenerate triangles, non-manifold edges and slivers. `render_mesh_qa.py` reloads the exported file and renders it.
- **Heritage Reconstruction API:** a Flask REST API with 7 endpoints for four Pakistani heritage sites and four reconstruction methods, with an HTML reference page and a React dashboard, covered by 22 pytest cases.
- **Applied ML notebooks:** linear regression and logistic regression (including the Kaggle Titanic data) and a Keras MNIST network (784-128-64-10) that reaches 97.18% test accuracy in the executed notebook, plus a from-scratch numpy rebuild of the same architecture.
- **Scripted short films:** `build_video.py` scripts assemble two MP4s from project artifacts with numpy, Pillow and ffmpeg.

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.11 |
| Computer vision and numerics | OpenCV, NumPy, SciPy, Matplotlib |
| 3D formats | ASCII PLY (point cloud and triangle mesh) |
| API | Flask 3, Flask-CORS |
| Frontend | Jinja HTML page, React 18 and Babel from a CDN, Three.js 0.160 (archived viewer page) |
| Machine learning | TensorFlow / Keras, scikit-learn, pandas, Jupyter notebooks |
| Testing | pytest with the Flask test client |
| Video | Pillow, NumPy, SciPy, ffmpeg |
| Hosting | GitHub Pages (static showcase) |

## Project Structure

```text
index.html                         # Live showcase page served by GitHub Pages
footage-research/                  # Six sourced Badshahi Mosque photos and coverage write-up
ml-viz-ar-capture3d/               # Sobel and Harris features, line overlay, first capture-to-3D pass
week3-3d-reconstruction/           # SfM test, PLY point cloud build, quantitative QA
final-sprint2-mesh-reconstruction/ # Triangulated mesh build and mesh QA renders
heritage-api/                      # Flask API, HTML and React frontends, tests/, screenshots/
research/                          # Method comparison (COLMAP, NeRF, 3DGS, MiDaS) and source log
week3-logistic-regression/         # Notebook, Titanic CSV, outputs
week4-neural-networks/             # Keras and numpy MNIST notebook, results deck
week3-story-film/                  # Script and build script for the 3D reconstruction film
week4-home-story/                  # Script and build script for the storytelling film
pmw-heritage-showcase-archive/     # Archived Three.js viewer page for the point cloud
case-study/                        # Write-up of the Jaulian reconstruction
blog-post/                         # Public walkthrough of the reconstruction journey
portfolio/                         # Early single-file personal portfolio page
```

## Getting Started

### Prerequisites

- Python 3.11
- For the reconstruction scripts: `numpy`, `opencv-python`, `matplotlib` and `scipy`
- For the notebooks: `jupyter`, `pandas`, `scikit-learn` and `tensorflow`
- For the video scripts: `pillow`, `scipy` and `ffmpeg` on your PATH
- No environment variables are read by any script in this repository

### Installation

```bash
git clone https://github.com/shahramshafiq/preservemy.world-internship.git
cd preservemy.world-internship
pip install numpy opencv-python matplotlib scipy
pip install -r heritage-api/requirements.txt
```

### Run

Reconstruction pipeline (run from the repository root, outputs are written next to each script):

```bash
python week3-3d-reconstruction/sfm_feasibility_test.py
python week3-3d-reconstruction/build_ply_reconstruction.py
python week3-3d-reconstruction/point_cloud_qa.py
python final-sprint2-mesh-reconstruction/build_mesh.py
python final-sprint2-mesh-reconstruction/render_mesh_qa.py
```

Heritage API:

```bash
cd heritage-api
python app.py
```

The server starts on `http://localhost:5000`. Open `/` for the API reference page and `/react` for the React dashboard.

## Usage

```bash
curl http://localhost:5000/api/health
curl http://localhost:5000/api/sites/lahore-fort
curl http://localhost:5000/api/sites/badshahi-mosque/pointcloud
curl -X POST http://localhost:5000/api/reconstruct \
  -H "Content-Type: application/json" \
  -d '{"site_id":"lahore-fort","method":"colmap","num_photos":120}'
```

| Endpoint | Purpose |
|---|---|
| `GET /api/health` | Service status |
| `GET /api/sites` and `/api/sites/<id>` | Site list and full site record |
| `GET /api/sites/<id>/pointcloud` | Sampled XYZ points for a reconstructed site |
| `POST /api/reconstruct` | Queue a simulated reconstruction job (at least 10 photos) |
| `GET /api/methods` and `/api/stats` | Method list and global statistics |

Site ids are `lahore-fort`, `rohtas-fort`, `mohenjo-daro` and `badshahi-mosque`; methods are `colmap`, `nerf`, `3dgs` and `midas`. The exported `.ply` files open in MeshLab, CloudCompare or Blender.

## Testing

```bash
cd heritage-api
python -m pytest tests/ -v
```

The suite has 22 test cases covering every endpoint and each error branch (404, 400 and 422 responses).

## Limitations and Roadmap

- The reconstruction is a monocular heuristic, not a trained depth network or real multi-view triangulation. The mesh still shows some fine ridging, and a depth model such as MiDaS is the planned fix.
- The Heritage API serves in-memory data, and `/api/reconstruct` only simulates a job. `app.py` starts Flask in debug mode on all interfaces, so it is for local use only.
- The video build scripts depend on source clips, fonts and photos that are not committed, so `week4-home-story/build_video.py` cannot be re-run from a fresh clone. The rendered MP4 files are included.
- There is no top-level `requirements.txt`; install the packages listed above to run the individual scripts.

## Author

**Shahram Shafiq** - [GitHub](https://github.com/shahramshafiq) | [LinkedIn](https://www.linkedin.com/in/shahramshafiq/)
