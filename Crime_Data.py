import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from sklearn.cluster import	KMeans

Crime = pd.read_csv("C:/Users/SHAJIUDDIN MOHAMMED/Desktop/crime_data.csv")
Crime.columns = 'State','Murder', 'Assault', 'UrbanPop','Rape'

Crime.describe()


# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(Crime.iloc[:, 1:])
df_norm.describe()

###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 8))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
    
TWSS

# Scree plot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 5 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 4)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
Crime['clust'] = mb # creating a  new column and assigning it to new column 

Crime.head()
df_norm.head()

Crime = Crime.iloc[:,[5,0,1,2,3,4]]
Crime.head()

Crime.iloc[:, 2:6].groupby(Crime.clust).mean()

Crime.to_csv("Kmeans_Crime.csv", encoding = "utf-8")

import os
os.getcwd()
