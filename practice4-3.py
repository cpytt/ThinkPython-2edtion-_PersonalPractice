import math
import turtle


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def triangle(t, angle, length):
    """

    :param t: turtle
    :param angle: apex angle
    :param length:side length of triangle
    """
    base_angle = (180 - angle) / 2
    base_length = 2 * length * math.sin(radian(angle / 2))

    t.fd(length)
    t.lt(180 - base_angle)
    t.fd(base_length)
    t.lt(180 - base_angle)
    t.fd(length)
    t.lt(180)


def pie(t, n, size):
    """

    :param t:turtle
    :param n: num of triangles
    :param size:side length of triangle
    """
    apex_angle = 360 / n
    t.lt(apex_angle/2)
    for i in range(n):
        triangle(t, apex_angle, size)
    turtle.mainloop()


def radian(x):
    """

    :param x:degree measure
    :return:radian
    """
    return x * (math.pi / 180)


bob = turtle.Turtle()
pie(bob, 5, 200)
