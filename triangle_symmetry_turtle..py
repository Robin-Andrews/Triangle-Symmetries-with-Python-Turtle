import turtle
import tkinter as tk

screen = turtle.Screen()


class Label(turtle.Turtle):
    def __init__(self, coordinates=None, screen=screen):
        turtle.Turtle.__init__(self)
        if coordinates is None:
            self.coordinates = [0, 0]
        else:
            self.coordinates = coordinates
        self.text = ""
        self.color("white")
        self.coordinates = coordinates
        self.hideturtle()
        self.penup()
        self.screen = screen

    def show(self, message, alignment="center", size=18):
        self.screen.tracer(0)
        self.clear()
        self.goto(self.coordinates)
        self.write(
            message,
            font=("Helvetica", size),
            align=alignment,
        )
        self.screen.tracer(1)


def show_labels(vertices):
    global label1, label2, label3
    label1.show(vertices[0])
    label2.show(vertices[1])
    label3.show(vertices[2])


def clear_labels():
    global label1, label2, label3
    label1.clear()
    label2.clear()
    label3.clear()


def reset():
    global vertices
    vertices = ["A", "B", "C"]
    show_labels(vertices)


def rotate_clockwise():
    global vertices
    temp = vertices[-1]
    for i in range(len(vertices) - 1, 0, -1):
        vertices[i] = vertices[i - 1]
    vertices[0] = temp

    update_rotation("clockwise")


def rotate_anticlockwise():
    global vertices
    temp = vertices[0]
    for i in range(len(vertices) - 1):
        vertices[i] = vertices[i + 1]
    vertices[-1] = temp

    update_rotation("anticlockwise")


def reflect_A():
    global vertices
    b_pos = vertices.index("B")
    c_pos = vertices.index("C")
    vertices[b_pos], vertices[c_pos] = (
        vertices[c_pos],
        vertices[b_pos],
    )

    update_reflection()


def reflect_B():
    global vertices
    a_pos = vertices.index("A")
    c_pos = vertices.index("C")
    vertices[a_pos], vertices[c_pos] = (
        vertices[c_pos],
        vertices[a_pos],
    )

    update_reflection()


def reflect_C():
    global vertices
    a_pos = vertices.index("A")
    b_pos = vertices.index("B")
    vertices[a_pos], vertices[b_pos] = (
        vertices[b_pos],
        vertices[a_pos],
    )

    update_reflection()


def update_rotation(direction):
    global triangle
    clear_labels()
    if direction == "clockwise":
        triangle.right(120)
    else:
        triangle.left(120)
    show_labels(vertices)


def update_reflection():
    global triangle
    clear_labels()
    show_labels(vertices)


def make_button(canvas, text, command):
    return tk.Button(
        canvas.master,
        font=("Helvetica", 12),
        text=text,
        background="hotpink",
        foreground="white",
        bd=0,
        command=command,
    )


def create_button(canvas, x, y, text, command):
    canvas.create_window(
        x, y, window=make_button(canvas, text, command)
    )


if __name__ == "__main__":

    screen.setup(500, 600)
    screen.title("Symmetries of an Equilateral Triangle")
    screen.bgcolor("blue")
    canvas = screen.getcanvas()

    label1 = Label([-85, -55])
    label2 = Label([0, 75])
    label3 = Label([85, -55])

    triangle = turtle.Turtle("triangle")
    triangle.shapesize(120 / 20)
    triangle.color("hotpink")
    triangle.right(30)

    canvas = screen.getcanvas()

    create_button(canvas, 0, -250, "Reset", reset)
    create_button(
        canvas,
        0,
        -150,
        "Rotate 120° clockwise",
        rotate_clockwise,
    )
    create_button(
        canvas,
        0,
        -200,
        "Rotate 120° anticlockwise",
        rotate_anticlockwise,
    )
    create_button(
        canvas,
        0,
        100,
        "Reflect about perp. bisector of BC",
        reflect_A,
    )
    create_button(
        canvas,
        0,
        150,
        "Reflect about perp. bisector of AC",
        reflect_B,
    )
    create_button(
        canvas,
        0,
        200,
        "Reflect about perp. bisector of AB",
        reflect_C,
    )

    vertices = ["A", "B", "C"]
    show_labels(vertices)

    turtle.done()
