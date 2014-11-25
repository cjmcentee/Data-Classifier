__author__ = 'coltonmcentee'

from numpy import array
from scipy.cluster.vq import kmeans
from math import sqrt, pow, exp, pi
from Utility import distance, average_point
import json

def gaussian(mean, std, x):
    return exp( -pow(x - mean, 2)/(2.0*pow(std, 2))) / (std * sqrt(2.0*pi))


class GaussianMixtureModel():

    def __init__(self, points, number_centroids):
        # Get KMeans centroids
        centroid_points, distortion = kmeans(array(points), number_centroids)
        centroid_points = [tuple(p) for p in centroid_points] # convert ndarray -> list of tuples

        # Set up clusters
        clustered_data = {}
        for centroid_point in centroid_points:
            clustered_data[centroid_point] = []

        # Assign each point to a cluster
        for point in points:
            cluster_distances = [distance(point, cp) for cp in centroid_points]
            min_val, min_index = min((val, i) for i, val in enumerate(cluster_distances))
            clustered_data[centroid_points[min_index]].append(point)

        # Save the clusters to the model
        self.clusters = [Cluster(centroid, cluster_points) for centroid, cluster_points in clustered_data.iteritems()]
        self.raw_points = points

    def str(self):
        x_range = range(int(min(self.raw_points)), int(max(self.raw_points)))
        for cluster in self.clusters:
            print "Centroid: " + str(cluster.centroid) \
                + "\nMean: " + str(cluster.mean) \
                + "\nStandard Deviation: " + str(cluster.std) \
                + "\n"

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_tab(self):
        tab_file = ""
        for point in self.raw_points:
            # One column per point coordinate value
            for coordinate in point:
                tab_file += str(coordinate) + "\t"

            # One column for the nearest cluster, named 'C#'
            nearest_cluster_index = self.clusters.index(self.nearest_cluster(point))
            tab_file += "C" + str(nearest_cluster_index) + "\t"

            # One column for the distance from each cluster
            for distance in self.cluster_quality_list(point):
                tab_file += str(distance) + "\t"

            # Remove the last tab from the line
            tab_file = tab_file[:-1]

            # Add a line ending
            tab_file += "\n"

        return tab_file


    def nearest_cluster(self, point):
        cluster_distances = [distance(point, centroid.centroid) for centroid in self.clusters]
        min_val, min_index = min((val, i) for i, val in enumerate(cluster_distances))
        return self.clusters[min_index]


    def cluster_quality_list(self, point):
        cluster_distances = [distance(point, centroid.centroid) for centroid in self.clusters]
        return cluster_distances


class Cluster():

    def __init__(self, centroid, points):
        self.centroid = centroid
        self.points = points
        self.mean = self.mean()
        self.std  = self.std()

    def mean(self):
        mean = average_point(self.points)
        return mean

    def std(self):
        sqrdiff_from_mean = [pow(distance(self.mean, point), 2) for point in self.points]
        sum = reduce(lambda x, acc: x + acc, sqrdiff_from_mean, 0)
        average_from_mean = sum / len(sqrdiff_from_mean)
        std = sqrt(average_from_mean)
        return std