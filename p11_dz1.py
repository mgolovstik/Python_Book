import turtle
t = turtle.Pen()
def myvosem(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
t.color(1, 1, 0)
myvosem(100, True)
t.color(0, 0, 0)
myvosem(100, False)
