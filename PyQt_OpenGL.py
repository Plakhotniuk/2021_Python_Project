from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QMouseEventTransition, QVBoxLayout, QGraphicsView, QGraphicsSceneMouseEvent, QKeyEventTransition, QTextEdit
from PyQt5 import QtCore, QtGui, QtOpenGL, Qt, QtWidgets
from PyQt5.Qt import Qt, QMouseEvent, QScrollEvent
import Space_objects
import Motion
import OpenGL.GL
import OpenGL.GLU
import OpenGL.GLUT
#
# space_objects = []
# """Cписок небесных тел"""
# space_objects.append(Space_objects.CelestialBody(name='Earth', r=6.4E5, m=5.974E24,
#                                                  texture_filename='wall-murals-planet-earth-texture.jpg' ,
#                                                  color=Space_objects.GREEN))
# space_objects.append(Space_objects.CelestialBody(name='Moon', r=1.7E5, m=7.36E22,
#                                                  texture_filename='wall-murals-planet-earth-texture.jpg',
#                                                  color=Space_objects.WHITE, x=3.8E8, vy=1.0E3))

dt = 10
space_objects = []
"""Cписок небесных тел"""
f_func = Motion.f(dt)
space_objects.append(Space_objects.CelestialBody(name='Moon', r=5.7E5, m=400000,
                                                 color=Space_objects.WHITE, x=3.8E7, vy=3000, vx=-0))
space_objects.append(Space_objects.CelestialBody(name='Earth', r=6.4E6, m=5.974E24,
                                                 color=Space_objects.GREEN, vy=-0, vx=0, x=0, y=0))
g_func = Motion.g(dt)
g_func.set_mass([space_objects[1].m, space_objects[0].m])


class PyOpenGL(QOpenGLWidget, QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        QtWidgets.qApp.installEventFilter(self)
        self.viewMatrix = None
        self.setFocus()
        self.scalefactor = 5.0E6
        self.rotation_angle = 10
        self.scale_x = 0
        self.scale_y = 0
        self.scale_z = 0
        self.input()
        self.input_pulse = 0


    def input(self):
        pass

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        pass

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        pass

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

    def eventFilter(self, obj: QtCore.QObject, event: QtGui.QKeyEvent) -> bool:
        if event.type() == QtGui.QKeyEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Escape:
                return True
        return super().eventFilter(obj, event)

    def paintGL(self):

        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
        OpenGL.GL.glTranslated(self.scale_x, -self.scale_z, -self.scale_y)
        Motion.recalculate_space_objects_positions(space_objects, f_func, g_func)
        for obj in space_objects:
            obj.Draw()
        self.update()

    def keyPressEvent(self, event):
        print("pressed key " + str(event.key()))
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
