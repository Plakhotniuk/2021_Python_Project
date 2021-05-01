import numpy as np
G = -6.67E-11


class f:
    def __init__(self, dt):
        self.dt = dt

    def __call__(self, t_n, x_n, y_n):
        return y_n

    def __add__(self):
        pass


class g:
    def __init__(self, dt):
        self.mass = []
        self.dt = dt

    def set_mass(self,  masss: list):
        self.mass = masss

    def __call__(self, t_n, x_n, y_n):
        return np.array([(G * self.mass[0] * (x_n[0] - x_n[2]) / ((np.sqrt((x_n[0]-x_n[2])**2 + (x_n[1]-x_n[3])**2)) ** 3)),
                         (G * self.mass[0] * (x_n[1] - x_n[3]) / ((np.sqrt((x_n[0]-x_n[2])**2 + (x_n[1]-x_n[3])**2)) ** 3)),
                         (G * self.mass[1] * ((-1)*x_n[0] + x_n[2]) / ((np.sqrt((x_n[0] - x_n[2]) ** 2 + (x_n[1] - x_n[3]) ** 2)) ** 3)),
                         (G * self.mass[1] * ((-1)*x_n[1] + x_n[3])) / ((np.sqrt((x_n[0] - x_n[2]) ** 2 + (x_n[1] - x_n[3]) ** 2)) ** 3)])

    def __add__(self):
        pass


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


def count_pos(x, v, f, g):
    nx, nv = RungeKutt(0, x, v, f, g, g.dt)
    return nx, nv
