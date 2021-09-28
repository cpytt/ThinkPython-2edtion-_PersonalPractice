import math
import turtle

bob = turtle.Turtle()
print(bob)


# 画一个正方形
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


# 画一个正N边形,n边数，length每个边的长度
def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    turtle.mainloop()


# 画一个圆，r半径
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    for i in range(n):
        t.fd(length)
        t.lt(360.0 / n)
    t.lt(90)
    t.fd(r * 2)
    turtle.mainloop()
    # 也可用arc(t, r, 360)


# 画一段圆弧，r半径长度，n边数， angle角度
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * (angle / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

    turtle.mainloop()


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# circle(bob, r=200)
# polygon(bob, 16, 100)
arc(bob, r=200, angle=128)
