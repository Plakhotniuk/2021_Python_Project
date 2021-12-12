import numpy as np
from numpy import linalg
from pyquaternion import Quaternion


class Calculation:
    def __init__(self, space_objs, dt):
        self.space_objs = space_objs
        self.dt = dt

    def recalculate_quaternion(self):
        for obj in self.space_objs:
            angle = linalg.norm(obj.angle_velocity) * self.dt
            obj.quaternion *= Quaternion(axis=obj.angle_velocity, angle=angle)
            print(obj.quaternion)

    def recalculate_mass_center_coordinates(self):
        for obj in self.space_objs:
            obj.mass_center_coordinates_velocity[:3] +=\
                obj.mass_center_coordinates_velocity[3:6] * self.dt
