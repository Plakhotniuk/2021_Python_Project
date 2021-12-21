from PyQt5.QtWidgets import QApplication, QDesktopWidget
import sys
from MainWindow import StartWindow
from Globals import Globals
from space_classes import CelestialBody, np, Quaternion
G = 6.674E-11
if __name__ == '__main__':
    App = QApplication(sys.argv)
    Globals.DESKTOP_SIZE = QDesktopWidget().screenGeometry()
    space_objects = [
        CelestialBody(name='Cone', dimentions=np.array([5.0E6, 0, 1.0E8, 1.0E3, 10], dtype=int),
                                   color=Globals.RED, angle_velocity=np.array([0.0, 0.0, 0.0]),
                                   mass_center_coordinates_velocity=np.array([0, 0, 5.0E7, -1.0E6, 0, 0, 0, 0, 0]),
                                   quaternion=Quaternion(0, 1, 0.0, 0.0), mass=1.0E30 * G),
                     CelestialBody(name='Cone', color=Globals.GREEN, angle_velocity=np.array([0.01, 0.02, 0.03]),
                                   dimentions=np.array([5.0E6, 0, 1.0E8, 1.0E3, 10], dtype=int),
                                   mass_center_coordinates_velocity=np.array([0, 5.0E7, -5.0E7, 0, 0, 1.0E5, 0, 0, 0]),
                                   quaternion=Quaternion(0, 0.7, 1, 0), mass=1.0E30 * G),
                     CelestialBody(name='Cone', color=Globals.BLUE, angle_velocity=np.array([0.01, 0.02, 0.03]),
                                   dimentions=np.array([5.0E6, 0, 1.0E8, 1.0E3, 10], dtype=int),
                                   mass_center_coordinates_velocity=np.array([5.0E7, 0, 5.0E7, 1.0E6, 0, -1.0E5, 0, 0, 0]),
                                   quaternion=Quaternion(1, 1, 1, 1), mass=1.0E30 * G),
                     CelestialBody(name='Cylinder', color=Globals.CYAN, angle_velocity=np.array([0.01, 0.02, 0.03]),
                                   dimentions=np.array([5.0E6, 5.0E6, 1.0E8, 1.0E3, 10], dtype=int),
                                   mass_center_coordinates_velocity=np.array(
                                       [-5.0E7, 0, 5.0E7, 0, 0, 0, 0, 0, 0]),
                                   quaternion=Quaternion(0.25, 0, 1, 0), mass=1.0E25 * G),
                     CelestialBody(name='Sphere', color=Globals.CYAN, angle_velocity=np.array([0.0, 0.0, 0.01]),
                                   dimentions=np.array([5.0E6, 1.0E3, 10], dtype=int),
                                   mass_center_coordinates_velocity=np.array(
                                       [5.0E7, 0, -5.0E7, 0, 0, 0, 0, 0, 0]),
                                   quaternion=Quaternion(0, 1, 0, 0), mass=1.0E50 * G)
                     ]
    window = StartWindow(space_objects)
    sys.exit(App.exec())
