# by Matias I. Bofarull Oddo - 2022.12.31

# 1. Get 100 viridis RGB triplets and plot them in an RGB cube
# 2. Approximate a 3D Bezier to the viridis curve
# 3. Do the same for inferno, magma, plasma
# 4. Create colormaps from these Beziers

# this is important, the first black hole image uses the inferno colormap

import matplotlib.pyplot as plt
from numpy import linspace
from seaborn import cm as sns_cm

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


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d", proj_type="ortho")

point_count = 500

# colorspline(plt.cm.Blues(linspace(0, 1, point_count)))
# colorspline(plt.cm.Greens(linspace(0, 1, point_count)))
# colorspline(plt.cm.Purples(linspace(0, 1, point_count)))
# colorspline(plt.cm.Reds(linspace(0, 1, point_count)))
# colorspline(plt.cm.Oranges(linspace(0, 1, point_count)))

# colorspline(plt.cm.Greys(linspace(0, 1, point_count)))
# colorspline(plt.cm.binary(linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_gray(linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_yarg(linspace(0, 1, point_count)))
# colorspline(plt.cm.gray(linspace(0, 1, point_count)))

# colorspline(plt.cm.Accent(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Dark2(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Paired(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Pastel1(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Pastel2(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Set1(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Set2(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.Set3(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.tab10(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.tab20(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.tab20b(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.tab20c(linspace(0, 1, point_count)), dotted=True)

# colorspline(plt.cm.flag(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.gist_ncar(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.gist_stern(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.prism(linspace(0, 1, point_count)), dotted=True)
# colorspline(plt.cm.nipy_spectral(linspace(0, 1, point_count)), dotted=True)

# colorspline(plt.cm.BrBG(linspace(0, 1, point_count)))
# colorspline(plt.cm.PiYG(linspace(0, 1, point_count)))
# colorspline(plt.cm.PuOr(linspace(0, 1, point_count)))
# colorspline(plt.cm.RdBu(linspace(0, 1, point_count)))
# colorspline(plt.cm.RdGy(linspace(0, 1, point_count)))
# colorspline(plt.cm.RdYlBu(linspace(0, 1, point_count)))
# colorspline(plt.cm.RdYlGn(linspace(0, 1, point_count)))
# colorspline(plt.cm.bwr(linspace(0, 1, point_count)))
# colorspline(plt.cm.coolwarm(linspace(0, 1, point_count)))
# colorspline(plt.cm.seismic(linspace(0, 1, point_count)))
# colorspline(plt.cm.twilight(linspace(0, 1, point_count)))
# colorspline(plt.cm.twilight_shifted(linspace(0, 1, point_count)))

# colorspline(plt.cm.BuGn(linspace(0, 1, point_count)))
# colorspline(plt.cm.BuPu(linspace(0, 1, point_count)))
# colorspline(plt.cm.GnBu(linspace(0, 1, point_count)))
# colorspline(plt.cm.PRGn(linspace(0, 1, point_count)))
# colorspline(plt.cm.OrRd(linspace(0, 1, point_count)))
# colorspline(plt.cm.PuBu(linspace(0, 1, point_count)))
# colorspline(plt.cm.PuBuGn(linspace(0, 1, point_count)))
# colorspline(plt.cm.PuRd(linspace(0, 1, point_count)))
# colorspline(plt.cm.RdPu(linspace(0, 1, point_count)))
# colorspline(plt.cm.YlGn(linspace(0, 1, point_count)))
# colorspline(plt.cm.YlGnBu(linspace(0, 1, point_count)))
# colorspline(plt.cm.YlOrBr(linspace(0, 1, point_count)))
# colorspline(plt.cm.YlOrRd(linspace(0, 1, point_count)))
# colorspline(plt.cm.afmhot(linspace(0, 1, point_count)))
# colorspline(plt.cm.bone(linspace(0, 1, point_count)))
# colorspline(plt.cm.cubehelix(linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_earth(linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_heat(linspace(0, 1, point_count)))
# colorspline(plt.cm.hot(linspace(0, 1, point_count)))
# colorspline(plt.cm.ocean(linspace(0, 1, point_count)))
# colorspline(plt.cm.pink(linspace(0, 1, point_count)))
# colorspline(plt.cm.terrain(linspace(0, 1, point_count)))

# colorspline(plt.cm.CMRmap(linspace(0, 1, point_count)))
# colorspline(plt.cm.Spectral(linspace(0, 1, point_count)))
# colorspline(plt.cm.gist_rainbow(linspace(0, 1, point_count)))
# colorspline(plt.cm.gnuplot(linspace(0, 1, point_count)))
# colorspline(plt.cm.gnuplot2(linspace(0, 1, point_count)))
# colorspline(plt.cm.hsv(linspace(0, 1, point_count)))
# colorspline(plt.cm.jet(linspace(0, 1, point_count)))
# colorspline(plt.cm.rainbow(linspace(0, 1, point_count)))

# colorspline(plt.cm.Wistia(linspace(0, 1, point_count)))
# colorspline(plt.cm.cool(linspace(0, 1, point_count)))
# colorspline(plt.cm.copper(linspace(0, 1, point_count)))
# colorspline(plt.cm.summer(linspace(0, 1, point_count)))
# colorspline(plt.cm.winter(linspace(0, 1, point_count)))

# colorspline(plt.cm.spring(linspace(0, 1, point_count)))
# colorspline(plt.cm.autumn(linspace(0, 1, point_count)))
# colorspline(plt.cm.brg(linspace(0, 1, point_count)))

# colorspline(plt.cm.cividis(linspace(0, 1, point_count)))
# colorspline(plt.cm.inferno(linspace(0, 1, point_count)))
# colorspline(plt.cm.magma(linspace(0, 1, point_count)))
# colorspline(plt.cm.plasma(linspace(0, 1, point_count)))
# colorspline(plt.cm.turbo(linspace(0, 1, point_count)))
# colorspline(plt.cm.viridis(linspace(0, 1, point_count)))

# colorspline(sns_cm.crest(linspace(0, 1, point_count)))
# colorspline(sns_cm.flare(linspace(0, 1, point_count)))
# colorspline(sns_cm.icefire(linspace(0, 1, point_count)))
# colorspline(sns_cm.mako(linspace(0, 1, point_count)))
colorspline(sns_cm.rocket(linspace(0, 1, point_count)))
# colorspline(sns_cm.vlag(linspace(0, 1, point_count)))

# crest
# flare
# icefire
# mako
# rocket
# vlag

# sinebow

# colorspline(parula_500)

# ax.scatter(0, 0, 0, s=30, color=[0, 0, 0])
# ax.scatter(0, 0, 1, s=30, color=[0, 0, 1])
# ax.scatter(0, 1, 0, s=30, color=[0, 1, 0])
# ax.scatter(0, 1, 1, s=30, color=[0, 1, 1])
# ax.scatter(1, 0, 0, s=30, color=[1, 0, 0])
# ax.scatter(1, 0, 1, s=30, color=[1, 0, 1])
# ax.scatter(1, 1, 0, s=30, color=[1, 1, 0])
# ax.scatter(1, 1, 1, s=30, color=[1, 1, 1])

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
ax.view_init(azim=40, elev=33)
ax.set_box_aspect((1, 1, 1))
plt.show()
