import random
import time
from tkinter import *

tk = Tk()  # создание объекта для работы с tkinter
tk.resizable(0, 0)
tk.title('Game')
tk.attributes('-topmost', 1)  # поверх окон

canvas = Canvas(tk, width=600, height=500, bd=0,
                highlightthickness=0)  # последние два параметра для того чтобы не было рамок у холста
canvas.pack()
canvas.update()


class Board:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.board_width = 150
        self.id = canvas.create_rectangle(0, 0, self.board_width, 15, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.speed_x = 10
        self.xx = self.canvas_width / 2 - self.board_width / 2
        self.yy = self.canvas_height - 40
        self.canvas.move(self.id, self.xx, self.yy)

    def move_left(self, event):
        if self.xx + (-1)*self.speed_x >= 0:
            self.x = (-1)*self.speed_x
            self.xx += self.x
            self.draw()

    def move_right(self, event):
        if self.xx + self.speed_x <= self.canvas_width - self.board_width:
            self.x = self.speed_x
            self.xx += self.x
            self.draw()

    def draw(self):
        self.canvas.move(self.id, self.x, 0)


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # сохраняем объект
        self.canvas.move(self.id, 250, 150)
        start = [-2, -1, 1, 2]
        random.shuffle(start)
        self.x = start[0]
        self.y = start[1]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)  # координаты объекта (верхний левый угол, нижний правый угол)
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = self.y * (-1)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * (-1)


ball = Ball(canvas, 'red')
board = Board(canvas, 'blue')
canvas.bind_all('<KeyPress-Left>', board.move_left)
canvas.bind_all('<KeyPress-Right>', board.move_right)

while True:
    ball.draw()
    # tk.update_idletasks()
    tk.update()
    time.sleep(0.005)

tk.mainloop()