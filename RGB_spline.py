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
                linewidth=8,
                solid_capstyle="round",
            )


control_points = np.array(
    [
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0],
            [1, 1, 1],
        ],
    ]
)

point_count = 500

cubespline = surface_Bezier(control_points, steps_u=1, steps_v=point_count)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

for row in control_points:
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)
for row in control_points.transpose(1, 0, 2):
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)

# colorspline(plt.cm.hot(np.linspace(0, 1, point_count)))
colorspline(plt.cm.afmhot(np.linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_heat(np.linspace(0, 1, point_count)))
colorspline(cubespline[0])

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
ax.view_init(azim=45, elev=45)
ax.set_box_aspect((1, 1, 1))
plt.show()
