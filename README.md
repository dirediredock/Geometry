# RGB_ColorSpline_Cube

Defining colormaps Bézier surfaces has a lot of benefits. First, minimal data storage, because you only save the coordinates of the control points. Second, the are altready parametrized, so rate of change within the colormap will be perceptually uniform. Third, manually-crafted colormaps can be approximated (and therefore perceptually improved) with this method.


<img src="figures/sequential_atomic_2.png" width="50%"><img src="figures/RGB_skew_atomic.png" width="50%">

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
<img src="figures/patch_1A.png" width="100%">
<img src="figures/patch_1B.png" width="100%">
<img src="figures/patch_1AB.png" width="100%">

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

<img src="figures/patch_2A.png" width="100%">
<img src="figures/patch_2B.png" width="100%">
<img src="figures/patch_2AB.png" width="100%">

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

<img src="figures/patch_3A.png" width="100%">
<img src="figures/patch_3B.png" width="100%">
<img src="figures/patch_3AB.png" width="100%">

<img src="figures/random_patch.png" width="100%">
<img src="figures/cone.png" width="100%">

Event Horizon Telescope used the `afmhot` colormap to visualize the M87 black hole

<img src="figures/hot.png" width="100%">
<img src="figures/turbo_spline_2.png" width="100%">
<img src="figures/turbo_spline_1.png" width="100%">

Bivariate chloropleth colormap and RGB bilinear patch

<img src="figures/bivariate_map.jpg" width="100%">
<img src="figures/bivariate.png" width="100%">

<img src="figures/parula_turbo_viridis_1.png" width="100%">
<img src="figures/parula_turbo_viridis_2.png" width="100%">
<img src="figures/sequential_atomic_1.png" width="100%">

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
