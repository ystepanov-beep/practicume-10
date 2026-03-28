import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("white")


def move_to(x: int, y: int) -> None:
    """
    Moves the turtle to the given coordinates without drawing.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color: str) -> None:
    """
    Draws a filled triangle using the given vertex coordinates and color.
    """
    t.fillcolor(color)
    t.begin_fill()
    move_to(x1, y1)
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()


def draw_tile_square(x: int, y: int, size: int, color1: str, color2: str, diagonal_type: int) -> None:
    """
    Draws a square made of two colored triangles.
    diagonal_type = 1 draws the diagonal from bottom-left to top-right.
    diagonal_type = 2 draws the diagonal from top-left to bottom-right.
    """
    if diagonal_type == 1:
        draw_triangle(x, y, x + size, y, x + size, y + size, color1)
        draw_triangle(x, y, x, y + size, x + size, y + size, color2)
    else:
        draw_triangle(x, y, x + size, y, x, y + size, color1)
        draw_triangle(x + size, y, x, y + size, x + size, y + size, color2)


def draw_pattern(start_x: int, start_y: int, tile_size: int, rows: int, cols: int) -> None:
    """
    Draws a tile ornament made of squares divided into two triangles.
    """
    colors = ["#d9f3ff", "#aee6ff", "#7fd0f6", "#4aa3df", "#2f6fb6"]

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * tile_size
            y = start_y - row * tile_size

            diagonal_type = 1 if (row + col) % 2 == 0 else 2
            color1 = colors[(row + col) % len(colors)]
            color2 = colors[(row + col + 2) % len(colors)]

            draw_tile_square(x, y, tile_size, color1, color2, diagonal_type)


draw_pattern(-150, 150, 60, 6, 6)

t.hideturtle()
screen.mainloop()
