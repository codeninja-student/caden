import turtle
screen=turtle.Screen()
my_turtle=turtle.Turtle()
my_turtle.pensize(10)
my_turtle.color("red")
my_turtle.shape("turtle")
my_turtle.speed("fast")

sides=5
angle=360/sides

size=int(input('how big is size of shape?:'))

for _ in range(size):
    my_turtle.forward(size)
    my_turtle.right(angle)
screen.mainloop()