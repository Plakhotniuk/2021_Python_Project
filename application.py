from PyQt5.QtWidgets import QApplication
import sys
from MainWindow import MainWindow, StartWindow
from Globals import Globals
from space_classes import Starship, CelestialBody
from PyQt5 import QtWidgets

if __name__ == '__main__':
    App = QApplication(sys.argv)

    space_objects = []

    """Cписок небесных тел"""
    space_objects.append(Starship(name='SpaceShip', r=5.7E5, m=440000,
                                  color=Globals.RED, x=3.8E7, vy=3000, vx=-0, engine_thrust=130000,
                                  time_engine_working=0))
    space_objects.append(CelestialBody(name='Earth', r=6.4E6, m=5.974E24,
                                       color=Globals.GREEN, vy=0, vx=0, x=0, y=0))
    space_objects.append(CelestialBody(name='Moon', r=1.7E6, m=7.34E22,
                                       color=Globals.WHITE, x=38500000 * 10, vy=1000, vx=-0))
    space_objects.append(CelestialBody(name='Satellite', r=1.0E6, m=700000,
                                       color=Globals.YELLOW, x=0, y=5.0E7, vx=2000))

    gamewindow = MainWindow(space_objects)

    sys.exit(App.exec())
