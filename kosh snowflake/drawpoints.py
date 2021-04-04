import turtle

c1 = input()
c1 = c1.split()
x1, y1 = (int(c1[0]), int(c1[1]))

c2 = input()
c2 = c2.split()
x2, y2 = (int(c2[0]), int(c2[1]))

w = turtle.Screen()
t = turtle.Turtle()
t.setpos(x1, y1)
t.down()
t.goto(x2, y2)
turtle.done()
