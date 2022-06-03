# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1InVjPExi5eIqvlMCHIK3AOyMCefeMXDJ

**Importing Libraries**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

"""**Loading the Dataset**"""

from google.colab import files
uploaded = files.upload()

"""**Dataset Analysis**"""

iris =pd.read_csv('Iris.csv')
print(iris.shape) #To know the rows and columns of dataset

print(iris.describe()) #Description of the data

print(iris.head(5)) #First five elements of the dataset

# checking for missing values
iris.isnull().sum()

"""**Choosing the number of clusters**

WCSS(within clusters sum of squares) method
"""

x = iris.iloc[:, [0, 1, 2, 3]].values
print(x)

from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', 
                    max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
# Plotting the results onto a line graph, 
# `allowing us to observe 'The elbow'
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') # Within cluster sum of squares
plt.show()

"""From the above graph, the optimum clusters is where the elbow occurs. This is when the within cluster sum of squares (WCSS) doesn't decrease significantly with every iteration.

From this we choose the number of clusters=3

**Apply K-Means to the Dataset**
"""

kmeans = KMeans(n_clusters = 3, init = 'k-means++',
                max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

"""**Visualize the clusters**"""

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], 
            s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], 
            s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1],
            s = 100, c = 'green', label = 'Iris-virginica')

# Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], 
            s = 100, c = 'yellow', label = 'Centroids')

plt.legend()