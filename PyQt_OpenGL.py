from PyQt5.QtWidgets import QOpenGLWidget, QGraphicsView
from PyQt5 import QtGui, Qt, QtWidgets
from PyQt5.Qt import Qt
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
from calculation import Calculation
import math


class PyOpenGL(QOpenGLWidget, QGraphicsView):
    """
    Основной класс  отрисовки космического пространства и обработки полета камеры,
    ручное управление кораблем, отрисовка траектории
    """
    def __init__(self, sp_objects: list, parent=None):
        super().__init__(parent)
        QtWidgets.qApp.installEventFilter(self)
        self.viewMatrix = None
        self.setFocus()
        self.scale_factor = 5.0E6
        self.specific_impulse_of_rocket_engine = 30000
        self.scale_x = 0
        self.scale_y = 0
        self.scale_z = 0
        self.input_pulse = 0
        self.minimum_mass = 40000
        self.current_velocity = 0
        self.current_angle = 0
        self.manual_control_delta_pulse = 2000000
        self.start_modeling = False
        self.is_trajectory_shown = False
        self.calculation_module = Calculation(sp_objects, speed=3000, dt=100)
        self.space_objects = sp_objects

    def initializeGL(self):
        """
        Инициализация основного окна отрисовки, создание матрицы изображения
        """
        OpenGL.GL.glClearColor(0, 0, 0, 1)
        OpenGL.GL.glEnable(OpenGL.GL.GL_DEPTH_TEST)
        OpenGL.GL.glEnable(OpenGL.GL.GL_LIGHT0)
        OpenGL.GL.glEnable(OpenGL.GL.GL_LIGHTING)
        OpenGL.GL.glColorMaterial(OpenGL.GL.GL_FRONT_AND_BACK, OpenGL.GL.GL_AMBIENT_AND_DIFFUSE)
        OpenGL.GL.glEnable(OpenGL.GL.GL_COLOR_MATERIAL)

    def resizeGL(self, w: int, h: int):
        """
        Масштабирование экрана, движение камеры, зум камеры
        """
        min_scale = 1.0E7
        max_scale = 1.5E11
        OpenGL.GL.glViewport(0, 0, w, h)
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
        OpenGL.GL.glLoadIdentity()
        OpenGL.GLU.gluPerspective(90, float(w / h), min_scale, max_scale)
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)
        OpenGL.GL.glLoadIdentity()
        OpenGL.GLU.gluLookAt(0, -1, 0, 0, 0, 0, 0, 0, 10)
        self.viewMatrix = OpenGL.GL.glGetFloatv(OpenGL.GL.GL_MODELVIEW_MATRIX)

    def paintGL(self):
        """
        Вызов функций для отрисовки планеток и траектории
        """
        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
        OpenGL.GL.glTranslated(self.scale_x, -self.scale_z, -self.scale_y)

        if self.start_modeling:
            self.calculation_module.recalculate_space_objects_positions()
        for obj in self.space_objects:
            if self.is_trajectory_shown and not self.start_modeling:
                obj.draw_trajectory()
            obj.draw()

            if obj.name == 'SpaceShip':
                self.current_velocity = int(math.sqrt(obj.vx ** 2 + obj.vy ** 2))
                if not self.start_modeling:
                    obj.set_arrow_angle(self.current_angle, obj.color)
                    if obj.vx:
                        plus_pi = int(obj.vx < 0) * 180
                        obj.set_arrow_angle((math.atan(obj.vy / obj.vx) * 180 / math.pi) + plus_pi, (1, 1, 1))
                    else:
                        obj.set_arrow_angle(((180 / abs(obj.vy)) * obj.vy) / 2, (1, 1, 1))

        self.update()

    def keyPressEvent(self, event):
        """
        Обработка нажатий кнопок на клавиауре
        """
        if event.key() == Qt.Key_W:
            self.scale_y = self.scale_factor
        elif event.key() == Qt.Key_S:
            self.scale_y = -self.scale_factor
        elif event.key() == Qt.Key_D:
            self.scale_x = -self.scale_factor
        elif event.key() == Qt.Key_A:
            self.scale_x = self.scale_factor
        if event.key() == Qt.Key_Down:
            self.scale_z = -self.scale_factor
        if event.key() == Qt.Key_Up:
            self.scale_z = self.scale_factor
        if event.key() == Qt.Key_6:
            if self.space_objects[0].m - self.manual_control_delta_pulse \
                    / self.specific_impulse_of_rocket_engine > self.minimum_mass:
                self.calculation_module.v[0] += self.manual_control_delta_pulse \
                                                / self.space_objects[0].m
                self.space_objects[0].m -= self.manual_control_delta_pulse / self.specific_impulse_of_rocket_engine
        if event.key() == Qt.Key_4:
            if self.space_objects[0].m - self.manual_control_delta_pulse \
                    / self.specific_impulse_of_rocket_engine > self.minimum_mass:
                self.calculation_module.v[0] -= self.manual_control_delta_pulse \
                                                / self.space_objects[0].m
                self.space_objects[0].m -= self.manual_control_delta_pulse / self.specific_impulse_of_rocket_engine
        if event.key() == Qt.Key_8:
            if self.space_objects[0].m - self.manual_control_delta_pulse \
                    / self.specific_impulse_of_rocket_engine > self.minimum_mass:
                self.calculation_module.v[1] += self.manual_control_delta_pulse \
                                                / self.space_objects[0].m
                self.space_objects[0].m -= self.manual_control_delta_pulse / self.specific_impulse_of_rocket_engine
        if event.key() == Qt.Key_2:
            if self.space_objects[0].m - self.manual_control_delta_pulse \
                    / self.specific_impulse_of_rocket_engine > self.minimum_mass:
                self.calculation_module.v[1] -= self.manual_control_delta_pulse \
                                                / self.space_objects[0].m
                self.space_objects[0].m -= self.manual_control_delta_pulse / self.specific_impulse_of_rocket_engine

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        """
        Обработка события клавиш на клавиатуре (отпускаем клавишу)
        """
        if event.key() == Qt.Key_W:
            self.scale_y = 0
        elif event.key() == Qt.Key_S:
            self.scale_y = 0
        elif event.key() == Qt.Key_D:
            self.scale_x = 0
        elif event.key() == Qt.Key_A:
            self.scale_x = 0
        if event.key() == Qt.Key_Down:
            self.scale_z = 0
        if event.key() == Qt.Key_Up:
            self.scale_z = 0

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        """
        Обработка нажатия мышкой на экран
        """
        self.setFocus()


if __name__ == "__main__":
    print("This module is not for direct call!")
