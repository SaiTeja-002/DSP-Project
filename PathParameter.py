import math

#A fucntion to calculate the number of footsteps
def calculateSteps(distance, stepSize=0.762):
    return (distance//stepSize)

#A function to calculate the number of calories burned
def burnedCalories(bodyWeight=62,time=10,MET=7):
    return ((bodyWeight*time*MET)/200)


#Opening The File
fileName = input("Please enter the file name: ")
rawData = open(fileName, "r")

#Reading The Contents
listOfLines = rawData.readlines()[1:]
coordinates = []

#Collecting Only Position Data
for line in listOfLines:
    data = line.split(",")
    coordinates.append([float(data[2]), float(data[3])])

#Intializing Variables
timeInterval, totalDistance = 1, 0
maxSpeed, averageSpeed = 0, 0

#Main Loop
for i in range(1, len(coordinates)):
    x1,y1 = coordinates[i-1]
    x2,y2 = coordinates[i-0]

    distanceX = (x2-x1)*111045
    distanceY = (y2-y1)*87870.18

    distanceT = math.sqrt(distanceX**2 + distanceY**2)
    totalDistance += distanceT

    instantaneousSpeed = distanceT/timeInterval

    if instantaneousSpeed > maxSpeed:
        maxSpeed = instantaneousSpeed

#Printing Required Data
print("Total Distance covered(in m) = ", totalDistance)
print("Average Speed(in m/s) = ", totalDistance/(len(coordinates)*timeInterval))
print("Max Speed(in m/s) = ", maxSpeed)
print("Number of footsteps = ", calculateSteps(totalDistance))
weight = int(input("Please enter your weight (in kg) \nEnter '0' if don't wish to enter your weight\n"))

if weight < 0:
    print("Invalid Input")

elif weight == 0:
    print(f"Calories burned : {burnedCalories()}")

else:
    print(f"Calories burned : {burnedCalories(bodyWeight=weight)}")
