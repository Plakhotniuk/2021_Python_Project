import numpy
import OpenGL.GLU
import OpenGL.GL
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


from PIL import Image


def read_texture(filename):
    """
    Reads an image file and converts to a OpenGL-readable textID format
    """
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = OpenGL.GL.glGenTextures(1)
    OpenGL.GL.glBindTexture(OpenGL.GL.GL_TEXTURE_2D, textID)
    OpenGL.GL.glPixelStorei(OpenGL.GL.GL_UNPACK_ALIGNMENT, 1)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                    OpenGL.GL.GL_TEXTURE_WRAP_S, OpenGL.GL.GL_CLAMP)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                           OpenGL.GL.GL_TEXTURE_BASE_LEVEL,
                           0)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                           OpenGL.GL.GL_TEXTURE_WRAP_S,
                           OpenGL.GL.GL_REPEAT)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                    OpenGL.GL.GL_TEXTURE_WRAP_T,
                    OpenGL.GL.GL_REPEAT)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                    OpenGL.GL.GL_TEXTURE_MAG_FILTER, OpenGL.GL.GL_NEAREST)
    OpenGL.GL.glTexParameterf(OpenGL.GL.GL_TEXTURE_2D,
                    OpenGL.GL.GL_TEXTURE_MIN_FILTER, OpenGL.GL.GL_NEAREST)
    OpenGL.GL.glTexEnvf(OpenGL.GL.GL_TEXTURE_ENV,
                                           OpenGL.GL.GL_TEXTURE_ENV_MODE,
                                           OpenGL.GL.GL_DECAL)
    OpenGL.GL.glTexImage2D(OpenGL.GL.GL_TEXTURE_2D, 0,
                                              OpenGL.GL.GL_RGB,
                 img.size[0], img.size[1], 0, OpenGL.GL.GL_RGB,
                                              OpenGL.GL.GL_UNSIGNED_BYTE, img_data)
    return textID


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
        """Масса планеты"""

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
        """Радиус планеты"""

        self.color = color
        """Цвет планеты"""

        self.name = name
        "Название планеты"

        self.texture_filename = texture_filename
        "Текстура планеты"

    def PlanetDraw(self):
        """
        Draws planets
        """
        # text = read_texture(self.texture_filename)
        sphere = OpenGL.GLU.gluNewQuadric()  # Create new sphere
        OpenGL.GL.glPushMatrix()
        # OpenGL.GLU.gluQuadricTexture(sphere, OpenGL.GL.GL_TRUE)
        # OpenGL.GL.glEnable(OpenGL.GL.GL_TEXTURE_2D)
        # OpenGL.GL.glBindTexture(OpenGL.GL.GL_TEXTURE_2D, text)
        OpenGL.GL.glTranslatef(self.x, 5.0E7, self.y)  # Move to the place
        OpenGL.GL.glColor4f(self.color[0], self.color[1], self.color[2], 1)  # Put color
        OpenGL.GLU.gluSphere(sphere, self.r * 10, 320, 160)  # Draw sphere (sphere, radius)
        OpenGL.GLU.gluDeleteQuadric(sphere)
        # OpenGL.GL.glDisable(OpenGL.GL.GL_TEXTURE_2D)
        OpenGL.GL.glPopMatrix()


if __name__ == "__main__":
    print("This module is not for direct call!")