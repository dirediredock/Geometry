# by Matias I. Bofarull Oddo - 2022.12.26

import numpy as np
import matplotlib.pyplot as plt

from algorithms_Bezier import surface_Bezier

surface_control_points = np.array(
    [
        [[0, 0, 0], [1, 0, 1]],
        [[0, 1, 1], [1, 1, 0]],
    ]
)
surface = surface_Bezier(surface_control_points)

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

for row in surface_control_points:
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)
for row in surface_control_points.transpose(1, 0, 2):
    ax.plot(row[:, 0], row[:, 1], row[:, 2], ".-k", linewidth=0.75)

ax.scatter(surface[:, :, 0], surface[:, :, 1], surface[:, :, 2], s=1)

spline_control_points = np.array([[[0, 0, 0], [0.5, 0.5, 1], [1, 1, 0]]])
spline = surface_Bezier(spline_control_points, steps_u=100, steps_v=100)
ax.plot(spline[:, :, 0][0], spline[:, :, 1][0], spline[:, :, 2][0], c="r")

spline_control_points = np.array([[[0, 1, 1], [0.5, 0.5, 0], [1, 0, 1]]])
spline = surface_Bezier(spline_control_points, steps_u=100, steps_v=100)
ax.plot(spline[:, :, 0][0], spline[:, :, 1][0], spline[:, :, 2][0], c="r")

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_zticks([0, 1])

ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

ax.xaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)


ax.set_box_aspect((1, 1, 1))
plt.box("on")
plt.show()
