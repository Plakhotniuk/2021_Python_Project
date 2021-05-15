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


class UiMainWindow:
    """
    Класс, создающий все виджеты (кнопки, слайдеры, надписи...)
    """

    def __init__(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuOpengl = QtWidgets.QMenu(self.menubar)
        self.label_engine_running_time = QtWidgets.QLabel(self.centralwidget)
        self.label_pulse = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
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
        # TODO: Functions!
        """
        Интерфейс окна
        :param MainWindow:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)

        """Полноэкранный режим и фиксация основного окна"""
        desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.resize(desktop_size.width(), desktop_size.height())
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setMouseTracking(True)

        """Далее идут все детали интерфейса (ползунки, кнопочки и тд):"""

        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.Picture.setGeometry(QtCore.QRect(0, 0, desktop_size.width(), desktop_size.height()))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("StarrySky.jpg"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")
        self.frame.setGeometry(
            QtCore.QRect(250 * desktop_size.width() / 1440, desktop_size.height() * 20 / 900,
                         desktop_size.width() * 1161 / 1440, desktop_size.height() * 811 / 900))

        size_policy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(size_policy)
        self.frame.setMouseTracking(True)

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # TODO: уйти от хардкода в расположении виджетов(кнопок)

        """Buttons"""
        self.pushButton_quit.setGeometry(QtCore.QRect(60 * desktop_size.width() / 1366, 642 * desktop_size.height()/768,
                                                      113 * desktop_size.width()/1366, 32 * desktop_size.height()/768))
        self.pushButton_quit.setObjectName("pushButton_quit")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setGeometry(QtCore.QRect(50 * desktop_size.width() / 1366,
                                                           530 * desktop_size.height() / 768,
                                                           130 * desktop_size.width() / 1366,
                                                           55 * desktop_size.height() / 768))
        self.pushButton_calculate.setObjectName("pushButton_calculate")

        self.pushButton_start.setGeometry(QtCore.QRect(50 * desktop_size.width() / 1366,
                                                       588 * desktop_size.height() / 768,
                                                       int(130 * desktop_size.width() / 1366),
                                                       int(52 * desktop_size.height() / 768)))
        font.setPointSize(25)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        """Slider"""
        self.slider_pulse_direction.setGeometry(QtCore.QRect(10 * desktop_size.width() / 1366,
                                                             245 * desktop_size.height() / 768,
                                                             int(200 * desktop_size.width() / 1366),
                                                             int(22 * desktop_size.height() / 768)))
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
        self.slider_pulse_direction.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4,"
                                                  " stop:1 #8f8f8f);border: 1px solid #5c5c5c; width: 18px;"
                                                  " margin: -2px 0; border-radius: 5px;")

        """Combo Box"""
        self.comboBox_time.setObjectName("comboBox")
        self.comboBox_time.addItem("X1")
        self.comboBox_time.addItem("X2")
        self.comboBox_time.addItem("X5")
        self.comboBox_time.addItem("X10")
        self.comboBox_time.addItem("Real Time")
        self.comboBox_time.setGeometry(QtCore.QRect(130 * desktop_size.width() / 1366,
                                                    507 * desktop_size.height() / 768,
                                                    105 * desktop_size.width() / 1366,
                                                    25 * desktop_size.height() / 768))

        """Labels and Fonts"""
        self.label.setGeometry(
            QtCore.QRect(20 * desktop_size.width() / 1366, 20 * desktop_size.height() / 768,
                         int(220 / 1440 * desktop_size.width()), int(110 / 900 * desktop_size.height())))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white")

        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_pulse.setGeometry(QtCore.QRect(16 * desktop_size.width() / 1366, 117 * desktop_size.height() / 768,
                                                  157 * desktop_size.width() / 1366, 51 * desktop_size.height() / 768))
        self.label_pulse.setFont(font)
        self.label_pulse.setObjectName("label_pulse")
        self.label_pulse.setStyleSheet("color: white")

        font.setPointSize(20)
        self.label_engine_running_time.setGeometry(QtCore.QRect(16 * desktop_size.width() / 1366,
                                                                195 * desktop_size.height() / 768,
                                                                200 * desktop_size.width() / 1366,
                                                                251 * desktop_size.height() / 768))
        self.label_engine_running_time.setFont(font)
        self.label_engine_running_time.setObjectName("label_time_wait")
        self.label_engine_running_time.setStyleSheet("color: white")

        font.setPointSize(20)
        self.label_time_of_calculation_tr.setGeometry(QtCore.QRect(20 * desktop_size.width() / 1366,
                                                                   380 * desktop_size.height() / 768,
                                                                   210 * desktop_size.width() / 1366,
                                                                   70 * desktop_size.height() / 768))
        self.label_time_of_calculation_tr.setFont(font)
        self.label_time_of_calculation_tr.setObjectName("label_time_of_calc")
        self.label_time_of_calculation_tr.setStyleSheet("color: white")

        self.label_current_velocity_fuel.setGeometry(QtCore.QRect(1050 * desktop_size.width() / 1366,
                                                                  50 * desktop_size.height() / 768,
                                                                  250 * desktop_size.width() / 1366,
                                                                  70 * desktop_size.height() / 768))
        self.label_current_velocity_fuel.setFont(font)
        self.label_current_velocity_fuel.setObjectName("label_current_velocity")
        self.label_current_velocity_fuel.setStyleSheet("color: white")

        self.label_current_velocity_value.setGeometry(QtCore.QRect(1290 * desktop_size.width() / 1366,
                                                                   40 * desktop_size.height() / 768,
                                                                   210 * desktop_size.width() / 1366,
                                                                   70 * desktop_size.height() / 768))
        self.label_current_velocity_value.setFont(font)
        self.label_current_velocity_value.setObjectName("label_current_velocity_value")
        self.label_current_velocity_value.setStyleSheet("color: white")

        self.label_current_fuel_value.setGeometry(QtCore.QRect(1290 * desktop_size.width() / 1366,
                                                               65 * desktop_size.height() / 768,
                                                               210 * desktop_size.width() / 1366,
                                                               70 * desktop_size.height() / 768))
        self.label_current_fuel_value.setFont(font)
        self.label_current_fuel_value.setObjectName("label_current_fuel_value")
        self.label_current_fuel_value.setStyleSheet("color: white")

        font.setPointSize(18)
        self.label_current_direction_angle.setFont(font)
        self.label_current_direction_angle.setGeometry(QtCore.QRect(215 * desktop_size.width() / 1366,
                                                                    235 * desktop_size.height() / 768,
                                                                    50 * desktop_size.width() / 1366,
                                                                    31 * desktop_size.height() / 768))
        self.label_current_direction_angle.setObjectName("label_direction_angle")
        self.label_current_direction_angle.setStyleSheet("color: white")

        font.setPointSize(20)
        self.label_direction_angle.setFont(font)
        self.label_direction_angle.setGeometry(QtCore.QRect(20 * desktop_size.width() / 1366, 190,
                                                            250 * desktop_size.width() / 1366, 61))
        self.label_direction_angle.setObjectName("label_direction_angle")
        self.label_direction_angle.setStyleSheet("color: white")

        font.setPointSize(17)
        self.label_time_factor.setFont(font)
        self.label_time_factor.setGeometry(QtCore.QRect(5 * desktop_size.width() / 1366,
                                                        500 * desktop_size.height() / 768,
                                                        130 * desktop_size.width() / 1366,
                                                        30 * desktop_size.height() / 768))
        self.label_time_factor.setObjectName("label_time_factor")
        self.label_time_factor.setStyleSheet("color: white")

        """Text edit"""
        self.textEdit_pulse.setGeometry(QtCore.QRect(110 * desktop_size.width() / 1366,
                                                     160 * desktop_size.height() / 768,
                                                     105 * desktop_size.width() / 1366,
                                                     30 * desktop_size.height() / 768))
        self.textEdit_pulse.setObjectName("textEdit_pulse")

        self.textEdit_time_engine_working.setGeometry(QtCore.QRect(110 * desktop_size.width() / 1366,
                                                                   330 * desktop_size.height() / 768,
                                                                   105 * desktop_size.width() / 1366,
                                                                   30 * desktop_size.height() / 768))
        self.textEdit_time_engine_working.setObjectName("textEdit_time_engine_working")

        self.textEdit_calc_tr.setGeometry(QtCore.QRect(110 * desktop_size.width() / 1366,
                                                       450 * desktop_size.height() / 768,
                                                       105 * desktop_size.width() / 1366,
                                                       30 * desktop_size.height() / 768))
        self.textEdit_calc_tr.setObjectName("textEdit_calcs_tr")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827 * desktop_size.width() / 1366, 24 * desktop_size.height()/768))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Kerbal 2.0 !"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_start.setText(_translate("MainWindow", "Start !"))
        self.label.setText(_translate("MainWindow", "Set Parametrs\n" "to\n" "Start modeling!"))
        self.label_pulse.setText(_translate("MainWindow", "Pulse (kg m/s):"))
        self.label_engine_running_time.setText(_translate("MainWindow", "Engine running\ntime (s):"))
        self.menuOpengl.setTitle(_translate("MainWindow", "Opengl"))
        self.label_current_direction_angle.setText(_translate("MainWindow", "0"))
        self.label_direction_angle.setText(_translate("MainWindow", "Angle (degrees) :"))
        self.label_time_factor.setText(_translate("MainWindow", "Time factor :"))

        self.label_time_of_calculation_tr.setText(_translate("MainWindow", "Time of \ncalculation (s):"))

        self.label_current_velocity_fuel.setText(_translate("MainWindow", "Velocity(m/s): \nFuel left (kg):"))
        self.label_current_fuel_value.setText(_translate("MainWindow", "0"))
        self.label_current_velocity_value.setText(_translate("MainWindow", "0"))

        self.comboBox_time.setItemText(0, _translate("MainWindow", "X1"))
        self.comboBox_time.setItemText(1, _translate("MainWindow", "X2"))
        self.comboBox_time.setItemText(2, _translate("MainWindow", "X5"))
        self.comboBox_time.setItemText(3, _translate("MainWindow", "X10"))
        self.comboBox_time.setItemText(4, _translate("MainWindow", "Real Time"))


class UiStartWindow:
    def __init__(self, StartWindow):
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.statusbar = QtWidgets.QStatusBar(StartWindow)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

    def setupUi(self, StartWindow):
        desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(desktop_size.width(), desktop_size.height())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartWindow.sizePolicy().hasHeightForWidth())
        StartWindow.setSizePolicy(sizePolicy)

        self.Picture.setGeometry(QtCore.QRect(0, 0, desktop_size.width(), desktop_size.height()))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("Entire_screen.jpg"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")
        self.pushButton.setGeometry(QtCore.QRect(580 * desktop_size.width() / 1366, 620 * desktop_size.height()/768,
                                                 241 * desktop_size.width() / 1366, 91 * desktop_size.height()/768))

        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440 * desktop_size.width() / 1366, 22 * desktop_size.height()/768))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        StartWindow.setStatusBar(self.statusbar)
        self.pushButton.setStyleSheet("#pushButton{background-color: transparent; border-image: url(StartGame.png);"
                                      " background: none; border: none; background-repeat: none;} #pushButton:pressed {border-image: url(StartGamePressed.png)}")

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "StartWindow"))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")


class StartWindow(QtWidgets.QWidget):
    """
        Класс начального меню внутри приложения
    """
    def __init__(self, sp_objects: list):
        super(StartWindow, self).__init__()
        self.main_win = QtWidgets.QMainWindow()
        self.ui = UiStartWindow(self.main_win)
        self.sp_objects = sp_objects
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.show_main_window)
        self.show()

    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()

    def show_main_window(self):
        """
        Создает основное окно внутри приложения
        """
        self.game_window = MainWindow(self.sp_objects)
        self.main_win.close()


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

    def update_velocity_and_angle(self):
        self.ui.label_current_velocity_value.setText(str(int(self.open_gl.current_velocity)))
        self.open_gl.current_angle = int(self.ui.slider_pulse_direction.value())
        self.ui.label_current_fuel_value.setText(str(int(self.space_objects[0].m - self.open_gl.minimum_mass)))

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
            self.combobox_index_time = 0.00033
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
            if self.time_engine_working != '' and self.pulse != '' and\
                    self.space_objects[0].m - float(self.time_engine_working) * float(self.pulse)\
                    / self.open_gl.specific_impulse_of_rocket_engine > self.open_gl.minimum_mass:
                self.space_objects[self.starshipi_index].time_engine_working = float(self.time_engine_working)
                """Расчет расхода топлива"""
                self.space_objects[0].m -= float(self.time_engine_working) * float(self.pulse) \
                                                               / self.open_gl.specific_impulse_of_rocket_engine
                self.ui.label_current_fuel_value.setText(str(int(self.space_objects[0].m - self.open_gl.minimum_mass)))

                if self.input_pulse_direction_angle != '':
                    self.space_objects[self.starshipi_index].engine_angle = float(self.input_pulse_direction_angle) \
                                                                            * pi / 180
                self.space_objects[self.starshipi_index].engine_thrust = float(self.pulse)
            self.ui.slider_pulse_direction.setValue(0)
            self.clear()

            self.ui.pushButton_calculate.setEnabled(False)

        else:
            self.ui.pushButton_start.setText("Start!")
            self.time_engine_working = 0
            self.ui.pushButton_calculate.setEnabled(True)

    def show(self):
        """
        Отображает меню на экране
        """
        self.main_win.show()
