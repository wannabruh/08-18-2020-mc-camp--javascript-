import turtle

e = turtle.Turtle()
r = turtle.Turtle()
screen = turtle.Screen()
screen.title("Window")
screen.bgcolor("gray")

r.pensize(10)
e.pensize(7)


for i in range(723):
    r.color("purple")
    r.shape("circle")
    r.forward(98)
    r.left(76)
    r.pencolor("cyan")
    r.forward(98)
    r.right(68)
    r.forward(78)
    r.left(78)
    r.circle(23)

    e.pencolor("red")
    e.forward(98)
    e.right(76)
    e.pencolor("orange")
    e.backward(98)
    e.left(68)
    e.forward(78)
    e.right(78)
    e.circle(23)

    e.color("purple")
    e.shape("circle")
    e.forward(98)
    e.left(76)
    e.pencolor("cyan")
    e.backward(98)
    e.right(68)
    e.forward(78)
    e.left(78)
    e.circle(23)
    
    r.pencolor("red")
    r.backward(98)
    r.right(76)
    r.pencolor("orange")
    r.forward(98)
    r.left(68)
    r.backward(78)
    r.right(78)
    r.circle(23)

    r.color("purple")
    r.shape("circle")
    r.backward(98)
    r.left(76)
    r.pencolor("cyan")
    r.backward(98)
    r.right(68)
    r.backward(78)
    r.left(78)
    r.circle(23)

    e.pencolor("red")
    e.backward(98)
    e.right(76)
    e.pencolor("orange")
    e.forward(98)
    e.left(68)
    e.backward(78)
    e.right(78)
    e.circle(43)
    backward(23)
    turtle.done()
