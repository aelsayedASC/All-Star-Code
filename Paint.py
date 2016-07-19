from Processing import *
#Creation of the box and rectangle to draw in
window(900,700)
rect(150,0,600,700)

#Left side/Extra options(brush size, erasor, and reset)
#Default brush size
fill(0)
ellipse(75,70,10,10)
#Second size
fill(0)
ellipse(75,180,20,20)
#Third size
fill(0)
ellipse(75,290,30,30)
#Largest size
fill(0)
ellipse(75,400,40,40)
#Eraser
#Saving the image to a variable in order to display it 3 lines later
Eraser=loadImage("Eraser.PNG")
fill(0)
image(Eraser,40,480,80,80)
#Reset
#Saving the image to a variable in order to display it 3 lines later
Reset=loadImage("Reset.PNG")
fill(0)
image(Reset,40,590,80,80)

#Right side/Colors
#Red color circle
fill(255,0,0)
ellipse(825,70,80,80)
#Green color circle
fill(0,255,0)
ellipse(825,180,80,80)
#Blue color circle
fill(0,0,255)
ellipse(825,290,80,80)  
#Yellow color circle
fill(255,255,0)
ellipse(825,510,80,80)
#Magenta color circle
fill(255,0,255)
ellipse(825,620,80,80) 
#Black color circle
fill(0)
ellipse(825,400,80,80)

noStroke()
fill(0)

while True:
    if isMousePressed()==True and mouseX()>155 and mouseX()<743:
        ellipse(mouseX(),mouseY(),10,10)
    if isMousePressed()==True and mouseX()>785 and mouseX()<865 and mouseY()>30 and mouseY()<110:
        fill(255,0,0)
        print("HI")
