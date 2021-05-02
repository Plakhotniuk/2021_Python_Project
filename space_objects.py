import class_Cel_body
import class_Starship
from Globals import Globals

space_objects = []
"""Cписок небесных тел"""
space_objects.append(class_Starship.Starship(name='SpaceShip', r=5.7E5, m=40000,
                                             color=Globals.WHITE, x=3.8E7, vy=3000, vx=-0, engine_thrust=4000000,
                                             time_engine_working=1))
space_objects.append(class_Cel_body.CelestialBody(name='Earth', r=6.4E6, m=5.974E24,
                                                  color=Globals.GREEN, vy=0, vx=300, x=0, y=0))
space_objects.append(class_Cel_body.CelestialBody(name='Moon', r=1.7E6, m=7.34E22,
                                                  color=Globals.RED, x=38500000 * 10, vy=1000, vx=-0))
space_objects.append(class_Cel_body.CelestialBody(name='Satellite', r=1.0E6, m=700000,
                                                  color=Globals.YELLOW, x=0, y=5.0E7, vx=2000))
