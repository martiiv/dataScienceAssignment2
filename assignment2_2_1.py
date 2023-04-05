import pandas as pd                                 #We use pandas for reading CSV 
import matplotlib.pyplot as plt                     #We use matplotlib to visualize the dataset 
from sklearn.neighbors import KNeighborsClassifier  #For this portion of the assignment i will use scikit learn and their KNN classifier
from sklearn import preprocessing as pre            #For normalizing 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score #Used for classification matrix 

#! Code inspired by the following resources:
#! https://realpython.com/knn-python/ For using the sklearn library and plotting 
#! https://towardsdatascience.com/multiclass-classification-using-k-nearest-neighbours-ca5281a9ef76 For inspiration regarding multi variable classification
#! https://ntnu.blackboard.com/ultra/courses/_35408_1/cl/outline Lecture 5 for k nearest neighboor 
#!                 
#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
test = pd.read_csv("test.csv", encoding="UTF-8")    #Reading test data
print(trainData.head())

trainData.plot.scatter(x="1", y="2",c = "label", colormap='viridis')    # Plot for visualization

label = trainData["label"]                                              #We define the label column
neighbors = 7                                                       #Defining variables
distanceMethod = "euclidean"

print("Starting classifier, K = "+str(neighbors)+" Distance method used: "+distanceMethod+"\n")

classifier = KNeighborsClassifier(n_neighbors=neighbors, metric=distanceMethod)    #We initialize our classifier
classifier.fit(trainData, label)                                        # We fit the classifier to the trainindata 
predictor = classifier.predict(test)                                    # We predict the values of the test data set 
score =classifier.score(test, test["label"])                            # Finds mean accuracy of our classifier 
print("Classifier score: "+str(score)+"\n")

# Due to the fact that some values are alot larger than others we will normalize them
print("Classifying again with normalized data: \n")
rawData = trainData.drop(["label"], axis=1)                             # We remove the label column
normalizer = pre.MinMaxScaler()                                         # Initialize normalizer 
normalData = normalizer.fit_transform(rawData)                          # Normalize data 
newFrame = pd.DataFrame(normalData, columns= ["1","2","3","4","5","6","7"]) #Create new dataframe
print(newFrame.head())  

normalClassifier =  KNeighborsClassifier(n_neighbors=neighbors, metric=distanceMethod) #Initializing new classifier
normalClassifier.fit(newFrame, label)                                   # Fitting
normalPredictor = classifier.predict(test)                              # Classifying
score = classifier.score(test, test["label"])
print("Classifier score: "+str(score)+"\n")

