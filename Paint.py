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
ellipse(75,290,40,40)
#Largest size
fill(0)
ellipse(75,400,80,80)
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
ellipse(825,400,80,80)
#Magenta color circle
fill(255,0,255)
ellipse(825,510,80,80) 
#Black color circle
fill(0)
ellipse(825,620,80,80)
brushSize=1
fill(0)
while True:
    global brushSize
    strokeWeight(brushSize)
    #Statement for the drawing.
    if isMousePressed()==True and 155<mouseX()<743:
        line(pmouseX(),pmouseY(),mouseX(),mouseY())  
    #Statements for the colors on the right side.
    if isMousePressed()==True and 785<mouseX()<865 and 30<mouseY()<110:
        stroke(255,0,0)
    if isMousePressed()==True and 785<mouseX()<865 and 140<mouseY()<220:
        stroke(0,255,0)
    if isMousePressed()==True and 785<mouseX()<865 and 250<mouseY()<330:
        stroke(0,0,255)     
    if isMousePressed()==True and 785<mouseX()<865 and 360<mouseY()<440:
        stroke(255,255,0)       
    if isMousePressed()==True and 785<mouseX()<865 and 470<mouseY()<550:
        stroke(255,0,255)         
    if isMousePressed()==True and 785<mouseX()<865 and 580<mouseY()<660:
        stroke(0)   
    #Statements for the extra options on the left side.    
    if isMousePressed()==True and 70<mouseX()<80 and 65<mouseY()<75:
        brushSize=1  
    if isMousePressed()==True and 65<mouseX()<85 and 170<mouseY()<190:
        brushSize=20  
    if isMousePressed()==True and 55<mouseX()<95 and 270<mouseY()<310:
        brushSize=40 
    if isMousePressed()==True and 35<mouseX()<115 and 360<mouseY()<440:
        brushSize=80 
    if isMousePressed()==True and 35<mouseX()<115 and 480<mouseY()<560:
        stroke(255)
    if isMousePressed()==True and 35<mouseX()<115 and 600<mouseY()<680:
        noStroke()
        fill(255,255,255)
        rect(150,0,600,700)
