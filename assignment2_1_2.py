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

# Function swaps genes based on probability  
def combineGenes(genePair, probability):
    for i in range(len(genePair)-1):                # For each pair (number of parents/population)
        children = []                               # ! Update with global parameters this is spaghetti

        parent1X = genePair[i][0]                   # We define the different genes in each pair of parents
        parent1Y = genePair[i][1]                   
        parent2X = genePair[i+1][0]
        parent2Y = genePair[i+1][1]
        
        for j in range(len(parent1X)):              #! For the length of our binary update with global variable 
            crossX = rand.random() < probability    # A bool value which decides if we crossover using probability
        
            if crossX is True:                      # If it returns true we cross over!
                gene1 = parent1X[j]                 # Defines one part of gene (one binary position)
                gene2 = parent2X[j]                 # We define both of the X genes value
                
                parent1X[j] = gene2                 # And swap accordingly
                parent2X[j] = gene1                 # ! This is horrible code but i am bad at python!
                
                gene1 = parent1Y[j]                 # Repeat for Y gene
                gene2 = parent2Y[j]
                    
                parent1Y[j] = gene2 
                parent2Y[j] = gene1
            
        #New Child!
        child1X = ''.join(parent1X)                 # We join the binary lists to one string and define child
        child1Y = ''.join(parent1Y)                 # ?We still keep the (x,y) format 
         
        #New Child!
        child2X = ''.join(parent2X)                 # Repeat for child 2
        child2Y = ''.join(parent2Y)                 
        
        children.append((child1X, child1Y))         # We add new child to list
        children.append((child2X,child2Y))          # Repeat for child 2 
    #! This works in pairs of parents so it should work for higher populations than 4
    
    return children                                 # We return the list of new children

def mutateChildren(children, mutationProbability):
    newCandidates = []                              # We define list of new candidates
    
    for i in children:                              # For each child
        child = i                                   # We define the child 
        completedChild = []                         # And a list with the two genes
        
        for j in child:                             # For Each gene 
            #print("GENE:"+str(j))                  # ! Uncomment for clarity regarding mutation
            geneList = []                           # We will split the gene into a list  
            geneList[:0] = j                        # To easily swap values 
            # !Note this might be really inefficent IDK!
            
            for i in range(len(geneList)):
                mutate = rand.random() < mutationProbability    # A bool value which decides if we crossover using probability
                if mutate is True:                              # If the mutate value is true 
                    #print("MUTATION!")                         # ! Uncomment for clarity regarding mutation
                    if geneList[i] == "0":                      # We change the value!
                        geneList[i] = "1"                   
                    else:
                        geneList[i] = "0"
                #else: print("No Mutation!")                    # ! Uncomment for clarity regarding mutation
                
            newGene = ''.join(geneList)                         # We join the gene list to one string again
            completedChild.append(newGene)                      # And add it to the new and mutated child
        newCandidates.append((completedChild[0], completedChild[1])) #Lastly we add the new children to the list of new candidates!
        
    return newCandidates    

def crossover(parents, probability):
    childCandidates = []
    
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
        children = combineGenes(genePair,probability)  # Function will swap genes based on set probability
        
        childCandidates.append(children[i-1])     #Adds the pairs of children
        childCandidates.append(children[i])         
    return childCandidates
                
    
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
        
    print("_____________________________________________________________________________________ \n")
    
    #We now have the results for our parents, for parent selection we will select the same number of parents
    #? They will however be selected with the probabilities calculated in rouletteWheelSelection
    candidates = selectParents(populationSize, chromAndProb) # Function selects candidates using probabilities 
    
    print("SELECTED CANDIDATES:")
    print(str(candidates)+"\n")
    print("_____________________________________________________________________________________ \n")
    print("Parents: \n")
    
    pairs = speedDating(populationSize, candidates)          # Function pairs up the candidates as parents :)
    binaries = convertToBinary(pairs)                        # Converts pairs to binary
    
    for i in range(len(pairs)):
        print("Pair "+str(i+1)+":\n")
        print("Mom:"+str(pairs[i][0])+" Binary: "+str(binaries[i][0])+"\n")
        print("Dad:"+str(pairs[i][1])+" Binary: "+str(binaries[i][1])+"\n")
    print("_____________________________________________________________________________________ \n")
    
    crossedChildren = crossover(binaries, crossoverProb)           #Function will perform the Reproduction
    
    print("Crossover done!\n")
    print("Produced Children: \n")
    for i in range(populationSize):
        print("Child: "+str(i+1)+", Gene: "+str(crossedChildren[i])+"\n")
    print("_____________________________________________________________________________________ \n")
    
    newCandidates = mutateChildren(crossedChildren, mutationProb)
    
    print("Mutation done!\n")
    print("Mutated Children: \n")
    for i in range(populationSize):
        print("Child: "+str(i+1)+", Gene: "+str(newCandidates[i])+"\n")
    print("_____________________________________________________________________________________ \n")
    
    
            
populationSize = 4
crossoverProb =0.5
mutationProb =0.2
numberOfGen = 10
geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)

for i in range(numberOfGen):
    geneticAlgorithm()
