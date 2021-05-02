import numpy as np

G = -6.67E-11


class f:
    def __init__(self, dt):
        pass

    def __call__(self, t_n, x_n, y_n):
        return y_n

    def __add__(self):
        pass


class g:
    def __init__(self, dt):
        self.mass = []
        self.dt = dt

    def set_mass(self, masss: list):
        self.mass = masss

    def __call__(self, t_n, x_n, y_n):
        return np.array([*(CalcGForce(x_n[0], x_n[1], x_n[2], x_n[3], self.mass[1]) + CalcGForce(x_n[0], x_n[1], x_n[4],x_n[5], self.mass[2])),
                         *(CalcGForce(x_n[2], x_n[3], x_n[0], x_n[1], self.mass[0]) + CalcGForce(x_n[2], x_n[3], x_n[4],x_n[5], self.mass[2])),
                         *(CalcGForce(x_n[4], x_n[5], x_n[0], x_n[1], self.mass[0]) + CalcGForce(x_n[4], x_n[5], x_n[2],x_n[3], self.mass[1]))])

    def __add__(self):
        pass


def CalcGForce(x1, y1, x2, y2, mass):
    return np.array([G * mass * (x1 - x2) / ((np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3),
            G * mass * (y1 - y2) / ((np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3)])


def RungeKutt(t_n, x_n, vx_n, f, g, t):
    k1 = f(t_n, x_n, vx_n)
    m1 = g(t_n, x_n, vx_n)
    k2 = f(t_n + (t / 2), x_n + (t / 2) * k1, vx_n + (t / 2) * m1)
    m2 = g(t_n + (t / 2), x_n + (t / 2) * k1, vx_n + (t / 2) * m1)
    k3 = f(t_n + (t / 2), x_n + (t / 2) * k2, vx_n + (t / 2) * m2)
    m3 = g(t_n + (t / 2), x_n + (t / 2) * k2, vx_n + (t / 2) * m2)
    k4 = f(t_n + t, x_n + t * k3, vx_n + t * m3)
    m4 = g(t_n + t, x_n + t * k3, vx_n + t * m3)

    x = x_n + (t / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    vx = vx_n + (t / 6) * (m1 + 2 * m2 + 2 * m3 + m4)

    return x, vx


def DormPrise(t_n, x_n, vx_n, f, g, t):
    k1 = f(t_n, x_n, vx_n)
    m1 = g(t_n, x_n, vx_n)

    k2 = f(t_n + (t / 5), x_n + (t / 5) * k1, vx_n + (t / 5) * m1)
    m2 = g(t_n + (t / 5), x_n + (t / 5) * k1, vx_n + (t / 5) * m1)

    k3 = f(t_n + t * (3 / 5), x_n + t * (3 / 40) * k1 + t * (9 / 40) * k2, vx_n + t * (3 / 40) * m1 + t * (9 / 40) * m2)
    m3 = g(t_n + t * (3 / 5), x_n + t * (3 / 40) * k1 + t * (9 / 40) * k2, vx_n + t * (3 / 40) * m1 + t * (9 / 40) * m2)

    k4 = f(t_n + t * (4 / 5), x_n + t * (44 / 45) * k1 + t * (-56 / 15) * k2 + t * (32 / 9) * k3,
           vx_n + t * (44 / 45) * m1 + t * (-56 / 15) * m2 + t * (32 / 9) * m3)
    m4 = g(t_n + t * (4 / 5), x_n + t * (44 / 45) * k1 + t * (-56 / 15) * k2 + t * (32 / 9) * k3,
           vx_n + t * (44 / 45) * m1 + t * (-56 / 15) * m2 + t * (32 / 9) * m3)

    k5 = f(t_n + t * (8 / 9),
           x_n + t * (19372 / 6561) * k1 + t * (-25360 / 2187) * k2 + t * (64448 / 6561) * k3 + t * (-212 / 729) * k4,
           vx_n + t * (19372 / 6561) * m1 + t * (-25360 / 2187) * m2 + t * (64448 / 6561) * m3 + t * (-212 / 729) * m4)
    m5 = g(t_n + t * (8 / 9),
           x_n + t * (19372 / 6561) * k1 + t * (-25360 / 2187) * k2 + t * (64448 / 6561) * k3 + t * (-212 / 729) * k4,
           vx_n + t * (19372 / 6561) * m1 + t * (-25360 / 2187) * m2 + t * (64448 / 6561) * m3 + t * (-212 / 729) * m4)

    k6 = f(t_n + t,
           x_n + t * (9017 / 3168) * k1 + t * (-355 / 33) * k2 + t * (46732 / 5247) * k3 + t * (49 / 176) * k4 + t * (
                       -5103 / 18656) * k5,
           vx_n + t * (9017 / 3168) * m1 + t * (-355 / 33) * m2 + t * (46732 / 5247) * m3 + t * (49 / 176) * m4 + t * (
                       -5103 / 18656) * m5)
    m6 = g(t_n + t,
           x_n + t * (9017 / 3168) * k1 + t * (-355 / 33) * k2 + t * (46732 / 5247) * k3 + t * (49 / 176) * k4 + t * (
                       -5103 / 18656) * k5,
           vx_n + t * (9017 / 3168) * m1 + t * (-355 / 33) * m2 + t * (46732 / 5247) * m3 + t * (49 / 176) * m4 + t * (
                       -5103 / 18656) * m5)

    k7 = f(t_n + t, x_n + t * (35 / 384) * k1 + t * 0 * k2 + t * (500 / 1113) * k3 + t * (125 / 192) * k4 + t * (
                -2187 / 6784) * k5 + t * (11 / 84) * k6,
           vx_n + t * (35 / 384) * m1 + t * 0 * m2 + t * (500 / 1113) * m3 + t * (125 / 192) * m4 + t * (
                       -2187 / 6784) * m5 + t * (11 / 84) * m6)
    m7 = g(t_n + t, x_n + t * (35 / 384) * k1 + t * 0 * k2 + t * (500 / 1113) * k3 + t * (125 / 192) * k4 + t * (
                -2187 / 6784) * k5 + t * (11 / 84) * k6,
           vx_n + t * (35 / 384) * m1 + t * 0 * m2 + t * (500 / 1113) * m3 + t * (125 / 192) * m4 + t * (
                       -2187 / 6784) * m5 + t * (11 / 84) * m6)

    x1 = x_n + t * ((35 / 384) * k1 + (0) * k2 + (500 / 1113) * k3 + (125 / 192) * k4 + (-2187 / 6784) * k5 + (
                11 / 84) * k6 + (0) * k7)
    vx1 = vx_n + t * ((35 / 384) * m1 + (0) * m2 + (500 / 1113) * m3 + (125 / 192) * m4 + (-2187 / 6784) * m5 + (
                11 / 84) * m6 + (0) * m7)

    x2 = x_n + t * ((5179 / 57600) * k1 + (7571 / 16695) * k3 + (393 / 640) * k4 + (-92097 / 339200) * k5 + (
                187 / 2100) * k6 + (1 / 40) * k7)
    vx2 = vx_n + t * ((5179 / 57600) * m1 + (7571 / 16695) * m3 + (393 / 640) * m4 + (-92097 / 339200) * m5 + (
                187 / 2100) * m6 + (1 / 40) * m7)

    if abs(x1[0] - x2[0]) < 0.0005:
        g.dt = g.dt * 2
    else:
        g.dt = g.dt / 2

    print(g.dt)

    return x1, vx1


def count_pos(x, v, f, g):
    nx, nv = RungeKutt(0, x, v, f, g, g.dt)
    return nx, nv


if __name__ == "__main__":
    print("This module is not for direct call!")
