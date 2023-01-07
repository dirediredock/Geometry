# RGB_ColorSpline_Cube

<img src="figures/sequential_atomic_2.png" width="50%"><img src="figures/RGB_skew_atomic.png" width="50%">

What if

Well, there are a lot of "batteries included" benefits to this method. First, minimal data storage, because you only save the coordinates of the control points. Second, everything is parametrized in regular intervals, so rate of change within the colormap is always perceptually uniform. Third, interpolation between the start and end control points allow arbitray within-colormap resolution (the limit is at the ability of a physical display to display RGB values). Fourth, this is a robust method to create bivariate colormaps, from four-point bilinear patches to a highly complex surface or mosaic of surfaces. Finally, existing manually-crafted colormaps can be approximated with this method, and then edited to increase smoothness and perceptual uniformity.

Bivariate chloropleth colormap and RGB bilinear patch

<img src="figures/bivariate_choropleth.png" width="100%"><img src="figures/bivariate_map.jpg" width="100%">

<img src="figures/color_1A.png" width="100%"><img src="figures/color_2A.png" width="50%"><img src="figures/color_3A.png" width="50%">
<img src="figures/color_1B.png" width="100%"><img src="figures/color_2B.png" width="50%"><img src="figures/color_3B.png" width="50%">

```python
patch_1A = np.array(
    [
        [[0, 0, 0], [1, 0, 1]],
        [[0, 1, 1], [1, 1, 0]],
    ]
)
patch_1B = np.array(
    [
        [[1, 1, 1], [0, 1, 0]],
        [[1, 0, 0], [0, 0, 1]],
    ]
)
```

<img src="figures/patch_1AB.png" width="100%"><img src="figures/patch_1A.png" width="50%"><img src="figures/patch_1B.png" width="50%">

```python
surface_control_points = np.array(
    [
        [[0, 1, 1], [0, 0, 0]],
        [[1, 0, 1], [1, 1, 0]],
    ]
)
surface_control_points = np.array(
    [
        [[0, 1, 0], [1, 0, 0]],
        [[0, 0, 1], [1, 1, 1]],
    ]
)
```
<img src="figures/patch_2AB.png" width="100%"><img src="figures/patch_2A.png" width="50%"><img src="figures/patch_2B.png" width="50%">

```python
surface_control_points = np.array(
    [
        [[0, 0, 0], [1, 0, 1]],
        [[1, 1, 0], [0, 1, 1]],
    ]
)
surface_control_points = np.array(
    [
        [[1, 0, 0], [0, 0, 1]],
        [[0, 1, 0], [1, 1, 1]],
    ]
)
```

<img src="figures/patch_3AB.png" width="100%"><img src="figures/patch_3A.png" width="50%"><img src="figures/patch_3B.png" width="50%">

Event Horizon Telescope used the `afmhot` colormap to visualize the M87 black hole

<img src="figures/hot.png" width="100%">

Approximating Google's `turbo` colormap with a handful of control points

<img src="figures/turbo_spline_2.png" width="100%">
<img src="figures/turbo_spline_1.png" width="100%">

Celebrity colormaps (`parula`, `viridis`, `turbo`) within the RGB cube
 
<img src="figures/parula_turbo_viridis_1.png" width="100%">
<img src="figures/parula_turbo_viridis_2.png" width="100%">
<img src="figures/sequential_atomic_1.png" width="100%">

Other surfaces 

<img src="figures/random_patch.png" width="100%">
<img src="figures/cone.png" width="100%">

---

Unit Circle (Trigonometric)
Unit Circle (Parametric)

3D Spiral (plt.scatter)
3D Spiral (plt.plot)

Bezier Spline
Bezier Surface

Barycentric Coordinates

Bezier Subdivision
Quadratic corner cutting (Chaikin)
Cubic corner cutting
4-point scheme

Spline parametrization, curvature, normal, tangent

OBJ meshes
