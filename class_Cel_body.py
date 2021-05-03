import OpenGL.GLU
import OpenGL.GL


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