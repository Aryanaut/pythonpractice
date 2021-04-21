import turtle
import math

t = turtle.Turtle()
w = turtle.Screen()

def drawTriangle(x1, y1, x2, y2, x3, y3):
    t.up()
    t.setpos(x1, y1)
    t.down()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    
def drawEq(x1, y1, x2, y2):
    m = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    y3 = (math.sqrt(3)/2)*m
    x3 = 0.5*m
    drawTriangle(x1, y1, x2, y2, x3, y3)

drawEq(100, 0, 0, 0)
drawTriangle(100, 0, 0, 0, 0, 100)
turtle.done()