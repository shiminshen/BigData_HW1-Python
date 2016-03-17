from loadFile import loadTaxiData 
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap


def cluster():
    """clustr the data from files
    :returns: TODO

    """
    dataMatrix = loadTaxiData()
    print(dataMatrix[1:2])
    # locationList = dataMatrix.iloc[:,5:7]
    # ds = DBSCAN(eps=0.001).fit(locationList)
    # print(ds.labels_)
    """
    locationList = dataMatrix[:, 5:7]
    db = DBSCAN(eps=0.001).fit(locationList)

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    core_samples = db.core_sample_indices_

    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    # Plot result
    """

"""
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'

        class_member_mask = (labels == k)

        xy = locationList[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=14)

        xy = locationList[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=6)

        plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()

"""

cluster()
