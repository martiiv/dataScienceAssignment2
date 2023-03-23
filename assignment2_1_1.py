import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

#Task 1.1
#Function for defining mathematical function 
def fitnessFunction(x,y):
    return ((x+2*y-7)**2)+((2*x+y-5)**2)            #Defines the mathematical function we are working with (Optimizing)

plt.rcParams["figure.figsize"] = [10, 5]            #Defines the figure    
plt.rcParams["figure.autolayout"] = True

x = np.linspace(-10,10,200)                         #Defines the range of x values
y = np.linspace(-10,10,200)                         #Defines the range of y values

plt.plot(x, fitnessFunction(x,y), color='green')    #Plot the function 
#plt.show()

