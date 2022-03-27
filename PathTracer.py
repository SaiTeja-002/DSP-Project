import turtle
import math

#Opening The File
fileName = input("Please enter the file name: ")
rawData = open(fileName, "r")

#Choosing The Decimation Level
stepSize = int(input("Decimate The Input By Factor of : "))

#Reading The Contents
listOfLines = rawData.readlines()[1:]
coordinates = []

#Collecting Only Position Data
for line in listOfLines:
    data = line.split(",")
    coordinates.append([float(data[2]), float(data[3])])

#Turtle Screen
pathScreen = turtle.Screen()
pathScreen.title("Path Trace")

#Intializing Turtle
path = turtle.Turtle()
path.hideturtle()

#Drawing The Path
for i in range(1,len(coordinates),stepSize):
	#Co ordintates of Tail & Head
	x1,y1 = coordinates[i-1]
	x2,y2 = coordinates[i-0]

	#Calculating Individual Components
	distanceX = (x2-x1)*111045 
	distanceY = (y2-y1)*87870.18

	#Final Vector Length & Angle
	totalDistance = math.sqrt( distanceX**2 + distanceY**2)	
	angleCovered  = math.atan2(distanceY,distanceX)*(180/math.pi)
	
	#Adjusting The Angle
	if angleCovered >= 0:
		path.setheading(angleCovered)
	else:
		path.setheading(360+angleCovered)
		
        #Drawing The Line
	screeHeight = turtle.screensize()[1]
	path.forward((totalDistance*screeHeight/(1.78*60*10))*3)

turtle.done()



