from class_Cel_body import CelestialBody
from Globals import Globals
# from Ui_mainwindow import UiMainWindow
import OpenGL.GLU
import OpenGL.GL


class Starship(CelestialBody):
    def __init__(self, time_engine_working=0, engine_thrust=0, m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', name=''):
        super().__init__(m=m, x=x, y=y, vx=vx, vy=vy, fx=fx, fy=fy, r=r, color=color, name=name)
        self.time_engine_working = time_engine_working
        self.engine_thrust = engine_thrust
        self.engine_angle = 0

    def set_engine_angle(self, tootoo):
        self.engine_angle = tootoo

    # def pulse_direction(self):
    #
    #     OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
    #
    #     OpenGL.GL.glLoadIdentity()
    #     OpenGL.GL.glOrtho(0.0, PyOpenGL.width, PyOpenGL.height, 0.0, -1.0, 10.0)
    #     OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)
    #
    #     OpenGL.GL.glLoadIdentity()
    #     OpenGL.GL.glDisable(OpenGL.GL.GL_CULL_FACE)
    #
    #     OpenGL.GL.glClear(OpenGL.GL.GL_DEPTH_BUFFER_BIT)
    #
    #     OpenGL.GL.glBegin(OpenGL.GL.GL_QUADS)
    #     OpenGL.GL.glColor3f(Globals.COLORS[0][0], Globals.COLORS[0][1], Globals.COLORS[0][2])
    #     OpenGL.GL.glVertex2f(0.0, 0.0)
    #     OpenGL.GL.glVertex2f(10.0, 0.0)
    #     OpenGL.GL.glVertex2f(10.0, 10.0)
    #     OpenGL.GL.glVertex2f(0.0, 10.0)
    #     OpenGL.GL.glEnd()
    #     OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
    #     # OpenGL.GL.glPopMatrix()
    #     OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)


if __name__ == "__main__":
    print("This module is not for direct call!")
