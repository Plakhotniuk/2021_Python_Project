import numpy as np
from math import cos, sin, pi

G = -6.67E-11


class function_f:
    def __init__(self):
        pass

    def __call__(self, t_n, x_n, vx_n):
        return vx_n

    def __add__(self):
        pass


class function_g:
    def __init__(self, sp_obj: list):
        self.mass = []
        self.space_objects = sp_obj
        for i in range(len(self.space_objects)):
            self.mass.append(self.space_objects[i].m)
        self.index_of_starship = 0

    def __call__(self, t_n, x_n, vx_n):
        return np.array([*self.calc_forces_on_starship(0, x_n), *self.calc_all_gforces(1, x_n),
                         *self.calc_all_gforces(2, x_n), *self.calc_all_gforces(3, x_n)])

    def __add__(self):
        pass

    def calc_gforce(self, x1, y1, x2, y2, mass):
        return np.array([G * mass * (x1 - x2) / ((np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3),
                         G * mass * (y1 - y2) / ((np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 3)])

    def calc_all_gforces(self, ind, x_n):
        result = np.array([0.0, 0.0])
        for i in range(x_n.size // 2):
            if i != ind:
                result = result + self.calc_gforce(x_n[2 * ind], x_n[2 * ind + 1], x_n[2 * i], x_n[2 * i + 1],
                                                   self.mass[i])
        return result

    def calc_forces_on_starship(self, ind, x_n):
        result = self.calc_all_gforces(ind, x_n)
        if self.space_objects[self.index_of_starship].time_engine_working > 0:
            result = result + np.array([self.space_objects[self.index_of_starship].engine_thrust * cos(
                self.space_objects[self.index_of_starship].engine_angle) / self.mass[self.index_of_starship],
                                        self.space_objects[self.index_of_starship].engine_thrust * sin(
                                            self.space_objects[self.index_of_starship].engine_angle) / self.mass[
                                            self.index_of_starship]])
        return result


class Calculation:
    def __init__(self, space_obj, dt):
        self.f = function_f()
        self.g = function_g(space_obj)
        self.dt = dt
        self.time_of_count = 0
        self.x = np.array([])  # координаты всех объектов системы подряд
        self.v = np.array([])  # скорости всех объектов системы подряд
        self.set_actual_params_of_system()

    def set_actual_params_of_system(self):
        x = []
        v = []
        for body in self.g.space_objects:
            x.append(body.x)
            x.append(body.y)
            v.append(body.vx)
            v.append(body.vy)
        self.x = np.array(x)  # координаты всех объектов системы подряд
        self.v = np.array(v)

    def runge_kutta(self, t_n, x_n, vx_n):
        k1 = self.f(t_n, x_n, vx_n)
        m1 = self.g(t_n, x_n, vx_n)
        k2 = self.f(t_n + (self.dt / 2), x_n + (self.dt / 2) * k1, vx_n + (self.dt / 2) * m1)
        m2 = self.g(t_n + (self.dt / 2), x_n + (self.dt / 2) * k1, vx_n + (self.dt / 2) * m1)
        k3 = self.f(t_n + (self.dt / 2), x_n + (self.dt / 2) * k2, vx_n + (self.dt / 2) * m2)
        m3 = self.g(t_n + (self.dt / 2), x_n + (self.dt / 2) * k2, vx_n + (self.dt / 2) * m2)
        k4 = self.f(t_n + self.dt, x_n + self.dt * k3, vx_n + self.dt * m3)
        m4 = self.g(t_n + self.dt, x_n + self.dt * k3, vx_n + self.dt * m3)

        x = x_n + (self.dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        vx = vx_n + (self.dt / 6) * (m1 + 2 * m2 + 2 * m3 + m4)

        return x, vx

    def dorm_prise(self, t_n, x_n, vx_n):
        k1 = self.f(t_n, x_n, vx_n)
        m1 = self.g(t_n, x_n, vx_n)

        k2 = self.f(t_n + (self.dt / 5), x_n + (self.dt / 5) * k1, vx_n + (self.dt / 5) * m1)
        m2 = self.g(t_n + (self.dt / 5), x_n + (self.dt / 5) * k1, vx_n + (self.dt / 5) * m1)

        k3 = self.f(t_n + self.dt * (3 / 5), x_n + self.dt * (3 / 40) * k1 + self.dt * (9 / 40) * k2,
                    vx_n + self.dt * (3 / 40) * m1 + self.dt * (9 / 40) * m2)
        m3 = self.g(t_n + self.dt * (3 / 5), x_n + self.dt * (3 / 40) * k1 + self.dt * (9 / 40) * k2,
                    vx_n + self.dt * (3 / 40) * m1 + self.dt * (9 / 40) * m2)

        k4 = self.f(t_n + self.dt * (4 / 5),
                    x_n + self.dt * (44 / 45) * k1 + self.dt * (-56 / 15) * k2 + self.dt * (32 / 9) * k3,
                    vx_n + self.dt * (44 / 45) * m1 + self.dt * (-56 / 15) * m2 + self.dt * (32 / 9) * m3)
        m4 = self.g(t_n + self.dt * (4 / 5),
                    x_n + self.dt * (44 / 45) * k1 + self.dt * (-56 / 15) * k2 + self.dt * (32 / 9) * k3,
                    vx_n + self.dt * (44 / 45) * m1 + self.dt * (-56 / 15) * m2 + self.dt * (32 / 9) * m3)

        k5 = self.f(t_n + self.dt * (8 / 9),
                    x_n + self.dt * (19372 / 6561) * k1 + self.dt * (-25360 / 2187) * k2 + self.dt * (
                            64448 / 6561) * k3 + self.dt * (-212 / 729) * k4,
                    vx_n + self.dt * (19372 / 6561) * m1 + self.dt * (-25360 / 2187) * m2 + self.dt * (
                            64448 / 6561) * m3 + self.dt * (-212 / 729) * m4)
        m5 = self.g(t_n + self.dt * (8 / 9),
                    x_n + self.dt * (19372 / 6561) * k1 + self.dt * (-25360 / 2187) * k2 + self.dt * (
                            64448 / 6561) * k3 + self.dt * (-212 / 729) * k4,
                    vx_n + self.dt * (19372 / 6561) * m1 + self.dt * (-25360 / 2187) * m2 + self.dt * (
                            64448 / 6561) * m3 + self.dt * (-212 / 729) * m4)

        k6 = self.f(t_n + self.dt,
                    x_n + self.dt * (9017 / 3168) * k1 + self.dt * (-355 / 33) * k2 + self.dt * (
                            46732 / 5247) * k3 + self.dt * (49 / 176) * k4 + self.dt * (
                            -5103 / 18656) * k5,
                    vx_n + self.dt * (9017 / 3168) * m1 + self.dt * (-355 / 33) * m2 + self.dt * (
                            46732 / 5247) * m3 + self.dt * (49 / 176) * m4 + self.dt * (
                            -5103 / 18656) * m5)
        m6 = self.g(t_n + self.dt,
                    x_n + self.dt * (9017 / 3168) * k1 + self.dt * (-355 / 33) * k2 + self.dt * (
                            46732 / 5247) * k3 + self.dt * (49 / 176) * k4 + self.dt * (
                            -5103 / 18656) * k5,
                    vx_n + self.dt * (9017 / 3168) * m1 + self.dt * (-355 / 33) * m2 + self.dt * (
                            46732 / 5247) * m3 + self.dt * (49 / 176) * m4 + self.dt * (
                            -5103 / 18656) * m5)

        k7 = self.f(t_n + self.dt,
                    x_n + self.dt * (35 / 384) * k1 + self.dt * 0 * k2 + self.dt * (500 / 1113) * k3 + self.dt * (
                            125 / 192) * k4 + self.dt * (
                            -2187 / 6784) * k5 + self.dt * (11 / 84) * k6,
                    vx_n + self.dt * (35 / 384) * m1 + self.dt * 0 * m2 + self.dt * (500 / 1113) * m3 + self.dt * (
                            125 / 192) * m4 + self.dt * (
                            -2187 / 6784) * m5 + self.dt * (11 / 84) * m6)
        m7 = self.g(t_n + self.dt,
                    x_n + self.dt * (35 / 384) * k1 + self.dt * 0 * k2 + self.dt * (500 / 1113) * k3 + self.dt * (
                            125 / 192) * k4 + self.dt * (
                            -2187 / 6784) * k5 + self.dt * (11 / 84) * k6,
                    vx_n + self.dt * (35 / 384) * m1 + self.dt * 0 * m2 + self.dt * (500 / 1113) * m3 + self.dt * (
                            125 / 192) * m4 + self.dt * (
                            -2187 / 6784) * m5 + self.dt * (11 / 84) * m6)

        x1 = x_n + self.dt * ((35 / 384) * k1 + 0 * k2 + (500 / 1113) * k3 + (125 / 192) * k4 + (-2187 / 6784) * k5 + (
                11 / 84) * k6 + 0 * k7)
        vx1 = vx_n + self.dt * (
                (35 / 384) * m1 + 0 * m2 + (500 / 1113) * m3 + (125 / 192) * m4 + (-2187 / 6784) * m5 + (11 / 84) *
                m6 + 0 * m7)

        x2 = x_n + self.dt * ((5179 / 57600) * k1 + (7571 / 16695) * k3 + (393 / 640) * k4 + (-92097 / 339200) * k5 + (
                187 / 2100) * k6 + (1 / 40) * k7)
        vx2 = vx_n + self.dt * (
                (5179 / 57600) * m1 + (7571 / 16695) * m3 + (393 / 640) * m4 + (-92097 / 339200) * m5 + (187 / 2100) *
                m6 + (1 / 40) * m7)

        if abs(x1[0] - x2[0]) > 0.0005:
            self.dt = self.dt / 2
        elif abs(x1[2] - x2[2]) > 0.0005:
            self.dt = self.dt / 2
        elif abs(x1[4] - x2[4]) > 0.0005:
            self.dt = self.dt / 2
        elif abs(x1[6] - x2[6]) > 0.0005:
            self.dt = self.dt / 2
        else:
            self.dt = self.dt * 2

        if self.dt > 100:
            self.dt = 100
        return x1, vx1

    def eiler(self, t_n, x_n, vx_n):
        x = x_n + self.dt * self.f(t_n, x_n, vx_n)
        vx = vx_n + self.dt * self.g(t_n, x_n, vx_n)

        return x, vx

    def count_pos(self):
        nx = self.x
        nv = self.v
        if self.dt > self.g.space_objects[self.g.index_of_starship].time_engine_working:
            self.dt = self.g.space_objects[self.g.index_of_starship].time_engine_working
            nx, nv = self.dorm_prise(0, nx, nv)
            self.time_of_count += self.dt
            self.g.space_objects[self.g.index_of_starship].time_engine_working = 0
            self.dt = 100

        while self.time_of_count < 300:
            nx, nv = self.dorm_prise(0, nx, nv)
            self.time_of_count += self.dt

        if self.g.space_objects[0].time_engine_working > self.time_of_count:
            self.g.space_objects[self.g.index_of_starship].time_engine_working -= self.time_of_count
            self.time_of_count = self.time_of_count - 300  # либо тут поменять

        if 0 < self.g.space_objects[0].time_engine_working < self.time_of_count:
            self.dt = self.g.space_objects[0].time_engine_working
            self.x, self.v = self.dorm_prise(0, nx, nv)
            self.time_of_count = self.dt + self.time_of_count - 300
            self.dt = 100
            self.g.space_objects[self.g.index_of_starship].time_engine_working = 0  # либо тут поменять

        else:
            self.time_of_count = self.time_of_count - 300
            self.x = nx
            self.v = nv

        return nx, nv
        # ATTENTION
        # если обнаружится какая-то мегаприколденая ошибка с
        # отрисовкой планет - это скорее всего здесь из-за счета времени

    def recalculate_space_objects_positions(self):
        """
        Пересчитывает координаты объектов.
        param: space_objects — список оьъектов, для которых нужно пересчитать координаты
        """
        new_x, new_v = self.count_pos()
        i = 0
        for body in self.g.space_objects:
            body.x = new_x[i]
            body.y = new_x[i + 1]
            body.vx = new_v[i]
            body.vy = new_v[i + 1]
            i += 2

    def calculate_prev_trajectory(self, time):
        """
        Предрасчёт траектори на время time
        """
        x = []
        self.dt = 100
        time_of_calcs = 0

        nx = self.x
        nv = self.v
        if self.dt > self.g.space_objects[self.g.index_of_starship].time_engine_working:
            self.dt = self.g.space_objects[self.g.index_of_starship].time_engine_working
            nx, nv = self.runge_kutta(0, nx, nv)
            x.append(nx)
            time_of_calcs += self.dt
            self.g.space_objects[self.g.index_of_starship].time_engine_working = 0
            self.dt = 100

        while time_of_calcs < time:
            nx, nv = self.runge_kutta(0, nx, nv)
            time_of_calcs += self.dt
            x.append(nx)
            self.dt = 100

            if self.g.space_objects[0].time_engine_working >= 100:
                self.g.space_objects[self.g.index_of_starship].time_engine_working -= self.dt
            if 0 < self.g.space_objects[0].time_engine_working < 100:
                self.dt = self.g.space_objects[0].time_engine_working
                time_of_calcs += self.dt
                nx, nv = self.runge_kutta(0, nx, nv)
                x.append(nx)
                self.dt = 100
                self.g.space_objects[0].time_engine_working = 0

        self.dt = 100

        # нужно закомментить этот кусок кода, чтобы планетки не перемещались после нажатия calculate
        ######################################################################################
        i = 0
        for body in self.g.space_objects:
            body.x = nx[i]
            body.y = nx[i + 1]
            body.vx = nv[i]
            body.vy = nv[i + 1]
            i += 2
        print(np.sqrt(nv[0] ** 2 + nv[1] ** 2))
        ########################################################################################
        return np.array(x)


if __name__ == "__main__":
    print("This module is not for direct call!")
