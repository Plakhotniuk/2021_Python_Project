from counting import np, count_pos, f, g


def recalculate_space_objects_positions(space_objects, f_func, g_func):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    x = []
    v = []
    for body in space_objects:
        x.append(body.x)
        x.append(body.y)
        v.append(body.vx)
        v.append(body.vy)
    x = np.array(x)
    v = np.array(v)

    new_x, new_v = count_pos(x, v, f_func, g_func)
    i = 0
    for body in space_objects:
        body.x = new_x[i]
        body.y = new_x[i+1]
        body.vx = new_v[i]
        body.vy = new_v[i+1]
        i += 2


if __name__ == "__main__":
    print("This module is not for direct call!")