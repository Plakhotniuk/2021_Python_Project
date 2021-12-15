import numpy as np
from numpy import linalg
from pyquaternion import Quaternion
from scipy.integrate import odeint

T = 0
G = 6.674E-11
M = 1.989E30
mu = G * M
sqrt_mu = np.sqrt(mu)
counter = 0


class Calculation:
    def __init__(self, space_objs, dt):
        self.space_objs = space_objs
        self.parsed_space_objs = self.parsing_into_numpy()
        self.dt = dt
        self.trajectory = self.calculate_trajectory()
        self.moment = np.array([])

    def dr_dt(self, y, t):
        """Integration of the governing vector differential equation.
        d2r_dt2 = -(mu/R^3)*r with d2r_dt2 and r as vecotrs.
        Initial position and velocity are given.
        y[0:2] = position components
        y[3:] = velocity components"""

        differs = np.zeros(6)

        differs[:3] = y[3:6]
        differs[3:] = self.calculate_accelerations()[counter]
        return differs

    def recalculate_quaternion(self):
        self.calculate_moment_forces()
        for obj in self.space_objs:
            angle = linalg.norm(obj.angle_velocity) * self.dt
            obj.quaternion *= Quaternion(axis=obj.angle_velocity, angle=angle)

    def parsing_into_numpy(self):
        result = []
        for obj in self.space_objs:
            # mass_center - 0:9
            # angle - 9:12
            # initials - 12:21
            # quaternion - 21:25
            # tensor - 25:34
            # mass - 35

            result.append(np.concatenate((obj.mass_center_coordinates_velocity, obj.angle_velocity, obj.initials,
                                          [obj.quaternion.scalar], obj.quaternion.vector,
                                          obj.tensor_of_inertia.ravel(), [obj.mass]), axis=0))
        return np.array(result)

    def calculate_accelerations(self):
        mass_matrix = self.parsed_space_objs[:, 34].reshape((1, -1, 1)) * \
                      self.parsed_space_objs[:, 34].reshape((-1, 1, 1))
        displacements = self.parsed_space_objs[:, :3].reshape((1, -1, 3)) - \
                        self.parsed_space_objs[:, :3].reshape((-1, 1, 3))
        distances = np.linalg.norm(displacements, axis=2)
        distances[distances == 0] = 0.001  # avoid divide by zero
        forces = G * displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
        return forces.sum(axis=1) / self.parsed_space_objs[:, 34].reshape(-1, 1)

    def calculate_trajectory(self):
        global counter
        t = np.arange(0, 100000, self.dt)
        result = []
        # for obj in self.space_objs:
        #     y0 = obj.initials[:6]
        #     result.append(odeint(dr_dt, y0, t))
        y0 = self.parsed_space_objs[:, 12:18]
        for Y0 in y0:
            result.append(odeint(self.dr_dt, Y0, t))
            counter += 1
        counter = 0
        return np.array(result)

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

    def calculate_moment_forces(self):
        for obj in self.space_objs:
            moment = 3 * mu * np.cross((obj.tensor_of_inertia @ obj.mass_center_coordinates_velocity[:3]),
                                       obj.mass_center_coordinates_velocity[:3])\
                     / linalg.norm(obj.mass_center_coordinates_velocity[:3])**5
            kinetic_moment = moment * self.dt
            obj.angle_velocity = np.dot( linalg.inv(obj.tensor_of_inertia),  kinetic_moment)
            print(obj.angle_velocity)
    # def calculate_kinetic_moment(self):
