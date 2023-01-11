# by Matias I. Bofarull Oddo - 2023.01.11

from random import randrange

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from algorithms_Bezier import surface_Bezier

mpl.use("Agg")


def jitt():
    return randrange(0, 2, 1)


def normalize(values_per_axis):
    scaled = np.subtract(values_per_axis, np.nanmin(values_per_axis))
    return np.divide(scaled, np.nanmax(scaled))


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
                linewidth=6,
                # solid_capstyle="round",
            )


control_points = np.array(
    [
        [
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
        ],
        [
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
        ],
        [
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
        ],
        [
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
            [jitt(), jitt(), jitt()],
        ],
    ]
)

surface = surface_Bezier(control_points, steps_u=120, steps_v=120)
surface_norm = np.stack(
    (
        normalize(surface[:, :, 0]),
        normalize(surface[:, :, 1]),
        normalize(surface[:, :, 2]),
    ),
    axis=2,
)

fig = plt.figure(figsize=(10, 10))
ax = plt.Axes(fig, [0.015, 0.015, 0.969, 0.969])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(surface_norm)

plt.savefig("colorsurface_result.png", dpi=300)
# plt.show()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

ax.scatter(
    normalize(surface[:, :, 0]),
    normalize(surface[:, :, 1]),
    normalize(surface[:, :, 2]),
    s=1,
)

# for step_u in surface_norm:
#     colorspline(step_u)

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

plt.savefig("colorsurface_spline.png", dpi=300)
# plt.show()
