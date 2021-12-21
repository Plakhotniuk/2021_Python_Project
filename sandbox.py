import itertools as it
import numpy as np

masses = np.array([100, 123])
coordinates = np.array([[1, 2, 3], [5, 4, 1]])

mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))
print(masses.reshape((1, -1, 1)), masses.reshape((-1, 1, 1)))
# print(mass_matrix)
displacements = coordinates.reshape((1, -1, 3)) - coordinates.reshape((-1, 1, 3))
print(displacements)
distances = np.linalg.norm(displacements, axis=2)
distances[distances == 0] = 0.001
# print(distances)
forces = displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
# print(forces)
accelerations = forces.sum(axis=1) / masses.reshape(-1, 1)
print(accelerations)

print("========================")

# masses = np.array([100, 123])
# coordinates = np.array([[-1, -2, -3], [5, 4, 1]])
#
# mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))
# # print(mass_matrix)
# displacements = coordinates.reshape((1, -1, 3)) - coordinates.reshape((-1, 1, 3))
# # print(displacements)
# distances = np.linalg.norm(displacements, axis=2)
# distances[distances == 0] = 0.001
# # print(distances)
# forces = displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
# # print(forces)
# accelerations = forces.sum(axis=1) / masses.reshape(-1, 1)
# print(accelerations)
#
# print("========================")
#
# masses = np.array([100, 123])
# coordinates = np.array([[-1, -2, 3], [-5, -4, -1]])
#
# mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))
# # print(mass_matrix)
# displacements = coordinates.reshape((1, -1, 3)) - coordinates.reshape((-1, 1, 3))
# # print(displacements)
# distances = np.linalg.norm(displacements, axis=2)
# distances[distances == 0] = 0.001
# # print(distances)
# forces = displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
# # print(forces)
# accelerations = forces.sum(axis=1) / masses.reshape(-1, 1)
# print(accelerations)
#
# print("========================")
#
# masses = np.array([100, 123])
# coordinates = np.array([[-1, -2, -3], [-5, -4, -1]])
#
# mass_matrix = masses.reshape((1, -1, 1)) * masses.reshape((-1, 1, 1))
# # print(mass_matrix)
# displacements = coordinates.reshape((1, -1, 3)) - coordinates.reshape((-1, 1, 3))
# # print(displacements)
# distances = np.linalg.norm(displacements, axis=2)
# distances[distances == 0] = 0.001
# # print(distances)
# forces = displacements * mass_matrix / np.expand_dims(distances, 2) ** 3
# # print(forces)
# accelerations = forces.sum(axis=1) / masses.reshape(-1, 1)
# print(accelerations)
