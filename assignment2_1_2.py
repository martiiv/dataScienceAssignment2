import matplotlib
import matplotlib.pyplot as plt #Import for plotting
import numpy as np 

from assignment2_1_1 import fitnessFunction #Importing the fitness function from 1.1
#! NB Algorithm steps and info taken from Excercise 3 in IMT4133: https://ntnu.blackboard.com/ultra/courses/_35408_1/cl/outline Last visit 17.03.2023

# Task 1.2, we will implement a simple GA (Genetic algorithm), this GA will minimize the fitness function defined from assignment2_1.1.py
def geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen): #? We start by defining the main parameters we will use for the GA 
    print("Starting our generation:"+"\n")
    print("________________________"+"\n")
    print("Population size: "+str(populationSize)+" Probability of crossover between genes: "+str(crossoverProb)+" \n")
    print("Probability of mutation within new gene: "+str(mutationProb)+" Number of generation for algorithm: "+str(numberOfGen)+ "\n")
    print("________________________"+"\n")
    
populationSize = 4
crossoverProb =0.5
mutationProb =0.2
numberOfGen = 10
geneticAlgorithm(populationSize, crossoverProb, mutationProb, numberOfGen)

    