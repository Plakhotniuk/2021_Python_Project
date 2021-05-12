import OpenGL.GLU
import OpenGL.GL
import numpy as np


class CelestialBody:
    """
    Класс небесного тела.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', name=''):
        self.m = m
        """Масса"""
        self.x = x
        """Координата по оси **x**"""
        self.y = y
        """Координата по оси **y**"""
        self.vx = vx
        """Скорость по оси **x**"""
        self.vy = vy
        """Скорость по оси **y**"""
        self.fx = fx
        """Сила по оси **x**"""
        self.fy = fy
        """Сила по оси **y**"""
        self.r = r
        """Радиус"""
        self.color = color
        """Цвет"""
        self.name = name
        "Название"
        self.prev_trajectory_coords = [[self.x, self.y, 0]]
        self.prev_velocity = [[self.vx, self.vy, 0]]

    def Draw(self):
        """
        Draws
        """
        sphere = OpenGL.GLU.gluNewQuadric()
        OpenGL.GL.glPushMatrix()

        OpenGL.GL.glTranslatef(self.x, 5.0E7, self.y)
        OpenGL.GL.glColor4f(self.color[0], self.color[1], self.color[2], 1)
        OpenGL.GLU.gluSphere(sphere, self.r, 320, 160)
        OpenGL.GLU.gluDeleteQuadric(sphere)
        OpenGL.GL.glPopMatrix()

    def draw_trajectory(self):
        OpenGL.GL.glLineWidth(10000000000)

        OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_STRIP)
        OpenGL.GL.glColor3d(self.color[0], self.color[1], self.color[2])

        for point in self.prev_trajectory_coords:
            OpenGL.GL.glVertex3d(point[0], 5.0E7, point[1])

        OpenGL.GL.glEnd()


class Starship(CelestialBody):
    def __init__(self, time_engine_working=0, engine_thrust=0, m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', name=''):
        super().__init__(m=m, x=x, y=y, vx=vx, vy=vy, fx=fx, fy=fy, r=r, color=color, name=name)
        self.time_engine_working = time_engine_working
        self.engine_thrust = engine_thrust
        self.engine_angle = 0
        self.arrow_length = 30000000

    def set_engine_angle(self, angle):
        OpenGL.GL.glLineWidth(1000000000)
        OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_STRIP)
        OpenGL.GL.glColor3d(1, 0, 0)
        OpenGL.GL.glVertex3d(self.x, 5.0E7, self.y)
        OpenGL.GL.glVertex3d(self.x + int(self.arrow_length * np.cos(angle * np.pi / 180)), 5.0E7,
                             self.y + int(self.arrow_length * np.sin(angle * np.pi / 180)))
        OpenGL.GL.glEnd()


if __name__ == "__main__":
    print("This module is not for direct call!")