import turtle
t = turtle.Pen()
def mystar(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)
mystar(150, True)
t.color(0, 0, 0)
mystar(150, False)
t.up()
t.forward(110)
t.down()
t.color(0, 0, 0)
mystar(50, True)
