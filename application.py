from PyQt5.QtWidgets import QApplication, QDesktopWidget
import sys
from MainWindow import StartWindow
from Globals import Globals
from space_classes import CelestialBody, np, Quaternion

if __name__ == '__main__':
    App = QApplication(sys.argv)
    Globals.DESKTOP_SIZE = QDesktopWidget().screenGeometry()
    space_objects = [CelestialBody(name='SpaceShip', color=Globals.RED, angle_velocity=np.array([5, 10, 0]),
                                   mass_center_coordinates_velocity=np.array([0, 5.0E7, 0, 5.0E7, 0, 0]),
                                   tensor_of_inertia=np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
                                   quaternion=Quaternion(0, 1, 1, 0))]
    window = StartWindow(space_objects)
    sys.exit(App.exec())
