from turtle import *
shape = "turtle"
speed(5)
pensize(5)
color("blue")

lado = 3
tri = 360 / lado
print(tri)

for count in range(3):
    forward(200)
    left(120)

forward(50)

for count in range(3):
    right(120)
    forward(200)

forward(100)

for count in range(3):
    left(120)
    forward(200)

backward(50)

for count in range(3):
    right(120)
    forward(200)

backward(100)

for count in range(3):
    left(120)
    forward(200)

backward(50)

for count in range(3):
    left(120)
    forward(200)

done()
