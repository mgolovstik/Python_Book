import turtle
t = turtle.Pen()
def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.left(110)
    t.forward(50)
t.color(0, 0, 0)
t.begin_fill()
t.circle(300)
t.end_fill()
t.left(90)
t.forward(300)
for x in range(1,11):
    mycircle(1, 1, 1)
    mycircle(0, 0, 0)
