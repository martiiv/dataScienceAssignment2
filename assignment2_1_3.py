import matplotlib as mtp
from matplotlib import pyplot as plt    # We use pyplot to plot the local minima 
import sympy as sym                     # We use sympy to differentiate the function 
import random as rand                   # Random is only used to initialize a random starting point


# Task 1.3 Will implement a simple gradient descent algorithm
# We will be using the fitnessfunction from assignment2_1_1 (Task 1.1)
from assignment2_1_1 import fitnessFunction 

def derivatives(valueX,valueY):
    x, y = sym.symbols('x y')

    f = ((x+2*y-7)**2)+((2*x+y-5)**2)                        # We define our function
    derx = f.diff(x).evalf(subs={x: valueX, y: valueY})
    dery = f.diff(y).evalf(subs={x: valueX, y: valueY})
    derx = float(derx)
    dery = float(dery)
    return derx, dery
    
def gradientDescent(position, stopCrit, learnRate, maxIt):
    
    print("______________________________________________________________________________ \n")
    print("STARTING GRADIENT DESCENT! \n")
    print("Starting point: "+str(position))
    print("Function: f = ((x+2*y-7)**2)+((2*x+y-5)**2) \n")
    print("______________________________________________________________________________ \n")
    
    x,y = position
    value = fitnessFunction(x,y)    
    dx, dy = derivatives(position[0], position[1])
    
    print("Computed value for Function at x,y:  "+str(value)+"\n")    
    print("Computed value for partial derivative X:  "+str(dx)+"\n")
    print("Computed value for partial derivative Y:  "+str(dy)+"\n")
    print("______________________________________________________________________________ \n")
    
    
    ##for i in range(maxIt):
    #    x = position[0]
    #    y = position[1]
    #    
    #    value = fitnessFunction(x,y)
    #    xValue = derx
    #    yValue = dery
        
    #    if value<=stopCrit: return
        
    #print("Finished Gradient Descent! \n Final value: "+str(value))
     
x = rand.randint(-10,10)                            # Defines the range of x values and picks one random value from the range 
y = rand.randint(-10,10)                            # Defines the range of y values and picks one random value from the range

startPosition = (x,y)
stoppingCriteria = 2
learningRate = 0.1
maximumIterations = 100

gradientDescent(startPosition,stoppingCriteria, learningRate, maximumIterations)