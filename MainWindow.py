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
            return '/System/Library/Frameworks/' + name + '.framework/' + name


        util.find_library = new_util_find_library
except ImportError:
    pass
import sys
from math import pi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from PyQt_OpenGL import PyOpenGL
from PyQt5.QtCore import QTimer



class UiMainWindow(object):
    """
    Класс, создающий все виджеты (кнопки, слайдеры, надписи...)
    """

    def __init__(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuOpengl = QtWidgets.QMenu(self.menubar)
        self.label_engine_running_time = QtWidgets.QLabel(self.centralwidget)
        self.label_pulse = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_confirm1 = QtWidgets.QPushButton(self.centralwidget)
        self.textEdit_pulse = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_time_engine_working = QtWidgets.QTextEdit(self.centralwidget)
        self.label_current_direction_angle = QtWidgets.QLabel(self.centralwidget)
        self.label_direction_angle = QtWidgets.QLabel(self.centralwidget)
        self.label_time_factor = QtWidgets.QLabel(self.centralwidget)
        self.slider_pulse_direction = QtWidgets.QSlider(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.label_time_of_calculation_tr = QtWidgets.QLabel(self.centralwidget)
        self.textEdit_calc_tr = QtWidgets.QTextEdit(self.centralwidget)
        self.comboBox_time = QtWidgets.QComboBox(self.centralwidget)

        self.label_current_velocity_fuel = QtWidgets.QLabel(self.centralwidget)
        self.label_current_velocity_value = QtWidgets.QLabel(self.centralwidget)
        self.label_current_fuel_value = QtWidgets.QLabel(self.centralwidget)


    def setupUi(self, MainWindow):
        """
        Интерфейс окна
        :param MainWindow:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)

        """Полноэкранный режим и фиксация основного окна"""
        desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.resize(desktop_size.width(), desktop_size.height())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(True)
        """Далее идут все детали интерфейса (ползунки, кнопочки и тд):"""

        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.frame.setGeometry(
            QtCore.QRect(250 * desktop_size.width() / 1440, desktop_size.height() * 20 / 900, desktop_size.width() * 1161 / 1440, desktop_size.height() * 811 / 900))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMouseTracking(True)

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #TODO: уйти от хардкода в расположении виджетов(кнопок)
        """Buttons"""
        self.pushButton_quit.setGeometry(QtCore.QRect(60, 800, 113, 32))
        self.pushButton_quit.setObjectName("pushButton_quit")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setGeometry(QtCore.QRect(50, 645, 130, 70))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        # font.setPointSize(25)
        # self.pushButton_confirm1.setFont(font)
        # self.pushButton_confirm1.setGeometry(QtCore.QRect(50, 560, 130, 70))
        # self.pushButton_confirm1.setObjectName("pushButton_confirm1")

        self.pushButton_start.setGeometry(QtCore.QRect(50, 730, 130, 70))
        font.setPointSize(25)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        """Slider"""
        self.slider_pulse_direction.setGeometry(QtCore.QRect(10, 225, 200, 22))
        self.slider_pulse_direction.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pulse_direction.setObjectName("horizontalSlider_pulse_direction")
        self.slider_pulse_direction.valueChanged['int'].connect(self.label_current_direction_angle.setNum)
        self.slider_pulse_direction.setMinimum(0)
        self.slider_pulse_direction.setMaximum(360)
        self.slider_pulse_direction.setValue(0)
        self.slider_pulse_direction.setTickInterval(5)
        self.slider_pulse_direction.setTickPosition(QSlider.TicksBelow)
        self.slider_pulse_direction.setProperty("value", 0)
        self.slider_pulse_direction.setSliderPosition(0)

        """Combo Box"""
        self.comboBox_time.setObjectName("comboBox")
        self.comboBox_time.addItem("X1")
        self.comboBox_time.addItem("X2")
        self.comboBox_time.addItem("X5")
        self.comboBox_time.addItem("X10")
        self.comboBox_time.addItem("Real Time")
        self.comboBox_time.setGeometry(QtCore.QRect(130, 507, 105, 25))


        """Labels and Fonts"""
        self.label.setGeometry(QtCore.QRect(20, 20, int(220 / 1440 * desktop_size.width()), int(110 / 900 * desktop_size.height())))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_pulse.setGeometry(QtCore.QRect(20, 117, 121, 51))
        self.label_pulse.setFont(font)
        self.label_pulse.setObjectName("label_pulse")

        font.setPointSize(25)
        self.label_engine_running_time.setGeometry(QtCore.QRect(20, 195, 200, 251))
        self.label_engine_running_time.setFont(font)
        self.label_engine_running_time.setObjectName("label_time_wait")

        font.setPointSize(25)
        self.label_time_of_calculation_tr.setGeometry(QtCore.QRect(20, 380, 210, 70))
        self.label_time_of_calculation_tr.setFont(font)
        self.label_time_of_calculation_tr.setObjectName("label_time_of_calc")

        self.label_current_velocity_fuel.setGeometry(QtCore.QRect(1100, 50, 210, 70))
        self.label_current_velocity_fuel.setFont(font)
        self.label_current_velocity_fuel.setObjectName("label_current_velocity")
        self.label_current_velocity_fuel.setStyleSheet("color: white")

        self.label_current_velocity_value.setGeometry(QtCore.QRect(1300, 40, 210, 70))
        self.label_current_velocity_value.setFont(font)
        self.label_current_velocity_value.setObjectName("label_current_velocity_value")
        self.label_current_velocity_value.setStyleSheet("color: white")

        self.label_current_fuel_value.setGeometry(QtCore.QRect(1300, 65, 210, 70))
        self.label_current_fuel_value.setFont(font)
        self.label_current_fuel_value.setObjectName("label_current_fuel_value")
        self.label_current_fuel_value.setStyleSheet("color: white")


        font.setPointSize(18)
        self.label_current_direction_angle.setFont(font)
        self.label_current_direction_angle.setGeometry(QtCore.QRect(215, 215, 50, 31))
        self.label_current_direction_angle.setObjectName("label_direction_angle")

        font.setPointSize(25)
        self.label_direction_angle.setFont(font)
        self.label_direction_angle.setGeometry(QtCore.QRect(20, 170, 250, 61))
        self.label_direction_angle.setObjectName("label_direction_angle")

        self.label_time_factor.setFont(font)
        self.label_time_factor.setGeometry(QtCore.QRect(10, 500, 130, 30))
        self.label_time_factor.setObjectName("label_time_factor")

        """Text edit"""
        self.textEdit_pulse.setGeometry(QtCore.QRect(110, 130, 105, 30))
        self.textEdit_pulse.setObjectName("textEdit_pulse")

        self.textEdit_time_engine_working.setGeometry(QtCore.QRect(110, 330, 105, 30))
        self.textEdit_time_engine_working.setObjectName("textEdit_time_engine_working")

        self.textEdit_calc_tr.setGeometry(QtCore.QRect(110, 450, 105, 30))
        self.textEdit_calc_tr.setObjectName("textEdit_calcs_tr")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 24))
        self.menubar.setObjectName("menubar")
        self.menuOpengl.setObjectName("menuOpengl")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpengl.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Выводит надписи на кнопках и доп поверхностях
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        # self.pushButton_confirm1.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_start.setText(_translate("MainWindow", "Start !"))
        self.label.setText(_translate("MainWindow", "Set Parametrs\n" "to\n" "Start modeling!"))
        self.label_pulse.setText(_translate("MainWindow", "Pulse :"))
        self.label_engine_running_time.setText(_translate("MainWindow", "Engine running\ntime :"))
        self.menuOpengl.setTitle(_translate("MainWindow", "Opengl"))
        self.label_current_direction_angle.setText(_translate("MainWindow", "0"))
        self.label_direction_angle.setText(_translate("MainWindow", "Angle :"))
        self.label_time_factor.setText(_translate("MainWindow", "Time factor :"))

        self.label_time_of_calculation_tr.setText(_translate("MainWindow", "Time of \ncalculation:"))

        self.label_current_velocity_fuel.setText(_translate("MainWindow", "Velocity: \nFuel consumption:"))
        self.label_current_fuel_value.setText(_translate("MainWindow", "0"))
        self.label_current_velocity_value.setText(_translate("MainWindow", "0"))


        self.comboBox_time.setItemText(0, _translate("MainWindow", "X1"))
        self.comboBox_time.setItemText(1, _translate("MainWindow", "X2"))
        self.comboBox_time.setItemText(2, _translate("MainWindow", "X5"))
        self.comboBox_time.setItemText(3, _translate("MainWindow", "X10"))
        self.comboBox_time.setItemText(4, _translate("MainWindow", "Real Time"))



class MainWindow(QtWidgets.QWidget):
    """
    Класс основного меню внутри приложения
    """

    def __init__(self, sp_objects: list):
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_win = QtWidgets.QMainWindow()
        self.ui = UiMainWindow(self.main_win)
        self.ui.setupUi(self.main_win)
        open_gl = PyOpenGL(sp_objects, parent=self.ui.frame)
        open_gl.setMinimumSize(self.ui.frame.width(), self.ui.frame.height())
        self.open_gl = open_gl
        self.screen_size = open_gl.size()
        self.input_pulse_direction_angle = 0
        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_velocity)
        self.timer.start(100)
        # self.ui.pushButton_confirm1.clicked.connect(open_gl.setFocus)
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

    def update_velocity(self):
        self.ui.label_current_velocity_value.setText(str(int(self.open_gl.current_velocity)))

    def set_time_accelerate(self):
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
            self.combobox_index_time = 0.001
        self.open_gl.calculation_module.set_speed(3000 * self.combobox_index_time)

    def slider_pulse_direction(self):
        self.input_pulse_direction_angle = int(self.ui.slider_pulse_direction.value())

    def clear(self):
        self.ui.textEdit_pulse.clear()
        self.ui.textEdit_time_engine_working.clear()
        self.ui.textEdit_calc_tr.clear()

    def calc_trajectory(self):
        self.open_gl.is_trajectory_shown = not self.open_gl.is_trajectory_shown
        if self.open_gl.is_trajectory_shown:
            self.ui.pushButton_calculate.setText('Back')
            self.ui.pushButton_start.setEnabled(False)
        else:
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_calculate.setText('Calculate')

        self.open_gl.setFocus()
        self.pulse = str(self.ui.textEdit_pulse.toPlainText())
        self.time_engine_working = str(self.ui.textEdit_time_engine_working.toPlainText())
        self.time_of_modeling = str(self.ui.textEdit_calc_tr.toPlainText())
        if self.time_engine_working != '':
            self.space_objects[self.starshipi_index].time_engine_working = float(self.time_engine_working)
        if self.input_pulse_direction_angle != '':
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
            self.ui.pushButton_start.setText("Pause")
            if self.time_engine_working != '':
                self.space_objects[self.starshipi_index].time_engine_working = float(self.time_engine_working)
                if self.pulse != '':
                    """Расчет расхода топлива"""
                    self.open_gl.total_fuel_consumption += float(self.time_engine_working) * float(self.pulse)\
                                                           / self.open_gl.specific_impulse_of_rocket_engine
                    self.ui.label_current_fuel_value.setText(str(int(self.open_gl.total_fuel_consumption)))

            if self.input_pulse_direction_angle != '':
                self.space_objects[self.starshipi_index].engine_angle = float(self.input_pulse_direction_angle) \
                                                                        * pi / 180
            if self.pulse != '':
                self.space_objects[self.starshipi_index].engine_thrust = float(self.pulse)
            self.ui.slider_pulse_direction.setValue(0)
            self.clear()

            self.ui.pushButton_calculate.setEnabled(False)  # чтобы нельзя было калькулить во время работы игры

        else:
            self.ui.pushButton_start.setText("Start!")
            self.time_engine_working = 0
            self.ui.pushButton_calculate.setEnabled(True)  # чтобы можно было калькулить только когда игра не работает

    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()

