# -*- coding: utf-8 -*-
"""starsblenderCIA3-Ananya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bQK00kKS0jripxstcNPHxDlXgxEwsry4

# **MINI PROJECT**

### Ananya Geetey
###22112308
###2BSCEA
###Introduction to Data Science

###Steps followed-
1. Data
2. Observation
3. Checking Null Values
4. Pre-processing
5. EDA
6. Classification

# DATA

The domain of data visualisation in Blender is explored, research papers like 3D Scientific Visualization
with Blender by brian Kent(which uses astronomical data) and
articles like 3D and Motion in data Visualization by Josh Taylor were reviewed

For this Project, 6 class star dataset was taken for star classification from KAGGLE
https://www.kaggle.com/datasets/deepu1109/star-dataset

# OBSERVATION
"""

#Importing the modules and packages to be used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

data=pd.read_csv("starss.csv")
data

"""the target or dependent variable is "star type" , independent or feature variables are "temperature","luminosity","radius","absolute magnitude","star color" and "spectral class"
---
This CSV file contains a dataset of 240 stars of 6 classes:

Brown Dwarf -> Star Type = 0

Red Dwarf -> Star Type = 1

White Dwarf-> Star Type = 2

Main Sequence -> Star Type = 3

Supergiant -> Star Type = 4

Hypergiant -> Star Type = 5

# NULL VALUES
"""

data.isnull().values.any()

"""There are no null values in the dataset

# PRE-PROCESSING

For pre-processing the data, qualitative columns were removed which cannot be used for analysis
"""

#removing purely qualitative variables
data.drop("Star color",inplace=True,axis='columns')
data.drop("Spectral Class",inplace=True,axis='columns')
print(data.columns)

"""# EDA"""

import seaborn as sns
sns.boxplot(x=data['Star type'])
#there  are no outliers

print("correlation matrix")
data.corr(method="kendall")

data.head()

dataplot=sns.heatmap(data.corr(),cmap="magma",annot=True)#options-magma
#annot is annotation on the blocks
#cmap is the colors u want

"""Luminosity shows the highest correlation with star type"""

# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(data['Luminosity(L/Lo)'], data['Star type'])
plt.title('Scatter plot between Star type and Luminosity')
ax.set_xlabel('Luminosity')
ax.set_ylabel('Star type')
plt.show()

"""Second most correlated is the Radius"""

fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(data['Radius(R/Ro)'], data['Star type'])
plt.title('Scatter plot between Star type and Radius')
ax.set_xlabel('Radius')
ax.set_ylabel('Star type')
plt.show()

#scatter plot for Luminosity and radius
fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(data['Radius(R/Ro)'], data['Luminosity(L/Lo)'])
plt.title('Scatter plot between Luminosity and Radius')
ax.set_xlabel('Radius')
ax.set_ylabel('Luminosity')
plt.show()

fig, ax = plt.subplots(figsize=(5,5))
ax.scatter(data['Temperature (K)'], data['Star type'])
plt.title('Scatter plot between Star type and Radius')
ax.set_xlabel('Temperature')
ax.set_ylabel('Star type')
plt.show()

"""# MODEL

K-means Clustering is the best model for Classification with this dataset

### Multiple Linear Regression
"""

#separating independent and dependent variables
#creating feature variables
x=data.drop("Star type",axis=1)
y=data["Star type"]
print(x)
print(y)

#creating train and test sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=101)
#creating regression model
model=LinearRegression()
#fitting the model
model.fit(x_train,y_train)

x_train

x_test

y_train

y_test

predictions=model.predict(x_test)
predictions

from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error
#model evaluation
print("mean_squared_error: ",MSE(y_test,predictions))
print("mean_absolute_error: ",mean_absolute_error(y_test,predictions))

"""The model is able to predict the star type with good accuracy.

### K-means Clustering

Classification of star type
"""

from sklearn.cluster import KMeans
# Selecingt the columns I want to cluster on
X=data.loc[:,['Star type','Luminosity(L/Lo)']]
# Performing k-means clustering with k=6 clusters
kmeans = KMeans(n_clusters=6)
kmeans.fit(X)

# Adding a new column to the original dataset with the cluster labels
data['cluster'] = kmeans.labels_
print(kmeans.cluster_centers_)

data.head()

# Plotting the clusters
colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray']
for i in range(kmeans.n_clusters):
    cluster_data = data[data['cluster'] == i]
    plt.scatter(cluster_data['Star type'], cluster_data['Luminosity(L/Lo)'],
                color=colors[i], label=f'Cluster {i+1}')

plt.xlabel('Star type')
plt.ylabel('Luminosity(L/Lo)')
plt.legend()
plt.show()
##star type divided on the basis of Luminosity

#dividing star type based on Radius
Y=data.loc[:,['Star type','Radius(R/Ro)']]
# Performing k-means clustering with k=6 clusters
kmeans = KMeans(n_clusters=6)
kmeans.fit(Y)
data['cluster'] = kmeans.labels_
print(kmeans.cluster_centers_)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray']
for i in range(kmeans.n_clusters):
    cluster_data = data[data['cluster'] == i]
    plt.scatter(cluster_data['Star type'], cluster_data['Radius(R/Ro)'],
                color=colors[i], label=f'Cluster {i+1}')

plt.xlabel('Star type')
plt.ylabel('Radius')
plt.legend()
plt.show()

#dividing the star type based on Temperature
Z=data.loc[:,['Star type','Temperature (K)']]
# Performing k-means clustering with k=6 clusters
kmeans = KMeans(n_clusters=6)
kmeans.fit(Z)
data['cluster'] = kmeans.labels_
print(kmeans.cluster_centers_)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray']
for i in range(kmeans.n_clusters):
    cluster_data = data[data['cluster'] == i]
    plt.scatter(cluster_data['Star type'], cluster_data['Temperature (K)'],
                color=colors[i], label=f'Cluster {i+1}')

plt.xlabel('Star type')
plt.ylabel('Temperature')
plt.legend()
plt.show()

#dividing the star type based on Temperature and radius
Z=data.loc[:,['Star type','Temperature (K)','Radius(R/Ro)',]]
# Performing k-means clustering with k=6 clusters
kmeans = KMeans(n_clusters=6)
kmeans.fit(Z)
data['cluster'] = kmeans.labels_
print(kmeans.cluster_centers_)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray']
for i in range(kmeans.n_clusters):
    cluster_data = data[data['cluster'] == i]
    plt.scatter(cluster_data['Star type'], cluster_data['Temperature (K)'],cluster_data['Radius(R/Ro)'],
                color=colors[i], label=f'Cluster {i+1}')

plt.xlabel('Star type')
plt.ylabel('Temperature')
plt.legend()
plt.show()

"""### INTERPRETATION

The Clusters can be classified as follows,

1. The Red Dwarf Star type have Temperature between 0 to 10,000 Kelvins and Radius between 0 to 250 units.
2. The Brown Dwarf Star type have temperature between 20,000 to 35,000 and radius between 1000 to 1500
3. The White Dwarf Star type have temperature between 30,000 to 40,000 and radius between 1500 to 2000
4. The Main Sequence Star type have temperature between 10,000 to 15,000 and radius between 500 to 1000
5. Super Giants have temperature between 0 to 10,000 and radius between 750 to 1250.
6. Hyper Giants have temperature between 15,000 to 25,000 and radius between 1250 and 1750
"""