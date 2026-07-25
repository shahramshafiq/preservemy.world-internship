"""
Extension Sprint 3 improvement: this app had zero automated tests before
this file existed (confirmed by running pytest --collect-only against the
bare repo first, see heritage-api/README.md for the before/after evidence).
Every route in app.py gets covered here: the happy path, and the error
cases that route's own code branches for (missing body, unknown site,
too few photos, unknown method), so a future change that breaks one of
those branches actually gets caught instead of silently shipping.
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, SITES, METHODS


def make_client():
    app.config['TESTING'] = True
    return app.test_client()


# ---------------------------------------------------------------------------
# GET /api/health
# ---------------------------------------------------------------------------
def test_health_returns_ok_status():
    client = make_client()
    resp = client.get('/api/health')
    assert resp.status_code == 200
    body = resp.get_json()
    assert body['status'] == 'ok'
    assert body['service'] == 'EchoFrame Heritage Reconstruction API'


def test_health_reports_correct_site_and_method_counts():
    client = make_client()
    body = client.get('/api/health').get_json()
    assert body['sites_loaded'] == len(SITES)
    assert body['methods_available'] == len(METHODS)


# ---------------------------------------------------------------------------
# GET /api/sites
# ---------------------------------------------------------------------------
def test_list_sites_returns_all_four():
    client = make_client()
    body = client.get('/api/sites').get_json()
    assert body['count'] == 4
    returned_ids = {s['id'] for s in body['sites']}
    assert returned_ids == {'lahore-fort', 'rohtas-fort', 'mohenjo-daro', 'badshahi-mosque'}


def test_list_sites_summary_excludes_heavy_fields():
    # the summary view should not leak the full point cloud size/lat/lng
    # payload, only the fields the endpoint's own summary_keys tuple names
    client = make_client()
    body = client.get('/api/sites').get_json()
    first = body['sites'][0]
    assert 'lat' not in first
    assert 'point_cloud_size' not in first
    assert 'name' in first and 'status' in first


# ---------------------------------------------------------------------------
# GET /api/sites/<site_id>
# ---------------------------------------------------------------------------
def test_get_known_site_returns_full_record():
    client = make_client()
    resp = client.get('/api/sites/lahore-fort')
    assert resp.status_code == 200
    body = resp.get_json()
    assert body['name'] == 'Lahore Fort'
    assert body['era'] == 'Mughal (1566 AD)'
    assert 'lat' in body and 'lng' in body


def test_get_unknown_site_returns_404_with_available_ids():
    client = make_client()
    resp = client.get('/api/sites/not-a-real-site')
    assert resp.status_code == 404
    body = resp.get_json()
    assert 'error' in body
    assert set(body['available_ids']) == {'lahore-fort', 'rohtas-fort', 'mohenjo-daro', 'badshahi-mosque'}


def test_all_four_real_sites_are_individually_reachable():
    client = make_client()
    for site_id in SITES:
        resp = client.get(f'/api/sites/{site_id}')
        assert resp.status_code == 200, f"{site_id} should return 200"
        assert resp.get_json()['id'] == site_id


# ---------------------------------------------------------------------------
# GET /api/sites/<site_id>/pointcloud
# ---------------------------------------------------------------------------
def test_pointcloud_for_reconstructed_site_returns_points():
    client = make_client()
    resp = client.get('/api/sites/lahore-fort/pointcloud')
    assert resp.status_code == 200
    body = resp.get_json()
    assert body['sample_returned'] > 0
    assert len(body['points']) == body['sample_returned']
    # every point needs real x/y/z/layer fields, not a malformed shape
    for pt in body['points'][:5]:
        assert set(pt.keys()) == {'x', 'y', 'z', 'layer'}


def test_pointcloud_for_queued_site_returns_202_not_data():
    # mohenjo-daro is status "queued" in the real data, this must not
    # silently return an empty/fake point cloud for a site with none yet
    client = make_client()
    resp = client.get('/api/sites/mohenjo-daro/pointcloud')
    assert resp.status_code == 202
    body = resp.get_json()
    assert body['status'] == 'queued'
    assert 'hint' in body


def test_pointcloud_unknown_site_returns_404():
    client = make_client()
    resp = client.get('/api/sites/nowhere/pointcloud')
    assert resp.status_code == 404


def test_pointcloud_is_deterministic_per_site():
    # the endpoint seeds random with hash(site_id), so calling it twice for
    # the same site should return the exact same points, this is what
    # actually makes it safe to cache or compare on the frontend
    client = make_client()
    first = client.get('/api/sites/badshahi-mosque/pointcloud').get_json()['points']
    second = client.get('/api/sites/badshahi-mosque/pointcloud').get_json()['points']
    assert first == second


# ---------------------------------------------------------------------------
# POST /api/reconstruct
# ---------------------------------------------------------------------------
def test_reconstruct_happy_path_returns_202_with_job():
    client = make_client()
    resp = client.post('/api/reconstruct', json={
        'site_id': 'lahore-fort', 'method': 'colmap', 'num_photos': 120
    })
    assert resp.status_code == 202
    body = resp.get_json()
    assert body['status'] == 'queued'
    assert body['site'] == 'Lahore Fort'
    assert body['job_id'].startswith('LAHO-COL-')
    assert body['estimated_hours'] > 0


def test_reconstruct_missing_body_returns_400():
    client = make_client()
    resp = client.post('/api/reconstruct')
    assert resp.status_code == 400
    assert 'error' in resp.get_json()


def test_reconstruct_missing_site_id_returns_400():
    client = make_client()
    resp = client.post('/api/reconstruct', json={'method': 'colmap', 'num_photos': 50})
    assert resp.status_code == 400


def test_reconstruct_unknown_site_returns_404():
    client = make_client()
    resp = client.post('/api/reconstruct', json={'site_id': 'atlantis', 'num_photos': 50})
    assert resp.status_code == 404


def test_reconstruct_too_few_photos_returns_422():
    # app.py's own rule: minimum 10 photos required
    client = make_client()
    resp = client.post('/api/reconstruct', json={'site_id': 'lahore-fort', 'num_photos': 3})
    assert resp.status_code == 422


def test_reconstruct_unknown_method_returns_400():
    client = make_client()
    resp = client.post('/api/reconstruct', json={
        'site_id': 'lahore-fort', 'method': 'magic', 'num_photos': 50
    })
    assert resp.status_code == 400


def test_reconstruct_defaults_method_to_colmap_when_omitted():
    client = make_client()
    resp = client.post('/api/reconstruct', json={'site_id': 'rohtas-fort', 'num_photos': 40})
    assert resp.status_code == 202
    assert resp.get_json()['method'] == 'COLMAP'


# ---------------------------------------------------------------------------
# GET /api/methods
# ---------------------------------------------------------------------------
def test_list_methods_returns_all_four():
    client = make_client()
    body = client.get('/api/methods').get_json()
    assert body['count'] == 4
    names = {m['name'] for m in body['methods']}
    assert names == {'COLMAP', 'NeRF', '3D Gaussian Splatting', 'MiDaS'}


# ---------------------------------------------------------------------------
# GET /api/stats
# ---------------------------------------------------------------------------
def test_stats_totals_match_the_real_site_data():
    client = make_client()
    body = client.get('/api/stats').get_json()
    assert body['total_sites'] == 4
    expected_photos = sum(s['photos'] for s in SITES.values())
    assert body['total_photos_processed'] == expected_photos
    assert 'mohenjo-daro' not in body['critical_risk_sites']  # id, not name, must not leak here
    assert 'Mohenjo-daro' in body['critical_risk_sites']


# ---------------------------------------------------------------------------
# Frontend routes
# ---------------------------------------------------------------------------
def test_index_route_serves_html():
    client = make_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'html' in resp.data.lower()


def test_react_route_serves_html():
    client = make_client()
    resp = client.get('/react')
    assert resp.status_code == 200
