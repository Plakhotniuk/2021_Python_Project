from PyQt5.QtWidgets import QOpenGLWidget, QGraphicsView
from PyQt5 import QtGui, Qt, QtWidgets
from PyQt5.Qt import Qt
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
from calculation import Calculation
import math


class PyOpenGL(QOpenGLWidget, QGraphicsView):
    def __init__(self, sp_objects: list, parent=None):
        super().__init__(parent)
        QtWidgets.qApp.installEventFilter(self)
        width = self.width()
        height = self.height()
        self.viewMatrix = None
        self.setFocus()
        self.scalefactor = 5.0E6
        self.specific_impulse_of_rocket_engine = 30000
        self.scale_x = 0
        self.scale_y = 0
        self.scale_z = 0
        self.input_pulse = 0
        self.total_fuel_consumption = 0
        self.current_velocity = 0
        self.current_angle = 0
        self.start_modeling = False
        self.is_trajectory_shown = False
        self.calculation_module = Calculation(sp_objects, speed=3000, dt=100)
        self.space_objects = sp_objects

    def initializeGL(self):
        OpenGL.GL.glClearColor(0, 0, 0, 1)
        OpenGL.GL.glEnable(OpenGL.GL.GL_DEPTH_TEST)
        OpenGL.GL.glEnable(OpenGL.GL.GL_LIGHT0)
        OpenGL.GL.glEnable(OpenGL.GL.GL_LIGHTING)
        OpenGL.GL.glColorMaterial(OpenGL.GL.GL_FRONT_AND_BACK, OpenGL.GL.GL_AMBIENT_AND_DIFFUSE)
        OpenGL.GL.glEnable(OpenGL.GL.GL_COLOR_MATERIAL)

    def resizeGL(self, w: int, h: int):
        MIN_SCALE = 1.0E7
        MAX_SCALE = 1.5E11
        OpenGL.GL.glViewport(0, 0, w, h)
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
        OpenGL.GL.glLoadIdentity()
        OpenGL.GLU.gluPerspective(90, float(w / h), MIN_SCALE, MAX_SCALE)
        OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)
        OpenGL.GL.glLoadIdentity()
        OpenGL.GLU.gluLookAt(0, -1, 0, 0, 0, 0, 0, 0, 10)
        self.viewMatrix = OpenGL.GL.glGetFloatv(OpenGL.GL.GL_MODELVIEW_MATRIX)

    def paintGL(self):

        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
        OpenGL.GL.glTranslated(self.scale_x, -self.scale_z, -self.scale_y)

        if self.start_modeling:
            self.calculation_module.recalculate_space_objects_positions()
        for obj in self.space_objects:
            if self.is_trajectory_shown and not self.start_modeling:
                 obj.draw_trajectory()
            obj.Draw()

            if obj.name == 'SpaceShip':
                self.current_velocity = int(math.sqrt(obj.vx**2 + obj.vy**2))
                if not self.start_modeling:
                    obj.engine_angle = self.current_angle
                    obj.set_engine_angle()
                print(self.current_velocity)

        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.scale_y = self.scalefactor
        elif event.key() == Qt.Key_S:
            self.scale_y = -self.scalefactor
        elif event.key() == Qt.Key_D:
            self.scale_x = -self.scalefactor
        elif event.key() == Qt.Key_A:
            self.scale_x = self.scalefactor
        if event.key() == Qt.Key_Down:
            self.scale_z = -self.scalefactor
        if event.key() == Qt.Key_Up:
            self.scale_z = self.scalefactor
        if event.key() == Qt.Key_6:
            self.calculation_module.v[0] += 50
        if event.key() == Qt.Key_4:
            self.calculation_module.v[0] -= 50
        if event.key() == Qt.Key_8:
            self.calculation_module.v[1] += 50
        if event.key() == Qt.Key_2:
            self.calculation_module.v[1] -= 50

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
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


if __name__ == "__main__":
    print("This module is not for direct call!")
