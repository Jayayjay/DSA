from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

class KMeansCLuster:
    """ 
    centiod-based unsuoervised ml algorithm used to partition data into k distinct clusters (I shall then call it n-means clusters: where n specifies the number of clusters predefined by the user) based on similar features. its simple and scalable
    
    Mode of Operation
        1. Choose number of clusters
        2. initialize k centriods randomly
        3. Assign each data point to the closest centriod
        4. Recompute centroids as the mean of all points in each cluster
        5. Repeat until centroids stop moving ie no significant change
    
    When to use:
        1. Fast, scalable algorithm
        2. Hard partitioning
        3. Number of clusters are known or guessable
    Limitations:
        1. Requires predefined K
        2. May converge to a point on a graph where the functional value is lower than all nearby points 
        3. struggles with overlapping clusters
        3. Terrible with outliers
    """
    X, _ = make_blobs(n_samples=3000, centers=4, random_state= 42)
    kmeans = KMeans(n_clusters = 7, random_state = 43)
    kmeans.fit(X)
    
    plt.scatter(X[:, 0], X[:, 1], s=kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', marker='X')
    
    plt.title('KMeans Clustering')
    plt.show()
    
KMeansCLuster()