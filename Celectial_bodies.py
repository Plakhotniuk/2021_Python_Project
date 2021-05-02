import Space_objects
import Starship

space_objects = []
"""Cписок небесных тел"""
space_objects.append(Starship.Starship(name='SpaceShip', r=5.7E5, m=40000,
                                       color=Space_objects.WHITE, x=3.8E7, vy=3000, vx=-0, engine_thrust=4000000,
                                       time_engine_working=1))
space_objects.append(Space_objects.CelestialBody(name='Earth', r=6.4E6, m=5.974E24,
                                                 color=Space_objects.GREEN, vy=0, vx=300, x=0, y=0))
space_objects.append(Space_objects.CelestialBody(name='Moon', r=1.7E6, m=7.34E22,
                                                 color=Space_objects.RED, x=38500000 * 10, vy=1000, vx=-0))
space_objects.append(Space_objects.CelestialBody(name='Satellite', r=1.0E6, m=700000,
                                                 color=Space_objects.YELLOW, x=0, y=5.0E7, vx=2000))
