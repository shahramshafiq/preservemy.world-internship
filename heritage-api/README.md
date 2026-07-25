# EchoFrame Heritage Reconstruction API

Full-stack Flask + React web app for AI-based 3D heritage site data.
Built for the PreserveMy.World x TechRealm 2026 internship.

**Team:** EchoFrame Labs | **Track:** AI-Based 3D Scene Reconstruction

---

## Setup

```bash
cd heritage-api
pip install -r requirements.txt
python app.py
```

Server runs at `http://localhost:5000` (also accessible via local IP: `http://192.168.x.x:5000`).

---

## Frontends

| Frontend | URL | Description |
|----------|-----|-------------|
| React Dashboard | http://localhost:5000/react | Animated point cloud, live terminal, reconstruct simulator |
| HTML Page | http://localhost:5000/ | API reference with live "Try it" buttons |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Service health and version |
| GET | /api/sites | List all heritage sites |
| GET | /api/sites/:id | Full details for one site |
| GET | /api/sites/:id/pointcloud | Sampled 3D XYZ point cloud data |
| POST | /api/reconstruct | Queue a reconstruction pipeline job |
| GET | /api/methods | List 3D reconstruction methods |
| GET | /api/stats | Global statistics |

**Site IDs:** `lahore-fort`, `rohtas-fort`, `mohenjo-daro`, `badshahi-mosque`

---

## curl Commands

### Health check
```bash
curl http://localhost:5000/api/health
```

### Direct IP hit (replace with your machine's LAN IP)
```bash
curl http://192.168.1.x:5000/api/health
```

### List all heritage sites
```bash
curl http://localhost:5000/api/sites
```

### Get site details
```bash
curl http://localhost:5000/api/sites/lahore-fort
curl http://localhost:5000/api/sites/mohenjo-daro
```

### Get point cloud data
```bash
curl http://localhost:5000/api/sites/lahore-fort/pointcloud
curl http://localhost:5000/api/sites/badshahi-mosque/pointcloud
```

### POST: Queue a reconstruction job
```bash
curl -X POST http://localhost:5000/api/reconstruct \
  -H "Content-Type: application/json" \
  -d '{"site_id":"lahore-fort","method":"colmap","num_photos":120}'
```

```bash
curl -X POST http://localhost:5000/api/reconstruct \
  -H "Content-Type: application/json" \
  -d '{"site_id":"mohenjo-daro","method":"midas","num_photos":95}'
```

### List reconstruction methods
```bash
curl http://localhost:5000/api/methods
```

### Global stats
```bash
curl http://localhost:5000/api/stats
```

---

## Postman

1. Open Postman, create a new collection: **EchoFrame Heritage API**
2. Set base URL variable: `http://localhost:5000`
3. Add GET requests for each `/api/*` endpoint above
4. For POST /api/reconstruct: set Body to raw JSON:
   ```json
   {"site_id": "lahore-fort", "method": "colmap", "num_photos": 120}
   ```
   Set Content-Type header to `application/json`

---

## Heritage Sites Covered

| Site | Era | Status | Risk |
|------|-----|--------|------|
| Lahore Fort | Mughal (1566 AD) | Reconstructed | Medium |
| Rohtas Fort | Sur Empire (1541 AD) | In Progress | Low |
| Mohenjo-daro | Indus Valley (2500 BC) | Queued | Critical |
| Badshahi Mosque | Mughal (1673 AD) | Reconstructed | Low |

---

## 3D Reconstruction Methods

- **COLMAP** (Structure from Motion + MVS): Foundation pipeline, 50+ photos, produces dense point cloud
- **NeRF** (Neural Radiance Fields): Photorealistic archival renders, GPU required
- **3DGS** (3D Gaussian Splatting): Real-time explorable worlds, PMW primary target
- **MiDaS** (Monocular Depth): Quick scan from a single photo, no GPU needed

---

## Extension Sprint 3: automated test suite (before / after)

**Before:** zero automated tests existed for any of the 7 endpoints. Confirmed directly, not assumed:

```
$ python -m pytest --collect-only
collected 0 items
no tests collected in 0.10s
```

Every route (`/api/health`, `/api/sites`, `/api/sites/<id>`, `/api/sites/<id>/pointcloud`, `/api/reconstruct`, `/api/methods`, `/api/stats`, plus the two frontend routes) had no coverage at all, every error branch already written into `app.py` (unknown site returns 404, too few photos returns 422, missing body returns 400, unknown method returns 400) was completely unverified.

**After:** [`tests/test_app.py`](tests/test_app.py), 22 real test cases covering the happy path and every error branch for every endpoint, using Flask's own test client, no live server needed.

```
$ python -m pytest tests/ -v
collected 22 items
...
============================== 22 passed in 1.53s ==============================
```

**Proof the tests actually test something, not just pass trivially:** temporarily changed the minimum-photos rule in `app.py` from `< 10` to `< 2`, reran the suite, and watched the corresponding test genuinely fail:

```
tests/test_app.py::test_reconstruct_too_few_photos_returns_422 FAILED
E       assert 202 == 422
E        +  where 202 = <WrapperTestResponse streamed [202 ACCEPTED]>.status_code
1 failed in 1.12s
```

Reverted the change immediately after, reran the full suite to confirm it was back to 22 passed. This before/after/broken/fixed cycle is the actual evidence that this test suite would catch a real regression, not just decoration that always shows green.

Run it yourself: `cd heritage-api && pip install -r requirements.txt && python -m pytest tests/ -v`
