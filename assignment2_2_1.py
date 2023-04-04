import pandas as pd             #We use pandas for reading CSV 
import matplotlib.pyplot as plt #We use matplotlib to visualize the dataset 

from sklearn.neighbors import KNeighborsClassifier

#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
attrClass = trainData["label"]

