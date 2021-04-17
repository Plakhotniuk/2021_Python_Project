from vpython import scene, vector, sphere, color, rate, mag


class SolarSystem:
    pass


class SpaceObject:
    """
    Класс небесных тел,
    Координаты, скорость и сила задаются векторами в R3
    """
    def __init__(self, mass=0, position=vector(0, 0, 0), velocity=vector(0, 0, 0),
                 force=vector(0, 0, 0), radius=0, color='', name=''):

        """Изображение планеты"""

        self.mass = mass
        """Масса планеты"""

        self.position = position
        """Координатный вектор небесного тела"""

        self.velocity = velocity
        """Скорость"""

        self.force = force
        """Сила"""

        self.radius = radius
        """Радиус планеты"""

        self.color = color
        """Цвет планеты"""

        self.name = name
        "Название планеты"

    def draw(self):
        obj = sphere(pos=self.position, radius=self.radius, velocity=self.velocity,
                     color=self.color, make_trail=True, interval=10, retain=50)







