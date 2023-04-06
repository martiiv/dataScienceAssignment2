import pandas as pd                                 #We use pandas for reading CSV 
import matplotlib.pyplot as plt                     #We use matplotlib to visualize the dataset 
from sklearn.neighbors import KNeighborsClassifier  #For this portion of the assignment i will use scikit learn and their KNN classifier
from sklearn import preprocessing as pre            #For normalizing 
from sklearn import metrics                         #Used for classification matrix 

#! Code inspired by the following resources:
#! https://realpython.com/knn-python/ For using the sklearn library and plotting 
#! https://towardsdatascience.com/multiclass-classification-using-k-nearest-neighbours-ca5281a9ef76 For inspiration regarding multi variable classification
#! https://ntnu.blackboard.com/ultra/courses/_35408_1/cl/outline Lecture 5 for k nearest neighboor 
#! 
                
#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
test = pd.read_csv("test.csv", encoding="UTF-8")    #Reading test data

trainData.plot.scatter(x="1", y="2",c = "label", colormap='viridis')    # Plot for visualization

label = trainData["label"]                                              #We define the label column
testLabel = test["label"]

neighbors = 15                                                        #Defining variables
distanceMethod = "chebyshev"

print("Starting classifier, K = "+str(neighbors)+" Distance method used: "+distanceMethod+"\n")

classifier = KNeighborsClassifier(n_neighbors=neighbors, metric=distanceMethod)    #We initialize our classifier
classifier.fit(trainData, label)                                        # We fit the classifier to the trainindata 
predictor = classifier.predict(test)                                    # We predict the values of the test data set 
score =classifier.score(test, test["label"])                            # Finds mean accuracy of our classifier 
print("Classifier score: "+str(score)+"\n")

#Printing basic confusion matrix
confusion_matrix = metrics.confusion_matrix(testLabel, predictor)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()
