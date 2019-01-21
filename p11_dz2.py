import turtle
t = turtle.Pen()
def draw_star(size, points):
    t.begin_fill()
    x = points + 1
    for x in range(1, x):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    t.end_fill()
t.color(1, 1, 0)
draw_star(200, 18)
