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
from math import pi
from PyQt5 import QtWidgets
from PyQt_OpenGL import PyOpenGL
from Ui_mainwindow import Ui_MainWindow
from space_objects import space_objects


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
        self.input_pulse_direction_angle = 0
        self.show()

        self.ui.pushButton_confirm1.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_confirm2.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_start.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_quit.clicked.connect(self.main_win.close)
        self.pulse = ''
        self.time_wait = ''

        self.ui.pushButton_start.clicked.connect(self.input)
        self.ui.pushButton_clear.clicked.connect(self.calc_trajectory)

        self.ui.slider_pulse_direction.valueChanged.connect(self.slider_pulse_direction)

    def slider_pulse_direction(self):
        self.input_pulse_direction_angle = int(self.ui.slider_pulse_direction.value())

    def clear(self):
        self.ui.textEdit_pulse.clear()
        self.ui.textEdit_time.clear()

    def calc_trajectory(self):

        # TODO: меняем текст кнопки вызываем метод окна PyQt
        #          Оттуда вызываем калкулятор и возвращаем большуб херню
        #         потом в том же методе отрисовываем эту фигню
        pass

    def input(self):
        """
        Записывает в поля self.pulse и self.time_wait введенные пользователем значения
        после нажатия Start!
        """
        self.pulse = str(self.ui.textEdit_pulse.toPlainText())
        self.time_wait = str(self.ui.textEdit_time.toPlainText())
        self.open_gl.start_modeling = not self.open_gl.start_modeling
        if self.open_gl.start_modeling:
            self.ui.pushButton_start.setText("Pause")
            if self.time_wait != '':
                space_objects[0].time_engine_working = float(self.time_wait)
            if self.input_pulse_direction_angle != '':
                space_objects[0].engine_angle = float(self.input_pulse_direction_angle) * pi / 180
            if self.pulse != '':
                space_objects[0].engine_thrust = float(self.pulse)
        else:
            self.ui.pushButton_start.setText("Start!")
            self.time_wait = 0
        self.clear()

    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()





