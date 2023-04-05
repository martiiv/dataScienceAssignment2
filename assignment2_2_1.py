import pandas as pd                                 #We use pandas for reading CSV 
import matplotlib.pyplot as plt                     #We use matplotlib to visualize the dataset 
from sklearn.neighbors import KNeighborsClassifier  #For this portion of the assignment i will use scikit learn and their KNN classifier
from 
#! Code inspired by the following resources:
#! https://realpython.com/knn-python/ For using the sklearn library and plotting 
#! https://towardsdatascience.com/multiclass-classification-using-k-nearest-neighbours-ca5281a9ef76 For inspiration regarding multi variable classification
#! https://ntnu.blackboard.com/ultra/courses/_35408_1/cl/outline Lecture 5 for k nearest neighboor 
#!                 
#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
trainData.plot.scatter(x="1", y="2",c = "label", colormap='viridis')
plt.show() 

label = trainData["label"]                          #We define the label column
test = pd.read_csv("test.csv", encoding="UTF-8")    #Reading test data
print(trainData.head())

classifier = KNeighborsClassifier(n_neighbors=1, metric="euclidean")    #We initialize our classifier
classifier.fit(trainData, label)                                        # We fit the classifier to the trainindata 
predictor = classifier.predict(test)                                    # We predict the values of the test data set 
print(predictor)

