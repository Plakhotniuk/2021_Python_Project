try:
    import OpenGL as Ogl

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
            return '/System/Library/Frameworks/' + name + '.framework/' + name

        util.find_library = new_util_find_library
except ImportError:
    pass
from math import pi
from PyQt5 import QtWidgets
from PyQt_OpenGL import PyOpenGL
from PyQt5.QtCore import QTimer
from UIClasses import UiTutorial, UiStartWindow, UiMainWindow


class StartWindow(QtWidgets.QWidget):
    """
    Класс начального меню внутри приложения
    """
    def __init__(self, sp_objects: list):
        super(StartWindow, self).__init__()
        self.start_win = QtWidgets.QMainWindow()
        self.ui = UiStartWindow(self.start_win)
        self.sp_objects = sp_objects
        self.ui.pushButton.clicked.connect(self.show_main_window)
        self.start_win.show()
        self.game_window = None

    def show_main_window(self):
        """
        Create game window
        """
        self.game_window = MainWindow(self.sp_objects)
        self.game_window.show()
        self.start_win.close()


class TutorialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.start_win = QtWidgets.QMainWindow()
        self.ui = UiTutorial(self.start_win)
        self.ui.pushButton_back.clicked.connect(self.start_win.close)

    def show(self):
        self.start_win.show()


