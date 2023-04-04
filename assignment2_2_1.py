import pandas as pd                                 #We use pandas for reading CSV 
import matplotlib.pyplot as plt                     #We use matplotlib to visualize the dataset 
from sklearn.neighbors import KNeighborsClassifier  #For this portion of the assignment i will use scikit learn and their KNN classifier




#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
one = trainData["1"]
two = trainData["2"]
three = trainData["3"]
four = trainData["4"]
five = trainData["5"]
six = trainData["6"]
seven = trainData["7"]
attrClass = trainData["label"]

plt.scatter(one,two, c = attrClass)
plt.show()