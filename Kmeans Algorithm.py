#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:23:28 2021

@author: adam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def distP(point1, point2):
    distance = pow( pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2) , 0.5 )
    return distance

def meanCols(points):
    #input an element of groupings
    a = np.array(points)
    a = a.mean(axis = 0)
    return a.tolist()

def convertList2d(inputList):
    #converts a 2d list to a list of numpy.array's
    output = []
    for i in range(len(inputList)):
        output.append( np.array(inputList[i]) )
    return output


    
        
        

def plotting(groupings, centroids):
    #convert variables to numpy arrays 
    centroid = np.array(centroids)
    legend = []
    word = "grouping "
    word2 = "Centroids"
    
    #plot all groupings with different colors
    for i in range(len(groupings)):
        plt.scatter(groupings[i][:,0],groupings[i][:,1] )
        insert = word + str(i)
        legend.append(insert)
    legend.append(word2)
    #plot all centroids
    plt.scatter(centroid[:,0],centroid[:,1], color = "red" )
    plt.title('Plot of K-Means groupings')
    plt.legend(labels = legend)
    
def FinalPrint(groupings, centroids):
    centroid = np.array(centroids)
    word = "grouping "
    word2 = "Centroids"
    
    print("Groupings: ")
    for i in range(len(groupings)):
        print("\nCentroid: (" + str(round(centroids[i][0],2)) + "," +  str(round(centroids[i][1], 2)) + ")")
        print("Points: ")
        for j in range(len(groupings[i])):
            print("(", str(groupings[i][j][0]),",",str(groupings[i][j][0]), ")")
        
    
    
    
def Kmeans(filname):
    data = pd.read_csv(filname);
    numPoints = int(data.values[0,0]);
    numCentroids = int(data.values[0,1]);
    
    points = []
    centroids = []
    groupings = []
    distances = []
    
    #extract points
    for i in range(numPoints):
        insert = [data.values[i,4], data.values[i,5]]
        points.append(insert)
    
    for i in range(numCentroids):
        insert = [data.values[i,2], data.values[i,3]]
        insert2 = []
        centroids.append(insert)
        groupings.append(insert2)
        distances.append(insert2)
        
    
    #algorithm 
    done = False;
    centroids = sorted(centroids,key=lambda l:l[0] + l[1])
    
    while done == False: #runs until final centroids are found
        distances.clear()
        
        #clear groupings
        for i in range(numCentroids): #go tthrough each grouping and clear
            groupings[i].clear()
        
        centroidTemps = centroids.copy()
        
        for i in range(numPoints):#measure distances between all points and all centroids
            minDist  = distP(points[i], centroids[0]);
            minCentroid = 0
            for j in range(numCentroids): #decides what point is closest to what centroid 
                dist = distP(points[i], centroids[j])
                if(dist < minDist): #if the distance between point i and cetroid j is smaller than minDist
                    minDist = dist
                    minCentroid = j 
            #append point to appropriate grouping 
            groupings[minCentroid].append(points[i])
        for i in range(numCentroids):
            if not groupings[i]:
                print("One Centroid does not atrack any points, please change the centroids used or try another clustering algorithm")
                return
            
        #recaculate centroids
        for i in range(numCentroids):#go through every grouping 
            avg = meanCols(groupings[i])
            centroids[i] = avg
        
                
        #sort new centroids, this methods removes error due to same x or y values
        centroids = [x for x in centroids if str(x) != 'nan']
        centroidss = sorted(centroids,key=lambda l:l[0] + l[1])
        centroids = centroidss
        
        if (centroids == centroidTemps):
            done = True
            
    groupings2 = convertList2d(groupings)
    FinalPrint(groupings, centroids)
    plotting(groupings2, centroids)
        



filename = 'points Template.csv'

Kmeans(filename)

