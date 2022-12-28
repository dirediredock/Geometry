# by Matias I. Bofarull Oddo - 2022.12.23

import numpy as np


def point_De_Casteljau(points, t):
    point_array = [point for point in points]
    for i in range(1, len(point_array)):
        for m in range(len(point_array) - i):
            point_array[m] = point_array[m] * (1 - t) + point_array[m + 1] * t
    return point_array[0]


def subdivision_De_Casteljau(points, t=0.5):
    point_array = [point for point in points]
    for i in range(1, len(point_array)):
        for m in range(len(point_array) - i):
            point_array[m] = point_array[m] * (1 - t) + point_array[m + 1] * t
    return point_array


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def Bernstein(n, k, t):
    return (
        (factorial(n) / ((factorial(k) * factorial(n - k))))
        * (t ** (n - k))
        * ((1 - t) ** k)
    )


def surface_Bezier(control_points, steps_u=80, steps_v=80):
    u = np.linspace(0, 1, steps_u)
    v = np.linspace(0, 1, steps_v)
    points_u, points_v = control_points.shape[:2]
    surface = np.zeros((steps_u, steps_v, 3))
    for i in range(steps_u):
        for j in range(steps_v):
            surface[i, j] = sum(
                Bernstein(points_u - 1, k, u[i])
                * Bernstein(points_v - 1, l, v[j])
                * control_points[k, l]
                for k in range(points_u)
                for l in range(points_v)
            )
    return surface
