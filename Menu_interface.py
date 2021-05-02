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
        self.open_gl = open_gl
        self.screen_size = open_gl.size()
        self.input_pulse = 0
        self.input_pulse_direction_angle = 0
        self.show()

        self.ui.pushButton_confirm1.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_confirm2.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_start.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_quit.clicked.connect(self.main_win.close)
        self.pulse = ''
        self.time_wait = ''

        self.ui.pushButton_start.clicked.connect(self.input)
        self.ui.pushButton_clear.clicked.connect(self.clear)

        self.ui.slider_pulse_direction.valueChanged.connect(self.slider_pulse_direction)

    def slider_pulse_direction(self):
        self.input_pulse_direction_angle = str(self.ui.slider_pulse_direction.value())

    def clear(self):
        self.ui.textEdit_pulse.clear()
        self.ui.textEdit_time.clear()

    def input(self):
        """
        Записывает в поля self.pulse и self.time_wait введенные пользователем значения
        после нажатия Start!
        """
        self.pulse = self.ui.textEdit_pulse.toPlainText()
        self.time_wait = self.ui.textEdit_time.toPlainText()
        self.open_gl.start_modeling = not self.open_gl.start_modeling
        if self.open_gl.start_modeling:
            self.ui.pushButton_start.setText("Pause")
            print(self.pulse)
            print(self.time_wait)
            print(self.input_pulse_direction_angle)
        else:
            self.ui.pushButton_start.setText("Start!")

    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()


if __name__ == '__main__':

    App = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(App.exec())