class MainWindow(QtWidgets.QWidget):
    """
    Класс основного меню внутри приложения
    """
    def __init__(self, sp_objects: list):
        super(MainWindow, self).__init__()
        self.main_win = QtWidgets.QMainWindow()
        self.ui = UiMainWindow(self.main_win)
        open_gl = PyOpenGL(sp_objects, parent=self.ui.frame)
        open_gl.setMinimumSize(self.ui.frame.width(), self.ui.frame.height())
        self.open_gl = open_gl
        self.tutorial_window = None
        self.screen_size = open_gl.size()
        self.input_pulse_direction_angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_velocity_and_angle)
        self.timer.start(10)
        self.ui.pushButton_start.clicked.connect(open_gl.setFocus)
        self.ui.pushButton_quit.clicked.connect(self.main_win.close)
        self.pulse = ''
        self.time_engine_working = ''
        self.time_of_modeling = ''
        self.space_objects = sp_objects
        self.starshipi_index = 0
        self.combobox_index_time = 0
        self.ui.pushButton_start.clicked.connect(self.input)
        self.ui.pushButton_start.clicked.connect(self.set_time_accelerate)
        self.ui.pushButton_calculate.clicked.connect(self.calc_trajectory)
        self.ui.slider_pulse_direction.valueChanged.connect(self.slider_pulse_direction)
        self.ui.pushButton_help.clicked.connect(self.help)

    def update_velocity_and_angle(self):
        """
        Обновляет значения угла и скорости движения космического корабля
        """
        self.ui.label_current_velocity_value.setText(str(int(self.open_gl.current_velocity)))
        self.open_gl.current_angle = int(self.ui.slider_pulse_direction.value())

        self.ui.label_current_fuel_value.setText(str(int(self.space_objects[0].m - self.open_gl.minimum_mass)))

    def set_time_accelerate(self):
        """
        Устанавливает коэффициент ускорения времени
        """
        self.open_gl.setFocus()
        if self.ui.comboBox_time.currentIndex() == 0:
            self.combobox_index_time = 1
        if self.ui.comboBox_time.currentIndex() == 1:
            self.combobox_index_time = 2
        if self.ui.comboBox_time.currentIndex() == 2:
            self.combobox_index_time = 5
        if self.ui.comboBox_time.currentIndex() == 3:
            self.combobox_index_time = 10
        if self.ui.comboBox_time.currentIndex() == 4:
            self.combobox_index_time = 0.00033
        self.open_gl.calculation_module.set_speed(3000 * self.combobox_index_time)

    def slider_pulse_direction(self):
        """
        Обновляет угол под которым будет передан импульс для отображения направляющего вектора
        """
        self.input_pulse_direction_angle = int(self.ui.slider_pulse_direction.value())

    def clear(self):
        """
        Удаляет старые значения в текстовых окошках и зануляет значение на слайдере
        """
        self.ui.textEdit_pulse.clear()
        self.ui.textEdit_time_engine_working.clear()
        self.ui.textEdit_calc_tr.clear()

    def calc_trajectory(self):
        """
        Обработка нажатия на кнопку Calculation, запись введенных пользователем значений
        в поля классов для дальнейшей отрисовки траектории
        """
        self.open_gl.is_trajectory_shown = not self.open_gl.is_trajectory_shown
        if self.open_gl.is_trajectory_shown:
            self.ui.pushButton_calculate.setStyleSheet(
                "#pushButton{background-color: transparent; border-image: url(Back.png);"
                " background: none; border: none; background-repeat: none;} #pushButton:pressed"
                " {border-image: url(BackPressed.png)}")
            self.ui.pushButton_start.setEnabled(False)
        else:
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_calculate.setStyleSheet(
                "#pushButton{background-color: transparent; border-image: url(Calculate.png);"
                " background: none; border: none; background-repeat: none;} #pushButton:pressed"
                " {border-image: url(CalculatePressed.png)}")

        self.open_gl.setFocus()
        self.pulse = str(self.ui.textEdit_pulse.toPlainText())
        self.time_engine_working = str(self.ui.textEdit_time_engine_working.toPlainText())
        self.time_of_modeling = str(self.ui.textEdit_calc_tr.toPlainText())
        if self.time_engine_working != '':
            self.space_objects[self.starshipi_index].time_engine_working = float(self.time_engine_working)
        if self.input_pulse_direction_angle != '':
            print(self.input_pulse_direction_angle)
            self.space_objects[self.starshipi_index].engine_angle = (int(self.input_pulse_direction_angle) * pi) / 180
        if self.pulse != '':
            self.space_objects[self.starshipi_index].engine_thrust = float(self.pulse)
        if self.time_of_modeling == '':
            self.time_of_modeling = 0

        self.open_gl.calculation_module.calculate_prev_trajectory(float(self.time_of_modeling))

    def input(self):
        """
        Записывает в поля self.pulse и self.time_wait введенные пользователем значения
        после нажатия Start!
        """
        self.pulse = str(self.ui.textEdit_pulse.toPlainText())
        self.time_engine_working = str(self.ui.textEdit_time_engine_working.toPlainText())
        self.open_gl.start_modeling = not self.open_gl.start_modeling
        if self.open_gl.start_modeling:
            self.ui.pushButton_start.setStyleSheet(
                "#pushButton{background-color: transparent; border-image: url(Pause.png);"
                " background: none; border: none; background-repeat: none;} #pushButton:pressed"
                " {border-image: url(PausePressed.png)}")
            if self.time_engine_working != '' and self.pulse != '' and \
                    self.space_objects[0].m - float(self.time_engine_working) * float(self.pulse) \
                    / self.open_gl.specific_impulse_of_rocket_engine > self.open_gl.minimum_mass:
                self.space_objects[self.starshipi_index].time_engine_working = float(self.time_engine_working)
                """Расчет расхода топлива"""
                self.space_objects[0].m -= float(self.time_engine_working) * float(self.pulse) \
                                           / self.open_gl.specific_impulse_of_rocket_engine
                self.ui.label_current_fuel_value.setText(str(int(self.space_objects[0].m - self.open_gl.minimum_mass)))

                if self.input_pulse_direction_angle != '':
                    print(self.input_pulse_direction_angle)
                    self.space_objects[self.starshipi_index].engine_angle = float(self.input_pulse_direction_angle) \
                                                                            * pi / 180
                self.space_objects[self.starshipi_index].engine_thrust = float(self.pulse)
            self.ui.slider_pulse_direction.setValue(0)
            self.clear()
            self.ui.pushButton_calculate.setEnabled(False)

        else:
            self.ui.pushButton_start.setStyleSheet(
                "#pushButton{background-color: transparent; border-image: url(Start.png);"
                " background: none; border: none; background-repeat: none;} #pushButton:pressed"
                " {border-image: url(StartPressed.png)}")
            self.time_engine_working = 0
            self.ui.pushButton_calculate.setEnabled(True)

    def show(self):
        self.main_win.show()
        self.help()

    def help(self):
        self.tutorial_window = TutorialWindow()
        self.tutorial_window.show()
