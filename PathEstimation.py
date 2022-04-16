import math
from matplotlib import pyplot as plt

#Functions
def readContents(fileName):
        #Opening File & Reading Contents
        rawData = open(fileName, "r")
        listOfLines = rawData.readlines()[1:]

	#Collecting Only Position Data
        coordinates = []
        for line in listOfLines:
                data = line.split(",")
                coordinates.append([float(data[2]), float(data[3])])
	
        return coordinates

def processData(coordinates):
	#Sensor Specific
	totalDistance = 0
	timeInterval = 1

	speeds,distances = [],[]
	for i in range(1,len(coordinates)):
		#Co ordintates of Tail & Head
		x1,y1 = coordinates[i-1]
		x2,y2 = coordinates[i-0]

		#Calculating Individual Components
		distanceX = (x2-x1)*111045 
		distanceY = (y2-y1)*87870.18

		#Distance Covered in The Interval (1 second in our Case)
		distanceT = math.sqrt( distanceX**2 + distanceY**2)
		totalDistance += distanceT
		speedT = distanceT/timeInterval

		#Collecting Instaneous Data
		distances.append(totalDistance)
		speeds.append(speedT)

	return [distances,speeds]
#Moving Average Filter
def movingAverageFilter(dataSet,n):
	distance,speed = [],[]
	for i in range(0,len(dataSet[0])-n,n):
		speed.append(sum(dataSet[1][i:i+n+1])/len(dataSet[1][i:i+n+1]))
		distance.append(sum(dataSet[0][i:i+n+1])/len(dataSet[0][i:i+n+1]))
	
	return [distance,speed]

#Making The Data Set
dataSets = [[]]*3
for i in range(0,3):
	fileName = input("Enter FileName "+str(i+1)+": ")
	positionData = readContents(fileName)
	dataSets[i] = processData(positionData)

#Estimated Distance
estimatedDistance = []
minDistValues  = min([len(x[0]) for x in dataSets])
for i in range(minDistValues):
	estimatedDistance.append((dataSets[0][0][i]+dataSets[1][0][i]+dataSets[2][0][i])/3)

#Estimated Speed
estimatedSpeed = []
minSpeedValues = min([len(x[1]) for x in dataSets])
for i in range(minSpeedValues):
	estimatedSpeed.append((dataSets[0][1][i]+dataSets[1][1][i]+dataSets[2][1][i])/3)

#Plotting Trails
for i in range(3):
	plt.subplot(3,2,i+1)
	plt.plot(dataSets[i][0], dataSets[i][1])
	
	#Plot Specifics
	graph = plt.gca()
	graph.set_title("Track "+str(i+1))
	graph.set_xlabel("Distance (in m)")
	graph.set_ylabel("Speed (in m/s)")

#Plotting Estimated Graphs
plt.subplot(3,2,5)
plt.plot(estimatedDistance, estimatedSpeed)

#Plot Specifics
graph = plt.gca()
graph.set_title("Track Estimate")
graph.set_xlabel("Distance (in m)")
graph.set_ylabel("Speed (in m/s)")

plt.subplot(3,2,6)
smoother = movingAverageFilter([estimatedDistance,estimatedSpeed],7)
plt.plot(smoother[0],smoother[1])

#Plot Specifics
graph = plt.gca()
graph.set_title("Smoothened Esitmate")
graph.set_xlabel("Distance (in m)")
graph.set_ylabel("Speed (in m/s)")

plt.subplots_adjust(left=0.1,bottom=0.1, right=0.9, top=0.9, wspace=0.4,hspace=0.6)

#Displaying Plots
plt.show()

	

	



