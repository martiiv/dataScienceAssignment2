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

def selectParents(numCandidates, scores):
    candidates = []
    probabilities = []
    for i in range(numCandidates):          #We convert float probability to int probability
        candidates.append(scores[i][0])     #!This is pessimistic (2.5 will be rounded to 2)
        prob = int((scores[i][1])*100)      
        probabilities.append(prob)
        
    elements = rand.choices(candidates, weights=probabilities, k=numCandidates)  # We select k number of parents based on probabilities from above
    return elements                                                              # Returns the list of new candidates

# Function handles "Reproduction" with gene crossover and mutation
def speedDating(numParents, candidates):
    numPairs = numParents/2
    numPairs = int(numPairs)
    throwAwayList = candidates
    
    pairs = []
    while len(throwAwayList)>1: 
        rnd = rand.randrange(0,len(throwAwayList))        
        mom = throwAwayList.pop(rnd)
        rnd = rand.randrange(0,len(throwAwayList))
        dad = throwAwayList.pop(rnd)
        
        pairs.append((mom,dad))
    return pairs

#Function takes a list of x,y coordinates and returns a list of those coordinates in binary
def convertToBinary(pairs):                                     #! This is bad code i know!
    parentBinaries = []
    for i in range(len(pairs)):
        binaryPair = []
        
        pair = pairs[i]
        for i in range(len(pair)):
            x = pair[i][0]
            y = pair[i][1]
            binaryStringX = f'{x:06b}'                          # We convert to binary 
            binaryStringY = f'{y:06b}'                          # Since we are working with -10 to 10 values we use 4 binary spaces 

            if x<0 and y<0:                                     
                binaryStringX = binaryStringX.replace('-','1',1)
                binaryStringY = binaryStringY.replace('-','1',1)
            elif x<0 and y>0:
                binaryStringX = binaryStringX.replace('-','1',1)
            elif x>0 and y<0:
                binaryStringY = binaryStringY.replace('-','1',1)
            binaryPair.append((binaryStringX, binaryStringY))       #Adds coordinates in binary Neither is negative  
            
        parentBinaries.append(binaryPair)
    return parentBinaries  
 
def combineGenes(genePair, probability,mutation):
    
    for i in range(len(genePair)-1): 
        parent1X = genePair[i][0]        
        parent1Y = genePair[i][1]      
        
        parent2X = genePair[i+1][0]
        parent2Y = genePair[i+1][1]
        
        for j in range(len(parent1X)):
            print(parent1X[j])
            print(parent2X[j])
            
        
        j = 0
        
        for j in range(len(parent1Y)):
            parent1Y[i]
            parent2Y[i]
    
def crossover(parents, probability, mutation):
    print("Starting crossover:")
    children = []
    
    for j in range(len(parents)):               # For each pair
        pair = parents[j]                       # Pair with 2 coordinates each Pair: [{x,y},{x,y}]
        genePair = []                         
        
        for i in range(len(pair)):              #For each parent in the pair (2)   
        
            genex = (pair[i][0])                # Take the parents gene X                   
            xList = []
            xList[:0] = genex                   # Convert it to list
            
            geney = (pair[i][1])                # Take parents gene Y
            yList = []
            yList[:0] = geney                   # Convert it to list
                        
            genePair.append((xList, yList))     # Add the pair of genes to the list
        combineGenes(genePair,0,0)            
        

        
    
def geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen): #? We start by defining the main parameters we will use for the GA 
    printStartOfAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)
    
    #We start by defining and encoding the chromosomes for our GA, for defining the chromosomes we will be using the fitness function from 1.1
    chromosomes = []
    
    for i in range(populationSize):
        x = rand.randint(-10,10)                            # Defines the range of x values and picks one random value from the range 
        y = rand.randint(-10,10)                            # Defines the range of y values and picks one random value from the range
        chromosomes.append((x,y))                           # Adds coordinate to list

    print("List of values: "+str(chromosomes)+" \n")            
    
    results = []                                            #We define the results in a list
    for i in range(populationSize): 
        xValue = chromosomes[i][0]                          #Defining x value
        yValue = chromosomes[i][1]                          #Defining y value
        value = fitnessFunction(xValue, yValue)             #Computing result of fitness function
        results.append(value)                               
    probabilities = rouletteWheelSelection(populationSize, results) #Computing probability for candidate selection

    chromAndProb = []                                       # Linking the chromosomes with their computed probability
    for i in range(populationSize):                 
        chromAndProb.append((chromosomes[i], probabilities[i]))    
    
    print("Results from fitness function: \n")              
    for i in range(populationSize):
        print("Chromosome: "+str(chromAndProb[i][0])+"   Result:"+str(results[i])+" Calculated probability: "+str(chromAndProb[i][1])+"\n")
    
    #We now have the results for our parents, for parent selection we will select the same number of parents
    #? They will however be selected with the probabilities calculated in rouletteWheelSelection
    candidates = selectParents(populationSize, chromAndProb) # Function selects candidates using probabilities 
    
    print("SELECTED CANDIDATES:")
    print(str(candidates)+"\n")
    print("Parents:")
    pairs = speedDating(populationSize, candidates)          # Function pairs up the candidates as parents :)
    for i in range(len(pairs)):
        print("Pair "+str(i+1)+" Mom:"+str(pairs[i][0])+" Dad:"+str(pairs[i][1])+"\n")
        
    binaries = convertToBinary(pairs)
    crossover(binaries, crossoverProb, mutationProb)           #Function will perform the Reproduction
 
            
populationSize = 4
crossoverProb =0.5
mutationProb =0.2
numberOfGen = 10
geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)

    