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

from PyQt5.QtWidgets import QOpenGLWidget, QApplication, QMouseEventTransition
from PyQt5 import QtCore, QtGui, QtOpenGL, Qt
from PyQt5.Qt import Qt, QMouseEvent, QScrollEvent
import Space_objects
import Motion
import OpenGL.GL
import OpenGL.GLU

space_objects = []
"""Cписок небесных тел"""
space_objects.append(Space_objects.CelestialBody(name='Earth', r=6.4E5, m=5.974E24, color=Space_objects.GREEN))
space_objects.append(
    Space_objects.CelestialBody(name='Moon', r=1.7E5, m=7.36E22, color=Space_objects.WHITE, x=3.8E8, vy=1.0E3))


class PyOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.viewMatrix = None
        self.setFocus()


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

        Motion.recalculate_space_objects_positions(space_objects, 1.0E3)
        for obj in space_objects:
            obj.PlanetDraw()

        self.update()

        # def mousePressEvent(self, a0: QtGui.QMouseEvent):

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_W:
            OpenGL.GL.glTranslatef(0, -5.0E6, 0)
            self.update()
        if event.key() == Qt.Key_S:
            OpenGL.GL.glTranslatef(0, 5.0E6, 0)
        if event.key() == Qt.Key_D:
            OpenGL.GL.glTranslatef(-5.0E6, 0, 0)
        if event.key() == Qt.Key_A:
            OpenGL.GL.glTranslatef(5.0E6, 0, 0)
        if event.key() == Qt.Key_Down:
            OpenGL.GL.glTranslatef(0, 0, -5.0E6)
        if event.key() == Qt.Key_Up:
            OpenGL.GL.glTranslatef(0, 0, 5.0E6)

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(500, 500)

