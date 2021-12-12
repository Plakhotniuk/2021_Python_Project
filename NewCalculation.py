import numpy as np
from numpy import linalg
from pyquaternion import Quaternion
from scipy import integrate

G = 6.674E-11
M = 1.989E30
mu = G * M


class Calculation:
    def __init__(self, space_objs, dt):
        self.space_objs = space_objs
        self.dt = dt
        self.moment = np.array([])

    def recalculate_quaternion(self):
        self.calculate_moment_forces()
        for obj in self.space_objs:
            angle = linalg.norm(obj.angle_velocity) * self.dt
            obj.quaternion *= Quaternion(axis=obj.angle_velocity, angle=angle)
            # print(obj.quaternion)

    def recalculate_accelerations(self):
        for obj in self.space_objs:
            obj.mass_center_coordinates_velocity[6:] = \
                - mu * (obj.mass_center_coordinates_velocity[:3]) / \
                (np.linalg.norm(obj.mass_center_coordinates_velocity[:3])) ** 3

    def recalculate_mass_center_coordinates(self):
        for obj in self.space_objs:
            self.recalculate_accelerations()
            obj.mass_center_coordinates_velocity[3:6] +=\
                obj.mass_center_coordinates_velocity[6:9] * self.dt
            obj.mass_center_coordinates_velocity[:3] +=\
                obj.mass_center_coordinates_velocity[3:6] * self.dt

    def calculate_moment_forces(self):
        for obj in self.space_objs:
            moment = 3 * mu * np.cross((obj.tensor_of_inertia @ obj.mass_center_coordinates_velocity[:3]),
                                       obj.mass_center_coordinates_velocity[:3])\
                     / linalg.norm(obj.mass_center_coordinates_velocity[:3])**5
            kinetic_moment = moment * self.dt
            obj.angle_velocity = np.dot( linalg.inv(obj.tensor_of_inertia),  kinetic_moment)
            print(obj.angle_velocity)
    # def calculate_kinetic_moment(self):



