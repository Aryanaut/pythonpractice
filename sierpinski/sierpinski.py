import math
import turtle

t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)

def drawTriangle(x1, y1, x2, y2, x3, y3):
    t.up()
    t.setpos(x1, y1)
    t.down()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)

def dist(A, B):
    x1, y1 = A
    x2, y2 = B
    return (x2-x1)**2+(y2-y1)**2

def drawLine(A, B):
    x1, y1 = A
    x2, y2 = B
    t.up()
    t.setpos(x1, y1)
    t.down()
    t.goto(x2, y2)

def sier(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    a = dist((x1, y1), (x2, y2))
    b = dist((x2, y2), (x3, y3))
    c = dist((x3, y3), (x1, y1))
    if min(a, b, c) < 30:
        drawLine(A, B)
        drawLine(B, C)
        drawLine(C, A)
    else: 
        p1 = ((x1+x2)/2, (y1+y2)/2)
        p2 = ((x2+x3)/2, (y2+y3)/2)
        p3 = ((x3+x1)/2, (y3+y1)/2)
        sier(p1, p3, A)
        sier(p1, p2, B)
        sier(p2, p3, C)

def main():
    points = input()
    points = points.split()
    
    p1 = (int(points[0]), int(points[1]))
    p2 = (int(points[2]), int(points[3]))
    p3 = (int(points[4]), int(points[5]))

    drawLine(p1, p2)
    drawLine(p2, p3)
    drawLine(p3, p1)
    sier(p1, p2, p3)
    turtle.done()

if __name__ == '__main__':
    main()