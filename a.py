import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("White")
t.pencolor("Black")

for i in range(50):
    t.forward(i * 5)
    t.right(90)
    
for i in range(50):
    t.forward(i * 5)
    t.right(90)

for i in range(50):
    t.forward(i * 5)
    t.right(90)

for i in range(50):
    t.forward(i * 5)
    t.left(90)

for i in range(50):
    t.forward(i * 5)
    t.left(90)
    
for i in range(50):
    t.forward(i * 5)
    t.left(90)
turtle.done()