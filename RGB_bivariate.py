# by Matias I. Bofarull Oddo - 2023.01.02

import numpy as np
import matplotlib.pyplot as plt
from algorithms_Bezier import surface_Bezier
from parula_list import parula_500

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.size": 10})


def colorspline(colormap, dotted=False):
    R = [row[0] for row in colormap]
    G = [row[1] for row in colormap]
    B = [row[2] for row in colormap]
    if dotted:
        ax.plot(R, G, B, ":", c="gray", linewidth=0.5)
        ax.scatter(R, G, B, s=30, c=colormap)
    else:
        for i in range(len(R)):
            ax.plot(
                R[i : i + 2],
                G[i : i + 2],
                B[i : i + 2],
                color=colormap[i],
                linewidth=7,
                # solid_capstyle="round",
            )


bivariate_map = np.divide(
    np.array(
        [
            [[1, 149, 255], [1, 106, 184], [1, 56, 103], [1, 1, 1]],
            [[100, 186, 255], [101, 147, 184], [103, 103, 103], [104, 55, 1]],
            [[185, 220, 255], [184, 184, 184], [185, 145, 102], [188, 104, 1]],
            [[255, 255, 255], [253, 219, 183], [255, 185, 103], [255, 148, 1]],
        ],
    ),
    255,
)

surface_control_points = np.divide(
    np.array(
        [
            [[1, 149, 255], [1, 1, 1]],
            [[255, 255, 255], [255, 148, 1]],
        ]
    ),
    255,
)
surface = surface_Bezier(surface_control_points, steps_u=50, steps_v=50)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

for row in surface_control_points:
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)
for row in surface_control_points.transpose(1, 0, 2):
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)

for step_u in surface:
    colorspline(step_u)

for row in bivariate_map:
    for triplet in row:
        ax.scatter(
            triplet[0],
            triplet[1],
            triplet[2],
            s=500,
            color=triplet,
            edgecolors="k",
        )


ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.xaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_zticks([0, 1])
ax.set_xlabel("R (x)")
ax.set_ylabel("G (y)")
ax.set_zlabel("B (z)")
ax.view_init(azim=130, elev=-40)
ax.set_box_aspect((1, 1, 1))
plt.show()
