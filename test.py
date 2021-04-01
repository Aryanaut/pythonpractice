from turtleLine import line

c1 = input()
c1 = c1.split()
x1, y1 = (int(c1[0]), int(c1[1]))

c2 = input()
c2 = c2.split()
x2, y2 = (int(c2[0]), int(c2[1]))

line = line()
line.drawLine(x1, y1, x2, y2)