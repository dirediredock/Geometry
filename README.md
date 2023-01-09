# RGB_ColorSpline_Cube

<img src="figures/R_scan.png" width="33.33%"><img src="figures/G_scan.png" width="33.33%"><img src="figures/B_scan.png" width="33.33%">
<img src="figures/sequential_atomic_2.png" width="50%"><img src="figures/RGB_skew_atomic.png" width="50%">

What if Bézier surfaces define colormaps within the RGB cube?

We get a lot of benefits. First, minimal data storage, because we only save the coordinates of the control points. Second, everything is parametrized in regular intervals, so rate of change within the colormap is always perceptually uniform. Third, interpolation between the endpoint control points allow arbitray within-colormap resolution (the limit is at the ability of a physical display to display RGB values). Fourth, this is a robust method to create bivariate colormaps, from four-point bilinear patches to a highly complex surface or mosaic of surfaces. Fifth, linear splines are a special case of Bézier surfaces, so this method generalizes for all 3D splines out-of-the-box. Finally, existing manually-crafted colormaps can be approximated with this method, and then edited to increase smoothness and perceptual uniformity.

Let's look at this example of a Bézier bilinear patch approximating and interpolating an example bivariate chloropleth colormap (source: https://cartographicperspectives.org/index.php/journal/article/view/1538/1819). We can approximate a zero-torsion bilinear patch for this bivaraiate colormap by having the four control points be `[[0, 0.5, 1], [0, 0, 0]], [[1, 1, 1], [1, 0.5, 0]]`.

<img src="figures/bivariate_map.jpg" width="100%"><img src="figures/bivariate_choropleth.png" width="100%">

The bivariate colormap above is a low-torsion bilinear patch in RGB space. Below are the six possible bilinear patches that have maximum torsion (and therefore the most comprehensive color ranges within RGB space).

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

<img src="figures/patch_1AB.png" width="100%"><img src="figures/patch_1A.png" width="50%"><img src="figures/patch_1B.png" width="50%">
<img src="figures/patch_2AB.png" width="100%"><img src="figures/patch_2A.png" width="50%"><img src="figures/patch_2B.png" width="50%">
<img src="figures/patch_3AB.png" width="100%"><img src="figures/patch_3A.png" width="50%"><img src="figures/patch_3B.png" width="50%">

Approximating Google's `turbo` colormap with a handful of control points

<img src="figures/turbo_spline_2.png" width="100%">
<img src="figures/turbo_spline_1.png" width="100%">

Celebrity colormaps (`parula`, `viridis`, `turbo`) within the RGB cube
 
<img src="figures/parula_turbo_viridis_1.png" width="100%">
<img src="figures/parula_turbo_viridis_2.png" width="100%">
<img src="figures/sequential_atomic_1.png" width="100%">

Event Horizon Telescope used the `afmhot` colormap to visualize the M87 black hole

<img src="figures/hot.png" width="100%">

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
