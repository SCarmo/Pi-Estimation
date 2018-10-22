from Tkinter import *
from decimal import *
import random
import time
import math
tk = Tk()

WIDTH = 400
HEIGHT = WIDTH # make canvas a square

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Pi Calculation")
canvas.pack()

#canvas.create_rectangle(0,0,WIDTH,HEIGHT,width=2)
canvas.create_oval(0,0,WIDTH,HEIGHT,width=2)

# count total dots drawn and how many are in the circle
total = 0
inCircle = 0

# find center of circle
CenterOfCircle = [WIDTH/2,HEIGHT/2]
radius = WIDTH/2
prevDifference = 0.1
canvas.config()
while True:
    total = total + 1
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT) 

    # use pythagorus theorem to find distance from center to drawn point
    # 
    a = abs(x - CenterOfCircle[0])
    b = abs(y - CenterOfCircle[1])

    # c^2 = a^2 + b^2
    dist = math.sqrt(a*a + b*b)

    if dist <= radius:
        inCircle = inCircle+1
        canvas.create_oval(x,y,x,y,outline="green")
    else:
        canvas.create_oval(x,y,x,y,outline="blue")

    # only print closest approximation of pi
    approximation= 4*(Decimal(inCircle)/Decimal(total))
    difference = abs(float(approximation) - math.pi)
    if difference < prevDifference:
        prevDifference = float(difference)
        print(approximation)
    tk.update()

canvas.mainloop()