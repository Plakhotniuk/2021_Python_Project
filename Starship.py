from Space_objects import CelestialBody, COLORS
class Starship(CelestialBody):
    def __init__(self, time_engine_working=0, engine_thrust=0, m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', name=''):
        super().__init__(m=m, x=x, y=y, vx=vx, vy=vy, fx=fx, fy=fy, r=r, color=color, name=name)
        self.time_engine_working = time_engine_working
        self.engine_thrust = engine_thrust


if __name__ == "__main__":
    print("This module is not for direct call!")
