from random import *
from matplotlib import pyplot as plt
import numpy as np

numOfClusters = 8
iterations = 50

def column(matrix, i):
    return [row[i] for row in matrix]

def generateClusterPositions(numOfPlots):
    randomData = []
    for i in range(0, numOfPlots):
        randomData.append([randint(0,1000)/1000, randint(0,1000)/1000])

    return randomData

def generateRandomTuple(numOfPlots):
    randomData = []
    for i in range(0, numOfPlots):
        randomData.append([randint(0,1000)/100, randint(0,1000)/1000, -1])

    return randomData

def plotData(data, clusters):
    plt.ion()
    for i in range(iterations):
        clusteredData = extractClusterData(data, clusters)

        plots = []
        for i in range(0, numOfClusters):
            plots.append(plt.scatter(column(clusteredData[i], 0), column(clusteredData[i], 1), label="cluster {}".format(i)))

        plt.scatter(column(clusters, 0), column(clusters, 1))

        plt.legend(handles=plots)
        plt.draw()
        plt.pause(0.001)
        plt.clf()
        moveClusters(clusters, clusteredData)

def extractClusterData(data, clusters):
    clusteredData = calculateDistanceFromClusters(data, clusters)

    dataClusters = [[] for x in range(0, numOfClusters)]

    for cd in clusteredData:
        cluster = cd[2]
        dataClusters[cluster].append([cd[0], cd[1]])

    return dataClusters

def calculateDistanceFromClusters(data, clusters):
    for d in data:
        distances = []
        for c in clusters:
            distance = ((d[0] - c[0])**2) +  ((d[1] - c[1])**2)
            distances.append(distance)

        d[2] = distances.index(min(distances))

    return data;

def moveClusters(clusters, dataInCluster):
    currClusterNumber = 0
    for c in clusters:
        averageX = 0
        averageY = 0
        for data in dataInCluster[currClusterNumber]:
            averageX += data[0];
            averageY += data[1];

        if(len(dataInCluster[currClusterNumber]) != 0):
            c[0] = round(averageX / len(dataInCluster[currClusterNumber]), 3)
            c[1] = round(averageY / len(dataInCluster[currClusterNumber]), 3)

        currClusterNumber += 1

clusterPositions = generateClusterPositions(numOfClusters)
data = generateRandomTuple(100)
plotData(data, clusterPositions)
