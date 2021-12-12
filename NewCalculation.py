import numpy as np
from numpy import linalg
from pyquaternion import Quaternion


G = 6.674E-11
M = 1.989E30
a  = G*M
class Calculation:
    def __init__(self, space_objs, dt):
        self.space_objs = space_objs
        self.dt = dt

    def recalculate_quaternion(self):
        for obj in self.space_objs:
            angle = linalg.norm(obj.angle_velocity) * self.dt
            obj.quaternion *= Quaternion(axis=obj.angle_velocity, angle=angle)
            print(obj.quaternion)

    def recalculate_accelerations(self):
        for obj in self.space_objs:
            for i in range(3):
                obj.mass_center_coordinates_velocity[6 + i] = \
                    - a * (obj.mass_center_coordinates_velocity[i]) /\
                    (np.linalg.norm(obj.mass_center_coordinates_velocity[:3]))**3

    def recalculate_mass_center_coordinates(self):
        for obj in self.space_objs:
            self.recalculate_accelerations()
            obj.mass_center_coordinates_velocity[3:6] +=\
                obj.mass_center_coordinates_velocity[6:9] * self.dt
            obj.mass_center_coordinates_velocity[:3] +=\
                obj.mass_center_coordinates_velocity[3:6] * self.dt
