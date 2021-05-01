try:
    import OpenGL as ogl
    try:
        import OpenGL.GL
    except ImportError:
        print('Drat, patching for Big Sur')
        from ctypes import util
        orig_util_find_library = util.find_library

        def new_util_find_library(name):
            res = orig_util_find_library(name)
            if res:
                return res
            return '/System/Library/Frameworks/'+name+'.framework/'+name
        util.find_library = new_util_find_library
except ImportError:
    pass

import sys
from PyQt5.QtWidgets import QApplication, QAction, QPushButton, qApp, QTextEdit, QMouseEventTransition
from Ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtPrintSupport
from PyQt_OpenGL import PyOpenGL


class MainWindow:
    """
    Класс основного меню внутри приложения
    """
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.main_win)
        self.ui.setupUi(self.main_win)
        open_gl = PyOpenGL(parent=self.ui.frame)
        open_gl.setMinimumSize(self.ui.frame.width(), self.ui.frame.height())

        self.screen_size = open_gl.size()
        self.show()
        self.ui.pushButton_quit.clicked.connect(sys.exit)


    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()


if __name__ == '__main__':

    App = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(App.exec())

