from PyQt5.QtWidgets import QOpenGLWidget, QGraphicsView
from PyQt5 import QtGui, Qt, QtWidgets
from PyQt5.Qt import Qt
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
import space_objects
import Motion


class PyOpenGL(QOpenGLWidget, QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        QtWidgets.qApp.installEventFilter(self)
        self.viewMatrix = None
        self.setFocus()
        self.scalefactor = 5.0E6
        self.rotation_angle = 0
        self.scale_x = 0
        self.scale_y = 0
        self.scale_z = 0
        self.input_pulse = 0
        self.start_modeling = False

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
            Motion.recalculate_space_objects_positions(space_objects.space_objects, Motion.f_func, Motion.g_func)
        for obj in space_objects.space_objects:
            # if obj.name == 'SpaceShip':
            #     obj.pulse_direction()
            obj.Draw()
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
            space_objects.space_objects[0].vx += 50
        if event.key() == Qt.Key_4:
            space_objects.space_objects[0].vx -= 50
        if event.key() == Qt.Key_8:
            space_objects.space_objects[0].vy += 50
        if event.key() == Qt.Key_2:
            space_objects.space_objects[0].vy -= 50

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
