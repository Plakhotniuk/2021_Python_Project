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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider


class UiMainWindow:
    """
    The class in which the initialization of all
    widgets of the main in-game window with the specified default values
    """

    def __init__(self, main_window):
        self.font = QtGui.QFont()
        self.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        self.main_window = main_window
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.menuOpengl = QtWidgets.QMenu(self.menubar)
        self.label_engine_running_time = QtWidgets.QLabel(self.centralwidget)
        self.label_pulse = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_help = QtWidgets.QPushButton(self.centralwidget)
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
        self.set_main_screen()
        self.set_central_widget_picture_frame()
        self.set_buttons()
        self.set_slider()
        self.set_combo_box()
        self.set_main_label()
        self.set_label_pulse()
        self.set_label_engine_running_time()
        self.set_label_time_of_calculation_tr()
        self.set_label_current_velocity_fuel()
        self.set_label_current_velocity_value()
        self.set_label_current_fuel_value()
        self.set_label_current_direction_angle()
        self.set_label_direction_angle()
        self.set_label_time_factor()
        self.set_text_edits()
        self.set_menubar()

    def set_main_screen(self):
        """
        Main Screen policy
        """
        self.main_window.setObjectName("MainWindow")
        self.main_window.setEnabled(True)
        self.main_window.resize(self.desktop_size.width(), self.desktop_size.height())
        self.size_policy.setHorizontalStretch(0)
        self.size_policy.setVerticalStretch(0)
        self.size_policy.setHeightForWidth(self.main_window.sizePolicy().hasHeightForWidth())
        self.main_window.setSizePolicy(self.size_policy)
        self.main_window.setMouseTracking(True)

    def set_central_widget_picture_frame(self):
        """
        Shows main window, sets picture and frame
        """
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.Picture.setGeometry(QtCore.QRect(0, 0, self.desktop_size.width(), self.desktop_size.height()))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("Pictures/StarrySky.jpg"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")
        self.frame.setGeometry(
            QtCore.QRect(265 * self.desktop_size.width() / 1440, self.desktop_size.height() * 20 / 900,
                         self.desktop_size.width() * 1161 / 1440, self.desktop_size.height() * 811 / 900))
        self.size_policy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(self.size_policy)
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

    def set_buttons(self):
        """
        Buttons params
        """
        self.pushButton_quit.setGeometry(QtCore.QRect(60 * self.desktop_size.width() / 1366,
                                                      642 * self.desktop_size.height() / 768,
                                                      113 * self.desktop_size.width() / 1366,
                                                      32 * self.desktop_size.height() / 768))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_quit.setStyleSheet(
            "#pushButton{background-color: transparent; border-image: url(Pictures/Quit.png);"
            " background: none; border: none; background-repeat: none;} #pushButton:pressed"
            " {border-image: url(Pictures/QuitPressed.png)}")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setGeometry(QtCore.QRect(50 * self.desktop_size.width() / 1366,
                                                           530 * self.desktop_size.height() / 768,
                                                           130 * self.desktop_size.width() / 1366,
                                                           55 * self.desktop_size.height() / 768))
        self.pushButton_calculate.setObjectName("Pictures/pushButton_calculate")
        self.pushButton_calculate.setStyleSheet("#pushButton{background-color: transparent; border-image:"
                                                " url(Pictures/Calculate.png);"
                                                " background: none; border: none; background-repeat: none;}"
                                                " #pushButton:pressed"
                                                " {border-image: url(Pictures/CalculatePressed.png)}")

        self.pushButton_start.setGeometry(QtCore.QRect(50 * self.desktop_size.width() / 1366,
                                                       588 * self.desktop_size.height() / 768,
                                                       int(130 * self.desktop_size.width() / 1366),
                                                       int(52 * self.desktop_size.height() / 768)))
        font.setPointSize(25)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("Pictures/pushButton_start")
        self.pushButton_start.setStyleSheet(
            "#pushButton{background-color: transparent; border-image: url(Pictures/Start.png);"
            " background: none; border: none; background-repeat: none;} #pushButton:pressed"
            " {border-image: url(Pictures/StartPressed.png)}")

        self.pushButton_help.setGeometry(QtCore.QRect(200 * self.desktop_size.width() / 1366,
                                                      50 * self.desktop_size.height() / 768,
                                                      int(50 * self.desktop_size.width() / 1366),
                                                      int(50 * self.desktop_size.height() / 768)))
        font.setPointSize(25)
        self.pushButton_help.setFont(font)
        self.pushButton_help.setObjectName("Pictures/pushButton_help")
        self.pushButton_help.setStyleSheet("#pushButton{background-color: transparent; border-image:"
                                           " url(Pictures/Help.png);"
                                           " background: none; border: none; background-repeat: none;}"
                                           " #pushButton:pressed"
                                           " {border-image: url(Pictures/HelpPressed.png)}")

    def set_slider(self):
        """
        Slider params
        """
        self.slider_pulse_direction.setGeometry(QtCore.QRect(10 * self.desktop_size.width() / 1366,
                                                             245 * self.desktop_size.height() / 768,
                                                             int(200 * self.desktop_size.width() / 1366),
                                                             int(22 * self.desktop_size.height() / 768)))
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

    def set_combo_box(self):
        """
        Combo Box params
        """
        self.comboBox_time.setObjectName("comboBox")
        self.comboBox_time.addItem("X1")
        self.comboBox_time.addItem("X2")
        self.comboBox_time.addItem("X5")
        self.comboBox_time.addItem("X10")
        self.comboBox_time.addItem("Real Time")
        self.comboBox_time.setGeometry(QtCore.QRect(130 * self.desktop_size.width() / 1366,
                                                    507 * self.desktop_size.height() / 768,
                                                    105 * self.desktop_size.width() / 1366,
                                                    25 * self.desktop_size.height() / 768))

    def set_main_label(self):
        """
        Main Label params
        """
        self.label.setGeometry(QtCore.QRect(20 * self.desktop_size.width() / 1366,
                                            20 * self.desktop_size.height() / 768,
                                            int(220 / 1440 * self.desktop_size.width()),
                                            int(110 / 900 * self.desktop_size.height())))
        self.font.setPointSize(20)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white")

    def set_label_pulse(self):
        """
        Label Pulse params
        """
        self.font.setPointSize(25)
        self.label_pulse.setGeometry(QtCore.QRect(20, 117, 157, 51))
        self.font.setPointSize(18)
        self.label_pulse.setGeometry(QtCore.QRect(16 * self.desktop_size.width() / 1366,
                                                  110 * self.desktop_size.height() / 768,
                                                  157 * self.desktop_size.width() / 1366,
                                                  51 * self.desktop_size.height() / 768))
        self.label_pulse.setFont(self.font)
        self.label_pulse.setObjectName("label_pulse")
        self.label_pulse.setStyleSheet("color: white")

    def set_label_engine_running_time(self):
        """
        label engine running time params
        """
        self.font.setPointSize(20)
        self.label_engine_running_time.setGeometry(QtCore.QRect(16 * self.desktop_size.width() / 1366,
                                                                195 * self.desktop_size.height() / 768,
                                                                200 * self.desktop_size.width() / 1366,
                                                                251 * self.desktop_size.height() / 768))
        self.label_engine_running_time.setFont(self.font)
        self.label_engine_running_time.setObjectName("label_time_wait")
        self.label_engine_running_time.setStyleSheet("color: white")
        self.label_engine_running_time.setStyleSheet("color: white")

    def set_label_time_of_calculation_tr(self):
        """
        Label time of calculation trajectory params
        """
        self.font.setPointSize(20)
        self.label_time_of_calculation_tr.setGeometry(QtCore.QRect(20 * self.desktop_size.width() / 1366,
                                                                   380 * self.desktop_size.height() / 768,
                                                                   210 * self.desktop_size.width() / 1366,
                                                                   70 * self.desktop_size.height() / 768))
        self.label_time_of_calculation_tr.setFont(self.font)
        self.label_time_of_calculation_tr.setObjectName("label_time_of_calc")
        self.label_time_of_calculation_tr.setStyleSheet("color: white")

    def set_label_current_velocity_fuel(self):
        """
        Label current velocity fuel params
        """
        self.label_current_velocity_fuel.setGeometry(QtCore.QRect(1050 * self.desktop_size.width() / 1366,
                                                                  50 * self.desktop_size.height() / 768,
                                                                  250 * self.desktop_size.width() / 1366,
                                                                  70 * self.desktop_size.height() / 768))
        self.label_current_velocity_fuel.setFont(self.font)
        self.label_current_velocity_fuel.setObjectName("label_current_velocity")
        self.label_current_velocity_fuel.setStyleSheet("color: white")

    def set_label_current_velocity_value(self):
        """
        Label current velocity value params
        """
        self.label_current_velocity_value.setGeometry(QtCore.QRect(1270 * self.desktop_size.width() / 1366,
                                                                   40 * self.desktop_size.height() / 768,
                                                                   210 * self.desktop_size.width() / 1366,
                                                                   70 * self.desktop_size.height() / 768))
        self.label_current_velocity_value.setFont(self.font)
        self.label_current_velocity_value.setObjectName("label_current_velocity_value")
        self.label_current_velocity_value.setStyleSheet("color: white")

    def set_label_current_fuel_value(self):
        """
        Label current fuel value params
        """
        self.label_current_fuel_value.setGeometry(QtCore.QRect(1270 * self.desktop_size.width() / 1366,
                                                               65 * self.desktop_size.height() / 768,
                                                               210 * self.desktop_size.width() / 1366,
                                                               70 * self.desktop_size.height() / 768))
        self.label_current_fuel_value.setFont(self.font)
        self.label_current_fuel_value.setObjectName("label_current_fuel_value")
        self.label_current_fuel_value.setStyleSheet("color: white")

    def set_label_current_direction_angle(self):
        """
        Label current direction angle params
        """
        self.font.setPointSize(18)
        self.label_current_direction_angle.setFont(self.font)
        self.label_current_direction_angle.setGeometry(QtCore.QRect(215 * self.desktop_size.width() / 1366,
                                                                    235 * self.desktop_size.height() / 768,
                                                                    50 * self.desktop_size.width() / 1366,
                                                                    31 * self.desktop_size.height() / 768))
        self.label_current_direction_angle.setObjectName("label_direction_angle")
        self.label_current_direction_angle.setStyleSheet("color: white")

    def set_label_direction_angle(self):
        """
        Label direction angle params
        """
        self.font.setPointSize(20)
        self.label_direction_angle.setFont(self.font)
        self.label_direction_angle.setGeometry(QtCore.QRect(20 * self.desktop_size.width() / 1366, 240,
                                                            250 * self.desktop_size.width() / 1366, 61))
        self.label_direction_angle.setObjectName("label_direction_angle")
        self.label_direction_angle.setStyleSheet("color: white")

    def set_label_time_factor(self):
        """
        Label time factor params
        """
        self.label_time_factor.setFont(self.font)
        self.label_time_factor.setGeometry(QtCore.QRect(5 * self.desktop_size.width() / 1366,
                                                        500 * self.desktop_size.height() / 768,
                                                        130 * self.desktop_size.width() / 1366,
                                                        30 * self.desktop_size.height() / 768))
        self.label_time_factor.setObjectName("label_time_factor")
        self.label_time_factor.setStyleSheet("color: white")

    def set_text_edits(self):
        """
        Text edits params
        """
        self.textEdit_pulse.setGeometry(QtCore.QRect(110 * self.desktop_size.width() / 1366,
                                                     160 * self.desktop_size.height() / 768,
                                                     105 * self.desktop_size.width() / 1366,
                                                     30 * self.desktop_size.height() / 768))
        self.textEdit_pulse.setObjectName("textEdit_pulse")

        self.textEdit_time_engine_working.setGeometry(QtCore.QRect(110 * self.desktop_size.width() / 1366,
                                                                   330 * self.desktop_size.height() / 768,
                                                                   105 * self.desktop_size.width() / 1366,
                                                                   30 * self.desktop_size.height() / 768))
        self.textEdit_time_engine_working.setObjectName("textEdit_time_engine_working")

        self.textEdit_calc_tr.setGeometry(QtCore.QRect(110 * self.desktop_size.width() / 1366,
                                                       450 * self.desktop_size.height() / 768,
                                                       105 * self.desktop_size.width() / 1366,
                                                       30 * self.desktop_size.height() / 768))
        self.textEdit_calc_tr.setObjectName("textEdit_calcs_tr")

    def set_menubar(self):
        """
        Menubar params
        """
        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827 * self.desktop_size.width() / 1366,
                                              24 * self.desktop_size.height() / 768))
        self.menubar.setObjectName("menubar")
        self.menuOpengl.setObjectName("menuOpengl")
        self.main_window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpengl.menuAction())
        self.retranslateui()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslateui(self):
        """
        Labels on buttons and surfaces

        """
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "Welcome to Kerbal 2.0 !"))
        self.pushButton_quit.setText("")
        self.pushButton_quit.setObjectName("pushButton")
        self.pushButton_calculate.setText("")
        self.pushButton_calculate.setObjectName("pushButton")
        self.pushButton_start.setText("")
        self.pushButton_start.setObjectName("pushButton")
        self.pushButton_help.setText("")
        self.pushButton_help.setObjectName("pushButton")
        self.label.setText(_translate("MainWindow", "Set Parametrs to\n" "change trajectory"))
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
    """
    The class in which the initialization of all
    initial window widgets with specified default values
    """

    def __init__(self, start_window):
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.statusbar = QtWidgets.QStatusBar(start_window)
        self.menubar = QtWidgets.QMenuBar(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_window = start_window
        self.desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        self.set_start_window_policy()
        self.set_picture()
        self.set_menubar()

    def set_start_window_policy(self):
        """
        Start window params
        """
        self.start_window.setObjectName("StartWindow")
        self.start_window.resize(self.desktop_size.width(), self.desktop_size.height())
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.start_window.sizePolicy().hasHeightForWidth())
        self.start_window.setSizePolicy(size_policy)

    def set_picture(self):
        """
        Picture params
        """
        self.Picture.setGeometry(QtCore.QRect(0, 0, self.desktop_size.width(), self.desktop_size.height()))
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("Pictures/Entire_screen.jpg"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")
        self.pushButton.setGeometry(QtCore.QRect(580 * self.desktop_size.width() / 1366,
                                                 620 * self.desktop_size.height() / 768,
                                                 241 * self.desktop_size.width() / 1366,
                                                 91 * self.desktop_size.height() / 768))

    def set_menubar(self):
        """
        Menubar params
        """
        self.start_window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440 * self.desktop_size.width() / 1366,
                                              22 * self.desktop_size.height() / 768))
        self.menubar.setObjectName("menubar")
        self.start_window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.start_window.setStatusBar(self.statusbar)
        self.pushButton.setStyleSheet("#pushButton{background-color: transparent; border-image: url(Pictures/StartGame.png);"
                                      " background: none; border: none; background-repeat: none;} #pushButton:pressed"
                                      " {border-image: url(Pictures/StartGamePressed.png)}")

        self.retranslate_ui(self.start_window)
        QtCore.QMetaObject.connectSlotsByName(self.start_window)

    def retranslate_ui(self, start_window):
        """
        Labels on buttons and surfaces
        """
        _translate = QtCore.QCoreApplication.translate
        start_window.setWindowTitle(_translate("StartWindow", "StartWindow"))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")


