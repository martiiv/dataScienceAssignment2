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

# Function for applying roulette wheel selection
# Uses formula 1/result+1 from tutorial 3
def rouletteWheelSelection(populationSize, functionResults):
     # For this GA we will be using Roulette Wheel Selection (inspired by tutorial 3)   
    # We will be using the values from the results list to compute sum of inverted values iValue = inverted value
    iValues = []
    for i in range(populationSize):                         #For full range of parents
        iValue = (1/(functionResults[i]+1))                         #We apply formula 1/(value+1)
        iValues.append(iValue)                             
    sumOfInvertedValues = sum(iValues)                      # We sum our results

    #We will now find probability of selecting hypothesis: 
    probabilities = []
    for i in range(populationSize):
        probability = iValues[i]/sumOfInvertedValues
        probabilities.append(probability)
    return probabilities

# Function handles "Reproduction" with gene crossover and mutation
def crossover(numParents, numChrom, resultList, probabilities):
    numPairs = numParents/2
    numPairs = int(numPairs)
    throwAwayList = numChrom
    
    pairs = []
    while len(throwAwayList)>1: 
        rnd = rand.randrange(0,len(throwAwayList))        
        mom = throwAwayList.pop(rnd)
        rnd = rand.randrange(0,len(throwAwayList))
        dad = throwAwayList.pop(rnd)
        
        pairs.append((mom,dad))
        
            
    
def geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen): #? We start by defining the main parameters we will use for the GA 
    printStartOfAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)
    
    #We start by defining and encoding the chromosomes for our GA, for defining the chromosomes we will be using the fitness function from 1.1
    chromosomes = []
    binChrom = []
    
    for i in range(populationSize):
        x = rand.randint(-10,10)                            # Defines the range of x values and picks one random value from the range 
        y = rand.randint(-10,10)                            # Defines the range of y values and picks one random value from the range
        chromosomes.append((x,y))                           # Adds coordinate to list
        
        binaryStringX = f'{x:06b}'                          # We convert to binary 
        binaryStringY = f'{y:06b}'                          # Since we are working with -10 to 10 values we use 4 binary spaces 

        if x<0 and y<0:                                     
            binaryStringX = binaryStringX.replace('-','1',1)
            binaryStringY = binaryStringY.replace('-','1',1)
        elif x<0 and y>0:
            binaryStringX = binaryStringX.replace('-','1',1)
        elif x>0 and y<0:
            binaryStringY = binaryStringY.replace('-','1',1)
        
        binChrom.append((binaryStringX, binaryStringY))       #Adds coordinates in binary Neither is negative

        
    print("List of values: "+str(chromosomes)+" \n")            
    print("List of values in binary"+str(binChrom)+" \n")
    
    results = []                                            #We define the results in a list
    for i in range(populationSize): 
        xValue = chromosomes[i][0]                          #Defining x value
        yValue = chromosomes[i][1]                          #Defining y value
        value = fitnessFunction(xValue, yValue)             #Computing result of fitness function
        results.append(value)                               
    
    probabilities = rouletteWheelSelection(populationSize, results)

    print("Results from fitness function:")
    
    for i in range(populationSize):
        print("____________________________________________________________________________________________________"+" \n")
        print("Result of value: "+str(chromosomes[i])+": "+ str(results[i])+"\n")
        print("Probability of value: "+str(chromosomes[i])+": "+ str(round(probabilities[i],3))+"\n")
    
    crossover(populationSize, binChrom, results, probabilities)
        
populationSize = 4
crossoverProb =0.5
mutationProb =0.2
numberOfGen = 10
geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)

    