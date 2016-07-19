from Processing import *
from random import *
#Sets the size of the window
window(700,600)

#Sets the values so the ball always starts at the start
centerX=200
centerY=300
#Sets the speed of the ball to always be 15
speedconst = 15
#Creates a list of choices that is randomly picked to go right/left and up/down
right = choice([True, False])
up = choice([True, False])
paddleTop=250
def doKeyPressed():
    if isKeyPressed()==True:
        if key()=='a':
            print("hi")
            paddleTop+=10
while True:
        global paddleTop
        #Fancy stuff for the ball itself
        delay(40)
        stroke(0)
        strokeWeight(2)
        fill(255,0,0)
        #If right is picked to be true then go at the speed of 15 right.
        if right:
           centerX += speedconst
        #If left is picked to be false then go at the speed of 15 left.
        else:
           centerX -= speedconst
        #if up is picked to be true then go at the speed of 15 up.
        if up:
           centerY -= speedconst
        #If up is picked to be false then go at the speed of 15 down.
        else:
           centerY += speedconst
        #Extra fancy stuff
        background(255)
        rect(mouseX(),500,200,30)
        rect(paddleTop,500,200,30)
        ellipse(centerX,centerY,50,50)
        #If the ball(Y value) is anywhere between 0 and 30 then it'll go down.
        if centerY<=30:
            up=False
        #If the ball(Y value) is anywhere between 570 and 600 then it'll go up.
        if centerY>=570:
            up=True
        #If the ball(X value) is anywhere between 0 and 34 then it'll go right.
        if centerX<=34:
            right=True
        #If the ball(X value) is anywhere between 666 and 700 then it'll go left.
        if centerX>=666:
            right=False
        #If the ball is between the ends of the paddle it will bounce up.
        if centerY>=465 and (mouseX()<=(centerX)< mouseX() + 200):
            up=True