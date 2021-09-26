import math
import turtle


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * (angle / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def flower(t, n, overlap):
    if not overlap:
        for i in range(n):
            arc(t, 200, 360 / n)  # 360/n=圆心角=花瓣两个切线之间的夹角
            t.lt(180 - 360 / n)  # 这里转过的角度与arc里面的angle互补
            arc(t, 200, 360 / n)
            t.lt(180)  # 掉头
    else:
        for i in range(n):
            arc(t, 200, 360 / (n / 2))
            t.lt(180 - 360 / (n / 2))  # 这里转过的角度与arc里面的angle互补
            arc(t, 200, 360 / (n / 2))
            t.lt(180)  # 掉头
            t.rt((360 / (n / 2)) / 2)

    # bob.lt(45)
    # arc(bob, 200, 70)
    # bob.lt(110)
    # arc(bob, 200, 70)

    turtle.mainloop()


bob = turtle.Turtle()
bob.speed(speed=9)
flower(bob, n=8, overlap=True)
