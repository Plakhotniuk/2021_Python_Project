import OpenGL.GLU
import OpenGL.GL
import numpy as np
from pyquaternion import Quaternion


class CelestialBody:
    """
        Класс небесного тела.
        Содержит массу, координаты, скорость звезды,
        а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, color=(1, 0, 0), name='', quaternion=Quaternion(0, 1, 0, 0),
                 angle_velocity=np.array([]),
                 tensor_of_inertia=np.array([]), mass_center_coordinates_velocity=np.array([])):

        self.color = color
        """Цвет"""
        self.name = name
        """Название"""
        self.engine_angle = 0
        """Направление работы двигателя (в какую сторону будет лететь аппарат)"""
        self.arrow_length = 10000000

        self.quaternion = quaternion

        self.mass_center_coordinates_velocity = mass_center_coordinates_velocity

        self.tensor_of_inertia = tensor_of_inertia  # (A, B, C)

        self.eigenvectors = np.array([])

        self.angle_velocity = angle_velocity  # (p, q, r)

        self.external_momentum = np.array([])

        self.basis_orts = np.array([])

    # def get_basis_orts(self):
    #     self.basis_orts = np.linalg.eigvals(self.tensor_of_inertia)
    #     self.tensor_of_inertia = np.diag(np.linalg.eigh(self.tensor_of_inertia))

    def draw(self):
        """
        Отрисовывает объект
        """
        obj = OpenGL.GLU.gluNewQuadric()
        OpenGL.GL.glPushMatrix()
        OpenGL.GL.glTranslatef(*self.mass_center_coordinates_velocity[:3])
        if self.name == 'SpaceShip':
            OpenGL.GL.glRotate(self.quaternion.degrees, *self.quaternion.axis)
            OpenGL.GL.glColor4f(*self.color, 1)
            OpenGL.GLU.gluCylinder(obj, 1000000, 0, 10 * 1000000, 1000, 10)
            # print(self.quaternion)
        else:
            OpenGL.GL.glColor4f(*self.color, 1)
            OpenGL.GLU.gluSphere(obj, 1000000, 320, 160)

        OpenGL.GLU.gluDeleteQuadric(obj)
        OpenGL.GL.glPopMatrix()

    def draw_center(self):
        obj = OpenGL.GLU.gluNewQuadric()
        OpenGL.GL.glPushMatrix()
        OpenGL.GL.glTranslatef(0, 5.0E7, 0)
        OpenGL.GL.glColor4f(*self.color, 1)
        OpenGL.GLU.gluSphere(obj, 1000000, 320, 160)
        OpenGL.GLU.gluDeleteQuadric(obj)
        OpenGL.GL.glPopMatrix()

    def set_arrow_angle(self, angle, color):
        """
        Устанавливаем угол для отрисовки направления для выбора угла полета
        angle - угол для отрисовки
        """
        OpenGL.GL.glLineWidth(1000000000)
        OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_STRIP)
        OpenGL.GL.glColor3d(*color)
        OpenGL.GL.glVertex3d(1000000, 5.0E7, 1000000)
        OpenGL.GL.glVertex3d(1000000 + int(self.arrow_length * np.cos(angle * np.pi / 180)), 5.0E7,
                             1000000 + int(self.arrow_length * np.sin(angle * np.pi / 180)))
        OpenGL.GL.glEnd()


if __name__ == "__main__":
    print("This module is not for direct call!")