class UiTutorial:
    """
    Class of tutorial window
    """
    def __init__(self, mainwindow):
        self.window = mainwindow
        self.menubar = QtWidgets.QMenuBar(self.window)
        self.desktop_size = QtWidgets.QDesktopWidget().screenGeometry()
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.font = QtGui.QFont()

        self.set_menubar()
        self.set_main_label()
        self.set_buttons()

        self.text = ""
        text_file = open('tutorial.txt')
        for line in text_file:
            self.text += line

        self.retranslate_ui(self.window)

    def set_menubar(self):
        """
        Menubar params
        """
        self.window.resize(700 * self.desktop_size.width() / 1366, 600 * self.desktop_size.height() / 768)
        self.window.setObjectName("MainWindow")
        self.window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 24))
        self.menubar.setObjectName("menubar")
        self.window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslate_ui(self, main_win):
        """
        Show labels on surfaces
        """
        _translate = QtCore.QCoreApplication.translate
        main_win.setWindowTitle(_translate("Tutorial", "Tutorial"))
        self.label.setText(_translate("MainWindow", self.text))
        self.pushButton_back.setText("")
        self.pushButton_back.setObjectName("pushButton")

    def set_main_label(self):
        """
        Params of main label
        """
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(0, 0, int(900 / 1336 * self.desktop_size.width()),
                                            int(500 / 768 * self.desktop_size.height())))
        self.font.setPointSize(20)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: black")

    def set_buttons(self):
        """
        Button params
        """
        self.pushButton_back.setGeometry(QtCore.QRect(300 * self.desktop_size.width() / 1366,
                                                      530 * self.desktop_size.height() / 768,
                                                      113 * self.desktop_size.width() / 1366,
                                                      50 * self.desktop_size.height() / 768))
        self.pushButton_back.setObjectName("pushButton_quit")
        self.pushButton_back.setStyleSheet(
            "#pushButton{background-color: transparent; border-image: url(Pictures/Backtut.png);"
            " background: none; border: none; background-repeat: none;} #pushButton:pressed"
            " {border-image: url(Pictures/BacktutPressed.png)}")
