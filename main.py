import turtle
import tkinter


drawing_board = turtle.Screen()
drawing_board.bgcolor("khaki1")
drawing_board.title("Drawing Star")
turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.forward(300)
    turtle_instance.right(144)
turtle.done()
