from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
def random_ractangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)
for x in range(0, 100):
    random_ractangle(300, 300, 'green')
    random_ractangle(300, 300, 'pink')
    random_ractangle(300, 300, 'red')
    random_ractangle(300, 300, 'blue')
    random_ractangle(300, 300, 'cyan')
    random_ractangle(300, 300, 'orange')
    random_ractangle(300, 300, 'violet')
