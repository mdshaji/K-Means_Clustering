import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from sklearn.cluster import	KMeans

Insurance = pd.read_csv("C:/Data Science/Assignments/Module-K-Means/Insurance Dataset.csv")
Insurance.describe()

############Normalizing the data#################
def norm_func(i):
    x=(i-i.min()/i.std())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm=norm_func(Insurance.iloc[:,0:])
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

# Selecting 3 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 3)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
Insurance['clust'] = mb # creating a  new column and assigning it to new column 

Insurance.head()
df_norm.head()

Insurance = Insurance.iloc[:,[5,0,1,2,3,4]]
Insurance.head()

Insurance.iloc[:, 1:6].groupby(Insurance.clust).mean()

Insurance.to_csv("Kmeans_Insurance.csv", encoding = "utf-8")

import os
os.getcwd()
