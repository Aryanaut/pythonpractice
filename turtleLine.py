
import turtle

class line:
    def __init__(self):
        self.w = turtle.Screen()
        self.t = turtle.Turtle()

    def drawLine(self, x1, y1, x2, y2):

        self.t.setpos(x1, y1)
        self.t.down()
        self.t.goto(x2, y2)
        turtle.done()