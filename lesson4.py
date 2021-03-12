import turtle
alex = turtle.Turtle()
alex.shape("turtle")
step = 10
for i in range(70):
    alex.penup()
    step = step+1
    alex.forward(step)
    alex.left(15)
    alex.stamp()
turtle.done()
turtle.bye()