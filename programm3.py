from tkinter import *
import random
import time

class ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        #starts = [-3, -2, -1, 1, 2, 3]
        #random.shuffle(starts)
        self.i = 2
        self.x = self.i#starts[0]
        self.y = -self.i
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.score = 664

    def rand_ig(self):
        self.i = random.randint(1, 5)

    def add_score(self):
        self.score += 1        
        
    def show_score(self):
        canvas.create_rectangle(450, 10, 500, 30, fill = 'gray')
        canvas.create_text(470, 20, text = str(self.score), font = ('Times', 15), fill = 'blue')

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.i
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.add_score()
            self.show_score()
            self.y = -self.i
        if pos[0] <= 0:
            self.x = self.i
        if pos[2] >= self.canvas_width:
            self.x = -self.i

class paddle:
    def turn_left(self, evt):
        self.x = -4
    def turn_right(self, evt):
        self.x = 4
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        
tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

paddle = paddle(canvas, 'blue')
ball = ball(canvas, paddle, 'red')
ball.show_score()
time.sleep(2.00)

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
time.sleep(1.00)
canvas.create_text(250, 200, text = 'Конец игры.', font = ('Times', 30))
#canvas.create_text(250, 200, 'Конец игры.', font = ('Times', 30))
