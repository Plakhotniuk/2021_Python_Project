import OpenGL.GLU
import OpenGL.GL


WHITE = (1, 1, 1)
RED = (1, 0, 0)
BLUE = (0, 0, 1)
YELLOW = (1, 1, 0)
GREEN = (0, 1, 0)
DARKGREEN = (0, 100, 0)
MAGENTA = (1, 0, 1)
CYAN = (0, 1, 1)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class CelestialBody:
    """
    Класс небесного тела.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', texture_filename='', name=''):
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

    def Draw(self):
        """
        Draws
        """
        sphere = OpenGL.GLU.gluNewQuadric()  # Create new sphere
        OpenGL.GL.glPushMatrix()

        OpenGL.GL.glTranslatef(self.x, 5.0E7, self.y)  # Move to the place
        OpenGL.GL.glColor4f(self.color[0], self.color[1], self.color[2], 1)  # Put color
        OpenGL.GLU.gluSphere(sphere, self.r, 320, 160)  # Draw sphere (sphere, radius)
        OpenGL.GLU.gluDeleteQuadric(sphere)
        OpenGL.GL.glPopMatrix()


if __name__ == "__main__":
    print("This module is not for direct call!")