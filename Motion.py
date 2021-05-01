import math
gravitational_constant = 6.67408e-11


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.    """

    body.fx = body.fy = 0
    fx = 0
    fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        r = math.sqrt(((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2))
        fx -= (gravitational_constant * obj.m * body.m * (body.x - obj.x))/r**3
        fy -= (gravitational_constant * obj.m * body.m * (body.y - obj.y)) / r**3
    body.fx = fx
    body.fy = fy

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.fx/body.m
    ay = body.fy/body.m
    body.vx += ax * dt

    body.x += body.vx * dt
    body.vy += ay * dt
    body.y += body.vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")