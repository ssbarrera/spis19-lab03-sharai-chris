# the anonymous turtle is the original turtle the program makes
# Turtle() is the function and turtle is the name of the object
# we would use the command myturtle.setpos(0,100) 

#Write initial

import turtle 
def drawS(theTurtle,size):
    theTurtle.forward(100/size)
    theTurtle.left(90)
    theTurtle.forward(100/size)
    theTurtle.left(90)
    theTurtle.forward(100/size)
    theTurtle.right(90)
    theTurtle.forward(100/size)
    theTurtle.right(90)
    theTurtle.forward(100/size)
myTurtle = turtle.Turtle()  # Create a new Turtle object
drawS(myTurtle,2)   # make the new Turtle draw the shape
#drawS(theturtle, size)
turtle.done()


