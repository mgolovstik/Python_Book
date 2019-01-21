from tkinter import *
import time
import random
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
canvas.create_arc(10, 230, 50, 270, extent = 359, style = ARC)
for x in range(0, 5):
    r = random.randrange(20, 40)
    t = random.randrange(20, 40)
    v = random.randrange(20, 40)
    n = random.randrange(20, 40)
    for x in range(0, r): 
        canvas.move(1, 5, -5)
        tk.update()
        time.sleep(0.05)
    for x in range(0, t):
        canvas.move(1, 5, 5)
        tk.update()
        time.sleep(0.05)
    for x in range(0, v):
        canvas.move(1, -5, 5)
        tk.update()
        time.sleep(0.05)
    for x in range(0, n): 
        canvas.move(1, -5, -5)
        tk.update()
        time.sleep(0.05)
