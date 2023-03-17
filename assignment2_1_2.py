import matplotlib
import matplotlib.pyplot as plt #Import for plotting
import numpy as np 
import random as rand

from assignment2_1_1 import fitnessFunction #Importing the fitness function from 1.1
#! NB Algorithm steps and info taken from Excercise 3 in IMT4133: https://ntnu.blackboard.com/ultra/courses/_35408_1/cl/outline Last visit 17.03.2023
    
# Task 1.2, we will implement a simple GA (Genetic algorithm), this GA will minimize the fitness function defined from assignment2_1.1.py

def printStartOfAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen):
    print("Starting our generation:"+"\n")
    print("____________________________________________________________________________________________________"+" \n")
    print("Population size: "+str(populationSize)+" Probability of crossover between genes: "+str(crossoverProb*100)+"% \n")
    print("Probability of mutation within new gene: "+str(mutationProb*100)+"%, Number of generation for algorithm: "+str(numberOfGen)+ "\n")
    print("____________________________________________________________________________________________________"+" \n")

def geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen): #? We start by defining the main parameters we will use for the GA 
    printStartOfAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)
    
    #We start by defining and encoding the chromosomes for our GA, for defining the chromosomes we will be using the fitness function from 1.1
    chromosomes = []
    binChrom = []
    
    for i in range(populationSize):
        x = rand.randint(-10,10)                            #Defines the range of x values and picks one random value from the range 
        y = rand.randint(-10,10)                            #Defines the range of y values and picks one random value from the range
        chromosomes.append((x,y))                           #Adds coordinate to list
        if x<0 and y<0:
            binChrom.append((f'{x:05b}', f'{y:05b}'))       #Adds coordinates in binary    
        elif x<0 and y>0:
            binChrom.append((f'{x:05b}', f'{y:04b}'))       #Adds coordinates in binary
        elif x>0 and y<0:
            binChrom.append((f'{x:04b}', f'{y:05b}'))       #Adds coordinates in binary
        else:
            binChrom.append((f'{x:04b}', f'{y:04b}'))       #Adds coordinates in binary
    
    print("List of values: "+str(chromosomes)+" \n")            
    print("List of values in binary"+str(binChrom)+" \n")
    
    results = []                                            #We define the results in a list
    for i in range(populationSize): 
        xValue = chromosomes[i][0]                          #Defining x value
        yValue = chromosomes[i][1]                          #Defining y value
        value = fitnessFunction(xValue, yValue)             #Computing result of fitness function
        results.append(value)                               
        
    print(results)
    
    

    
populationSize = 4
crossoverProb =0.5
mutationProb =0.2
numberOfGen = 10
geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)

    