# geometry-puzzle

The goal is to write a class that can support three types of query efficiently:
1. Given a radius, query to find the number of coordinates from the coordinate set that are
within a radius distance from at least one of the centroid
2. Given a percent value (p), query to find the minimum radius such that p percent of the
coordinates of the the coordinate set are within that radius from at least one centroid.
3. Given number (n), query for maximum radius, r such that number of coordinates within r is
at most n for every centroids.
I take advantage of k-d tree data structure to help for nearest neighbor search. I also use pandas
to parse the csv files. This can be done with other parser but I chose pandas because of ease of
data exploration. I first did some scatter plot and basic statistics to check for outliers.

## Prerequisites

sklearn, numpy, pandas
install anaconda
conda install sklean, numpy, pandas


## Algorithm and runtime

1.2 CoorCentroidQuery class
It contains two main attributes: 
1. distance_array is used to store the first nearest neighbor distance
of each coordinate to a centroid. This is done by construct a tempolary k-d tree of centroids then
query for the first nearest neighbor of each coordinate. This array is then sorted
2. __coor_tree which is the k-d tree of the centroid
3. centroid_set
The memory used by this class is O(n_coord+n_centroid)

## Running the tests

python proximity_test.py to run test.


## Authors

* **Wathid Assawasunthonnet** 

## Acknowledgments

* StackExchange for inspiration
* sklearn for implementing kdtree
