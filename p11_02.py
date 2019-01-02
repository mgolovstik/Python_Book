import turtle
t = turtle.Pen()
def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.left(90)
    t.forward(50)
mycircle(0, 0, 0)
