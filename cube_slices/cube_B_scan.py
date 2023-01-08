# by Matias I. Bofarull Oddo - 2023.01.02

import matplotlib.pyplot as plt
import numpy as np

from algorithms_Bezier import surface_Bezier

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.size": 10})


def colorspline(colormap, dotted=False):
    colormap[colormap < 0] = 0
    colormap[colormap > 1] = 1
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
                # solid_capstyle="butt",
            )


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

Q = 0

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)

Q = 0.0625

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)


Q = 0.125

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)


Q = 0.25

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)

Q = 0.5

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)

Q = 1

surface_control_points = np.array(
    [
        [[0, 0, Q], [0, 1, Q]],
        [[1, 0, Q], [1, 1, Q]],
    ]
)
surface = surface_Bezier(surface_control_points)
for step_u in surface[::-1]:
    colorspline(step_u)

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
ax.view_init(azim=45, elev=35)
ax.set_box_aspect((1, 1, 1))
plt.show()
