"""
Final Sprint 2 QA render: loads the exported mesh back from disk (not from
the in-memory arrays that built it, the same reload-from-disk discipline
used for the point cloud in week3-3d-reconstruction), and renders it shaded
from 4 independent angles plus a side-by-side against the source point
cloud, so the mesh can be checked visually and not just by its numeric
validation stats.
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MESH_PATH = os.path.join(SCRIPT_DIR, 'output', 'jaulian_monastery_mesh.ply')
OUT_DIR = os.path.join(SCRIPT_DIR, 'output')


def load_ply_mesh(path):
    with open(path) as f:
        lines = f.readlines()
    header_end = next(i for i, l in enumerate(lines) if l.strip() == 'end_header')
    header = lines[:header_end]
    n_v = int([l for l in header if l.startswith('element vertex')][0].split()[-1])
    n_f = int([l for l in header if l.startswith('element face')][0].split()[-1])
    body = lines[header_end + 1:]
    vertex_lines = body[:n_v]
    face_lines = body[n_v:n_v + n_f]
    xyz = np.array([[float(x) for x in l.split()[:3]] for l in vertex_lines])
    rgb = np.array([[int(x) for x in l.split()[3:6]] for l in vertex_lines])
    faces = np.array([[int(x) for x in l.split()[1:4]] for l in face_lines])
    return xyz, rgb, faces, n_v, n_f


xyz, rgb, faces, n_v, n_f = load_ply_mesh(MESH_PATH)
print(f"Reloaded mesh from disk: {n_v} vertices, {n_f} faces (independent of the script that built it)")

face_colors = rgb[faces].mean(axis=1) / 255.0
triangles = xyz[faces]

fig = plt.figure(figsize=(12, 10))
angles = [(20, -60), (20, 30), (60, -60), (80, 0)]
for i, (elev, azim) in enumerate(angles):
    ax = fig.add_subplot(2, 2, i + 1, projection='3d')
    mesh_coords = triangles[:, :, [0, 2, 1]]  # match the x, z, y axis order used in point_cloud_qa.py
    pc = Poly3DCollection(mesh_coords, facecolor=face_colors, edgecolor='none', linewidths=0)
    ax.add_collection3d(pc)
    ax.set_xlim(xyz[:, 0].min(), xyz[:, 0].max())
    ax.set_ylim(xyz[:, 2].min(), xyz[:, 2].max())
    ax.set_zlim(xyz[:, 1].min(), xyz[:, 1].max())
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(f"elev={elev}, azim={azim}", fontsize=10)
    ax.set_box_aspect([1, 1, 0.6])
    ax.set_axis_off()
fig.suptitle(f"Jaulian monastery mesh, {n_f} triangles, 4 independent viewing angles", fontsize=12, fontweight='bold')
fig.tight_layout()
render_path = os.path.join(OUT_DIR, 'mesh_multi_angle_render.png')
fig.savefig(render_path, dpi=130)
plt.close(fig)
print(f"Saved: {os.path.relpath(render_path, SCRIPT_DIR)}")

# Point cloud vs mesh, same angle, side by side, so the surface-filling
# effect of meshing is visible directly against the raw points it came from.
fig = plt.figure(figsize=(11, 5.2))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.scatter(xyz[:, 0], xyz[:, 2], xyz[:, 1], c=rgb / 255.0, s=1.2)
ax1.view_init(elev=20, azim=-60)
ax1.set_title(f"Point cloud ({n_v} points)", fontsize=10)
ax1.set_box_aspect([1, 1, 0.6])
ax1.set_axis_off()

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
pc2 = Poly3DCollection(triangles[:, :, [0, 2, 1]], facecolor=face_colors, edgecolor='none', linewidths=0)
ax2.add_collection3d(pc2)
ax2.set_xlim(xyz[:, 0].min(), xyz[:, 0].max())
ax2.set_ylim(xyz[:, 2].min(), xyz[:, 2].max())
ax2.set_zlim(xyz[:, 1].min(), xyz[:, 1].max())
ax2.view_init(elev=20, azim=-60)
ax2.set_title(f"Triangulated mesh ({n_f} faces)", fontsize=10)
ax2.set_box_aspect([1, 1, 0.6])
ax2.set_axis_off()

fig.suptitle("Point cloud vs mesh, same camera angle", fontsize=12, fontweight='bold')
fig.tight_layout()
compare_path = os.path.join(OUT_DIR, 'point_cloud_vs_mesh.png')
fig.savefig(compare_path, dpi=130)
plt.close(fig)
print(f"Saved: {os.path.relpath(compare_path, SCRIPT_DIR)}")
