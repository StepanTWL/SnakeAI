import tkinter as tk

window = tk.Tk()

screen_width = 400
screen_height = 400
point_width = 20
point_height = 20
snake_blocks = []

window.geometry(f"{screen_width}x{screen_height}")

point = tk.Canvas(window, width=screen_width, height=screen_height, bg='black')
point.pack()
point.create_rectangle(20, 20, 40, 40, fill='white')
point.create_rectangle(22, 22, 38, 38, fill='white')


def draw_block(color: tuple, row: int, column: int) -> None:
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])

class SnakeBlock:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_inside(self) -> bool: #проверка на удар
        return 0 <= self.x < screen_width//point_width and 0 <= self.y < screen_height//point_height

    def __eq__(self, __o: object) -> bool: #для возможности сравнивать двух объектов
        return isinstance(__o, SnakeBlock) and self.x == __o.x and self.y == __o.y

snake_blocks.append(SnakeBlock(1, 1))

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

window.title("SnakeAI")
window.mainloop()
