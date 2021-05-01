from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuOpengl = QtWidgets.QMenu(self.menubar)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.textEdit_time = QtWidgets.QTextEdit(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm2 = QtWidgets.QPushButton(self.centralwidget)

        self.textEdit_pulse = QtWidgets.QTextEdit(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)

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

        self.frame.setGeometry(QtCore.QRect(249, 20, 1161, 811))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        """Buttons"""
        self.pushButton_quit.setGeometry(QtCore.QRect(10, 750, 113, 32))
        self.pushButton_quit.setObjectName("pushButton_quit")

        self.pushButton_confirm1.setGeometry(QtCore.QRect(125, 180, 100, 32))
        self.pushButton_confirm1.setObjectName("pushButton_confirm1")

        self.pushButton_confirm2.setGeometry(QtCore.QRect(125, 330, 100, 32))
        self.pushButton_confirm2.setObjectName("pushButton_confirm2")
        self.pushButton_start.setGeometry(QtCore.QRect(10, 460, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        """Labels and Fonts"""
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(20, 130, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(10, 270, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        """Text edit"""
        self.textEdit_pulse.setGeometry(QtCore.QRect(20, 180, 104, 31))
        self.textEdit_pulse.setObjectName("textEdit_pulse")
        self.textEdit_time.setGeometry(QtCore.QRect(20, 330, 104, 31))
        self.textEdit_time.setObjectName("textEdit_time")

        """Horizontal Slider 1"""
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 230, 180, 32))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        """Horizontal Slider 2"""
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 390, 180, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

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

        self.add_functions()

    def add_functions(self):
        """
        Дополнительная функция обработки нажатия на кнопки
        """
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)

        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(100)

    def retranslateUi(self, MainWindow):
        """
        Выводит надписи на кнопках и доп поверхностях
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_confirm1.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_confirm2.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_start.setText(_translate("MainWindow", "Start!"))
        self.label.setText(_translate("MainWindow", "Set Parametrs to\n" " Start modeling!"))
        self.label_2.setText(_translate("MainWindow", "PULSE:"))
        self.label_3.setText(_translate("MainWindow", "Time wait:"))
        self.menuOpengl.setTitle(_translate("MainWindow", "Opengl"))
