from PyQt5.QtWidgets import QApplication, QDesktopWidget
import sys
from MainWindow import StartWindow
from Globals import Globals
from space_classes import CelestialBody, np, Quaternion

if __name__ == '__main__':
    App = QApplication(sys.argv)
    Globals.DESKTOP_SIZE = QDesktopWidget().screenGeometry()
    # space_objects = [CelestialBody(name='SpaceShip', color=Globals.RED, x=3.8E7, vy=3000, vx=-0,
    #                           engine_thrust=130000, time_engine_working=0, current_orientation=np.array([45, 1, 0, 0]),
    #                           w=np.array([1, 0, 0])),
    #                  CelestialBody(name='Earth', r=6.4E6, m=5.974E24, color=Globals.GREEN, vy=0, vx=0, x=0, y=0)]
    space_objects = [CelestialBody(name='SpaceShip', color=Globals.RED, angle_velocity=np.array([1, 1, 1]),
                                   orientation=np.array([0, 0, 0]),
                                   # mass_value_coordinates_velocity=np.array([5.974E23, 3.8E7, 0, 0, 3000, 0, 0]),
                                   quaternion=Quaternion(0, 1, 0, 0))]
    window = StartWindow(space_objects)
    sys.exit(App.exec())
