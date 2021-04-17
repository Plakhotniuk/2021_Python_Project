"""
Тестовый файл с движением планеток в космосе
"""

from vpython import scene, vector, sphere, color, rate, mag, box
from Starship import *
import math
# GlowScript 3.1 VPython


scene.caption = """In GlowScript programs:
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
scene.forward = vector(0,-3,-1)

scene.width = 1500
scene.height = 1000
G = 6.7e-11 # Newton gravitational constant

giant = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.red)
giant.mass = 2e30
giant.p = vector(0, 0, -1e4) * giant.mass


# dwarf = sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.yellow,
#                 make_trail=True, interval=10, retain=50, spin=0.5)
dwarf = box(pos=vector(1.5e11,0,0), length=2e10, height=2e10, width=2e10, color=color.yellow, make_trail=True, interval=10, retain=50)
dwarf.mass = 1e30
dwarf.p = -giant.p

scene.autoscale = False


ship = Player(100, (0, 0, 0), (100, 100, 0))

ship.draw()

sphere(pos=vector(0, 0, 0), texture="Stars.jpg", radius=25e12, shininess=0)

dt = 1e5
while True:
    rate(200)

    r = dwarf.pos - giant.pos
    F = G * giant.mass * dwarf.mass * r.hat / mag(r)**2
    giant.p = giant.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant.pos = giant.pos + (giant.p/giant.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt

    ship.camera_tracking()
    camera_pos = scene.camera.pos




