import turtle
screen=turtle.Screen()
my_turtle=turtle.Turtle()
my_turtle.pencolor("blue")
my_turtle.pencolor(0.2, 0.8, 0.5490196078431373)
my_turtle.pensize(5)
my_turtle.fillcolor("blue")
my_turtle.speed("fast")
for t in range(36):
    for _ in range(3):
        my_turtle.forward(150)
        my_turtle.right(120)
    my_turtle.left(10)


screen.mainloop()