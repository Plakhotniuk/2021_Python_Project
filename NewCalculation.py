import numpy as np
from numpy import linalg
from pyquaternion import Quaternion
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

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
        self.time = 0
        # self.trajectory = self.calculate_trajectory()
        self.trajectory = []
        self.moment = np.array([])

    def dr_dt(self, t, y):
        """Integration of the governing vector differential equation.
        d2r_dt2 = -(mu/R^3)*r with d2r_dt2 and r as vecotrs.
        Initial position and velocity are given.
        y[0:2] = position components
        y[3:] = velocity components"""
        y = np.reshape(y, (-1, 6))
        differs = np.zeros((len(y), 6))

        differs[:, :3] = y[:, 3:6]
        differs[:, 3:] = self.calculate_accelerations(y[:, :3])
        return differs.ravel()

        # def d_dt(self):
        #     pass

    def recalculate_quaternion(self):
        for obj1 in self.space_objs:
            external_moment = np.array([0.0, 0.0, 0.0])
            kinetic_moment = np.array([0.0, 0.0, 0.0])
            for obj2 in self.space_objs:
                if linalg.norm(obj2.mass_center_coordinates_velocity[:3] - obj1.mass_center_coordinates_velocity[:3]) != 0:
                    r = obj1.mass_center_coordinates_velocity[:3] - obj2.mass_center_coordinates_velocity[:3]
                    external_moment -= 3 * G * (obj1.mass / linalg.norm(r)**5) * np.cross((obj1.tensor_of_inertia @ r), r) * self.dt
            kinetic_moment += external_moment * self.dt
            obj1.angle_velocity += (linalg.inv(obj1.tensor_of_inertia) @ kinetic_moment) * self.dt
            angle = linalg.norm(obj1.angle_velocity) * self.dt
            obj1.quaternion *= Quaternion(axis=obj1.angle_velocity, angle=angle)

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

    def calculate_accelerations(self, coordinates):
        mass_matrix = self.parsed_space_objs[:, 34].reshape((1, -1, 1)) * \
                      self.parsed_space_objs[:, 34].reshape((-1, 1, 1))
        self.displacements = coordinates.reshape((1, -1, 3)) - coordinates.reshape((-1, 1, 3))
        # print(self.displacements)
        distances = np.linalg.norm(self.displacements, axis=2)
        distances[distances == 0] = 0.001
        forces = G * self.displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
        return forces.sum(axis=1) / self.parsed_space_objs[:, 34].reshape(-1, 1)

    def calculate_trajectory(self, time):
        self.time = time
        t = np.arange(0, self.time, self.dt)
        result = []
        y0 = self.parsed_space_objs[:, 12:18]
        result.append(odeint(self.dr_dt, y0.ravel(), t, tfirst=True))
        self. trajectory = np.array(result)[0]

    def for_calculate_accelerations(self):
        for obj1 in self.space_objs:
            for obj2 in self.space_objs:
                if obj2.mass_center_coordinates_velocity[:3] - obj1.mass_center_coordinates_velocity[:3] != 0:
                    # self.recalculate_angle_velocity(obj1, obj2)
                    obj1.mass_center_coordinates_velocity[6:] += \
                        - G * obj2.mass * (obj2.mass_center_coordinates_velocity[:3] -
                                           obj1.mass_center_coordinates_velocity[:3]) / \
                        (np.linalg.norm(obj2.mass_center_coordinates_velocity[:3] -
                                        obj1.mass_center_coordinates_velocity[:3]) ** 3)

    def recalculate_mass_center_coordinates(self):
        global T
        if len(self.trajectory) - T > 0:
            for i in range(len(self.space_objs)):
                self.space_objs[i].mass_center_coordinates_velocity[:6] = self.trajectory[T, 6 * i:6 * i + 6]
        T += 1

    def calculate_moment_forces(self):
        for obj in self.space_objs:
            moment = 3 * mu * np.cross((obj.tensor_of_inertia @ obj.mass_center_coordinates_velocity[:3]),
                                       obj.mass_center_coordinates_velocity[:3]) \
                     / linalg.norm(obj.mass_center_coordinates_velocity[:3]) ** 5
            kinetic_moment = moment * self.dt
            obj.angle_velocity = np.dot(linalg.inv(obj.tensor_of_inertia), kinetic_moment)

    def recalculate_angle_velocity(self):
        for obj1 in self.space_objs:
            kin_moment = np.array([0, 0, 0])
            for obj2 in self.space_objs:
                if linalg.norm(obj2.mass_center_coordinates_velocity[:3] - obj1.mass_center_coordinates_velocity[:3]) != 0:
                    r = obj1.mass_center_coordinates_velocity[:3] - obj2.mass_center_coordinates_velocity[:3]
                    kin_moment = np.vstack((kin_moment, (obj1.mass / linalg.norm(r)**5) * np.cross((obj1.tensor_of_inertia @ r), r) * self.dt))
            obj1.kinetic_moment += kin_moment.sum(axis=0)
            obj1.angle_velocity += 3 * G * (linalg.inv(obj1.tensor_of_inertia) @ obj1.kinetic_moment) * self.dt
