import matplotlib as mtp
from matplotlib import pyplot as plt    # We use pyplot to plot the local minima 
import sympy as sym                     # We use sympy to differentiate the function 
import random as rand                   # Random is only used to initialize a random starting point


# Task 1.3 Will implement a simple gradient descent algorithm
# We will be using the fitnessfunction from assignment2_1_1 (Task 1.1)
from assignment2_1_1 import fitnessFunction 

def derivatives(valueX,valueY):
    x, y = sym.symbols('x y')

    f = ((x+2*y-7)**2)+((2*x+y-5)**2)                       # We define our function
    derx = f.diff(x).evalf(subs={x: valueX, y: valueY})     #* We define and evaluate the partial derivative with respect to X
    dery = f.diff(y).evalf(subs={x: valueX, y: valueY})     #* We define and evaluate the partial derivative with respect to Y  
    derx = float(derx)                                      # We convert the values to float 
    dery = float(dery)
    return derx, dery                                       #? We return the values to the main function 
    
def gradientDescent(position, stopCrit, learnRate, maxIt):
    #Convenience prints
    print("______________________________________________________________________________ \n")
    print("STARTING GRADIENT DESCENT! \n")
    print("Starting point: "+str(position))
    print("Function: f = ((x+2*y-7)**2)+((2*x+y-5)**2) \n")
    print("______________________________________________________________________________ \n")
    
    x,y = position                                          # We set the initial position (random)
    
    for i in range(maxIt):                                  
        print("Iteration:"+str(i)+"\n")
            
        value = fitnessFunction(x,y)                        # We compute the initial value for the function
        dx, dy = derivatives(x, y)                          # We compute the gradients with partial derivatives and return the values 
        
        print("Point: "+str(x)+"  "+str(y)+" Computed value:  "+str(value)+"\n")    
        print("Computed value for partial derivative X:  "+str(dx)+"\n")
        print("Computed value for partial derivative Y:  "+str(dy)+"\n")
        print("______________________________________________________________________________ \n")
        
        tempx = x
        tempy = y
        
        x = x-learningRate*dx                               #* We update the x and y coordinates with basic formula
        y = y-learningRate*dy                               # ! Taken from tutorial 3 slides 

        #Stopping criteria 1 if the rate of change in points is too low we stop
        if (abs(tempx-x))<stopCrit or (abs(tempy-y))<stopCrit:      
            print("Rate of change between points is too small! Rate of change: x "+str(tempx-x)+", y "+str(tempy-y)+"\n")
            print("Selected points: x "+str(round(x))+" y "+str(round(y))+"\n Computed value:"+str(value))
            return
        
        #Stopping criteria 2 if the rate of change between the computed value is too low we stop
        newValue = fitnessFunction(x, y)                    #* New function value
        if (abs(newValue-value)<stopCrit):
            print("Rate of change of function value is too small! Rate of change: "+str(abs(newValue-value))+"\n")
            print("Selected points: x "+str(round(x))+" y "+str(round(y))+"\n Computed value:"+str(value))
            return
            
        
    print("Maximum iterations reached! \n Selected points: x "+str(x)+" y "+str(y)+"\n Computed value:"+str(value))
     

x = rand.randint(-10,10)                            # Defines the range of x values and picks one random value from the range 
y = rand.randint(-10,10)                            # Defines the range of y values and picks one random value from the range

startPosition = (x,y)
stoppingCriteria = 0.001
learningRate = 0.1
maximumIterations = 100

gradientDescent(startPosition,stoppingCriteria, learningRate, maximumIterations)