import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt

#skipping the distance calculation part and directly using the Distance Matrix
#sample mat = np.array([[0,4,25,24,9,7], [4,0,21,20,5,3], [25,21,0,1,16,18], [24,20,1,0,15,17], [9,5,16,15,0,2], [7,3,18,17,2,0] ])
mat = np.array([[0,1,4,5], [1,0,2,6], [4,2,0,3], [5,6,3,0]])
dists = squareform(mat)

#This step is where we mention its "Single Link" Cluster
linkage_matrix = linkage(dists, "single")
#sample dendrogram(linkage_matrix, labels=["A","B","C","D","E","F"])
dendrogram(linkage_matrix, labels=["A","B","C","D"])
plt.title("Single Link")
plt.show()
