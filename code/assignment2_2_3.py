import pandas as pd                                 #We use pandas for reading CSV 
import matplotlib.pyplot as plt                     #We use matplotlib to visualize the dataset 
from sklearn.neighbors import KNeighborsClassifier  #For this portion of the assignment i will use scikit learn and their KNN classifier
from sklearn import preprocessing as pre            #For normalizing 
from sklearn import metrics                         #Used for classification matrix 
    
#We read the csv files like in assignment 1:
trainData = pd.read_csv("train.csv",encoding="UTF-8")    #Read from csv 
test = pd.read_csv("test.csv", encoding="UTF-8")    #Reading test data

label = trainData["label"]                                              #We define the label column
testLabel = test["label"]

neighbors = 31                                                        #Defining variables
distanceMethod = "manhattan"

print("Starting classifier, K = "+str(neighbors)+" Distance method used: "+distanceMethod+"\n")

# Task 2.3 Due to the fact that some values are alot larger than others we will normalize them
normalizer = pre.MinMaxScaler()                                         # Initialize normalizer 

#Normalizing train data
onlyData = trainData.drop(["label"], axis=1)                            # Remove label column
normalizedData = normalizer.fit_transform(onlyData)                     # Fit normalizer and scale data

#Normalizing test data
onlyTest = test.drop(["label"], axis=1)                                 # Remove label column
normalizedTest = normalizer.transform(onlyTest)                         # Scale data

normalizedClassifier = KNeighborsClassifier(n_neighbors=neighbors, metric=distanceMethod)

normalizedClassifier.fit(normalizedData, label)                         # Fit model
normalPredictor = normalizedClassifier.predict(normalizedTest)          # Apply model
normalizedScore = normalizedClassifier.score(normalizedTest, testLabel)
print("Normalized classification accuracy: "+str(normalizedScore))

#Printing confusion matrix
confusion_matrix = metrics.confusion_matrix(testLabel, normalPredictor)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()



