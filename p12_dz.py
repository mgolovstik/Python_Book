from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
colors = ['red','green','blue','yellow','cyan','violet','orange']
def randomtreugle(wid, heig):
    randfill = random.choice(colors)
    x1 = random.randrange(wid)
    y1 = random.randrange(heig)
    x2 = x1 + random.randrange(wid)
    y2 = y1 + random.randrange(heig)
    x3 = x2 + random.randrange(heig)
    y3 = y2 + random.randrange(wid)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = randfill)
for x in range(0, 100):
    randomtreugle(400, 400)
    
    
