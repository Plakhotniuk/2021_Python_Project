import numpy as np
from numpy import linalg
from pyquaternion import Quaternion
from scipy.integrate import odeint

T = 0
G = 6.674E-11
M = 1.989E30
mu = G * M
sqrt_mu = np.sqrt(mu)


def dr_dt(y, t):
    """Integration of the governing vector differential equation.
    d2r_dt2 = -(mu/R^3)*r with d2r_dt2 and r as vecotrs.
    Initial position and velocity are given.
    y[0:2] = position components
    y[3:] = velocity components"""

    r = np.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)

    dy0 = y[3]
    dy1 = y[4]
    dy2 = y[5]
    dy3 = -(mu / (r ** 3)) * y[0]
    dy4 = -(mu / (r ** 3)) * y[1]
    dy5 = -(mu / (r ** 3)) * y[2]
    return [dy0, dy1, dy2, dy3, dy4, dy5]


class Calculation:
    def __init__(self, space_objs, dt):
        self.space_objs = space_objs
        self.dt = dt
        self.trajectory = self.calculate_trajectory()

    def recalculate_quaternion(self):
        for obj in self.space_objs:
            angle = linalg.norm(obj.angle_velocity) * self.dt
            obj.quaternion *= Quaternion(axis=obj.angle_velocity, angle=angle)
            print(obj.quaternion)

    def calculate_trajectory(self):
        t = np.arange(0, 100000, 0.1)
        result = []
        for obj in self.space_objs:
            y0 = obj.initials[:6]
            result.append(odeint(dr_dt, y0, t))
        print(len(result), result)
        return result

    def recalculate_accelerations(self):
        for obj in self.space_objs:
            obj.mass_center_coordinates_velocity[6:] = \
                - mu * (obj.mass_center_coordinates_velocity[:3]) / \
                (np.linalg.norm(obj.mass_center_coordinates_velocity[:3])) ** 3

    def recalculate_mass_center_coordinates(self):
        global T
        for i in range(len(self.space_objs)):
            self.space_objs[i].mass_center_coordinates_velocity[:6] = self.trajectory[i][T]
        T += 1
        # global T
        # T += self.dt
        #
        # for obj in self.space_objs:
        #     self.recalculate_accelerations()
        #     obj.mass_center_coordinates_velocity[3:6] +=\
        #         obj.mass_center_coordinates_velocity[6:9] * self.dt
        #     obj.mass_center_coordinates_velocity[:3] +=\
        #         obj.mass_center_coordinates_velocity[3:6] * self.dt
