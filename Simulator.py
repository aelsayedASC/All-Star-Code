def Square(x,y):
    from Myro import *
    x=int(input("What is the size of the square?"))
    y=int(input("What is the speed of the robot?"))
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
Square(1,1)