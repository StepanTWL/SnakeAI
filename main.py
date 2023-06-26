import random
import time
import tkinter as tk

window = tk.Tk()

screen_width = 400
screen_height = 400
point_width = 20
point_height = 20
snake_blocks = []
d_row = 1
d_col = 0

window.geometry(f"{screen_width}x{screen_height}")

canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg='black')
canvas.pack()
#point.create_rectangle(20, 20, 40, 40, fill='white')
#point.create_rectangle(22, 22, 38, 38, fill='white', outline='black')


def draw_block(color: str, row: int, column: int) -> None:
    canvas.create_rectangle((row-1)*point_width, (column-1)*point_height, row*point_width, column*point_height, fill=color)
    canvas.create_rectangle((row-1)*point_width+2, (column-1)*point_height+2, row*point_width-2, column*point_height-2, fill=color, outline='black')

def vector_move(direction: str):
    if direction == 'UP' and d_row: #change switch
        d_row = -1
        d_col = 0
    elif direction == 'DOWN' and d_row:
        d_row = 1
        d_col = 0
    elif direction == 'LEFT' and d_col:
        d_row = 0
        d_col = -1
    elif direction == 'RIGHT' and d_col:
        d_row = 0
        d_col = 1

class SnakeBlock:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_inside(self) -> bool: #проверка на удар
        return 0 <= self.x < screen_width//point_width and 0 <= self.y < screen_height//point_height

    def __eq__(self, __o: object) -> bool: #для возможности сравнивать двух объектов
        return isinstance(__o, SnakeBlock) and self.x == __o.x and self.y == __o.y

snake_blocks.append(SnakeBlock(random.randint(2,20), random.randint(2, 20)))

while True:
    head = snake_blocks[-1]
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    for block in snake_blocks:
        draw_block("white", block.x, block.y)

    time.sleep(0.5)

window.title("SnakeAI")
window.mainloop()


