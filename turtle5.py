import turtle
e = turtle.Turtle()
r= int(input("how many sides do you need it to be?"))
for i in range(r):
    e.forward(25)
    e.left(360/r)
turtle.done()




