from PyQt5.QtWidgets import QApplication, QDesktopWidget
import sys
from MainWindow import MainWindow
from Globals import Globals

if __name__ == '__main__':
    App = QApplication(sys.argv)
    Globals.DESCTOPSIZE = QDesktopWidget().screenGeometry()
    window = MainWindow()
    sys.exit(App.exec())
