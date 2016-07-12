def Square(x,y):
    from Myro import *
    init("sim")
    penDown()
    forward(x,y)
    turnBy(90)
    forward(x,y)
    turnBy(90)
    forward(x,y)
    turnBy(90)
    forward(x,y)
    penUp() 

Square(0.5,7)
Square(1,3)
def Triangle(x,y):
    from Myro import *
    init("sim")
    turnBy(45)