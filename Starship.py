from vpython import scene, vector, sphere, color, rate, mag, cone, cylinder


class Player:
    def __init__(self, mass=0, position=vector(0, 0, 0), velocity=vector(0, 0, 0),
                 force=vector(0, 0, 0), name=''):
        self.mass = mass
        """Масса космического корабля"""

        self.position = position
        """Координатный вектор космического корабля"""

        self.velocity = velocity
        """Скорость"""

        self.force = force
        """Сила, действующая на космический корабль"""
        self.body = body = cylinder(pos=vector(0, 0, 0),
                                    axis=vector(0, 0, 0) + vector(1, 1, 1),
                        size=vector(20, 10, 10), color=color.white)

    def draw(self):
        """
        Рисует космический корабль
        :return:
        """

        body = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 0) + vector(1, 1, 1),
                        size=vector(20, 10, 10), color=color.white)
        cone(pos=vector(0, 0, 0), axis=-vector(1, 1, 1),
                         size=vector(10, 10, 10), color=color.white)
        cone(pos=vector(0, 0, 0) + vector(12, 12, 12), axis=vector(0, 0, 0) - vector(1, 1, 1),
             size=vector(22, 15, 7), color=color.white)

        cone(pos=vector(0, 0, 0) + vector(12, 12, 12), axis=vector(0, 0, 0) - vector(1, 1, 1),
             size=vector(22, 7, 15), color=color.white)

    def camera_tracking(self):
        """
        Устанавливает слежение камеры за кораблем
        :return:
        """
        scene.camera.follow(self.body)

