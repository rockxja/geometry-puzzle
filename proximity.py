from __future__ import division
import numpy as np
import pandas as pd
import bisect
from sklearn.neighbors import KDTree

'''
A class that process the coordinates and centroid data that supports three types
of queries:
1. Given a radius, query to find the number of coordinates from the coordinate set that are 
   within a radius distance from at least one of the centroid
2. Given a percent value (p), query to find the minimum radius such that p percent of the coordinates
   of the the coordinate set are within that radius from at least one centroid.
3. Given number (n), query for maximum radius, r such that number of coordinates within r is at most n
   for every centroids.
Parameters: coor_set, type: Pandas dataframe or numpy array, size = [n_coords, 2].
            centroid_set, type: type: Pandas dataframe or numpy array, size = [n_centroids, 2]
Attributes: numb_coords
            numb_centroids
            centr_set
Methods: get_num_coors
		 get_min_radius
		 get_max_radius
'''

class CoorCentroidQuery:

    def __init__(self, coor_set, centr_set):
    	self.num_coords = coor_set.shape[0]
    	self.num_centroids = centr_set.shape[0]
    	self.centr_set = centr_set
    	self.__coor_tree = KDTree(coor_set)
    	self.__gendistancearr(centr_set, coor_set)

    def __gendistancearr(self, centr_set, coor_set):
    	kdt = KDTree(centr_set)
    	distance, indx = kdt.query(coor_set)
        self.distance_array = sorted(distance.reshape(distance.shape[0], ))
    '''
    This method queries number of coordinates that are within radius distance 
    from at least one centroid.
    
    Parameters: radius in meters, float.
    Return: number of coordinates, int.
    '''
    def get_num_coors(self, radius):
        if radius<0:
            raise ValueError("distance has to be positive")
        i = bisect.bisect_left(self.distance_array, radius)
        if i>len(self.distance_array)-1:
    	    return len(self.distance_array)
        # if it exists in the array return the index+1
    	elif self.distance_array[i]==radius:
    	    return i+1
    	else:
 		    return i
    
    '''
    This method queries for minimum radius such that p percent of coor_set
    are within at least one centroid.

    Parameters: percentage point, float
    Return:  radius, float
    '''
    def get_min_radius(self, percent):
        if percent==0:
            return 0.0
    	if (percent>=0) and (percent<=100):
    		length = len(self.distance_array)
    		# percent = (position+1)/length hence 
    		pos = int(np.ceil((percent/100)*length))
    	else:
    		raise ValueError("percent not in 0 to 100")
    	return self.distance_array[pos-1]
    
    '''
    Parameters: number of coordinates, int
    Return: radius, float
    '''
    def get_max_radius(self, numb_within):
    	n = 0
    	if numb_within>self.num_coords:
    		raise ValueError("number of contained coordinates cannot be larger than total number of coordinates")
    	if numb_within<self.num_coords:
            n = numb_within+1
    		# get the (numb_within+1)ith biggest distance
            distances, idx = self.__coor_tree.query(self.centr_set, k=n)
    	    # get the (numb_coord+1)ith biggest distance
            max_radii = [dist[n-1] for dist in distances]
    	    # return the minimum of the list substract by a small epsilon to guarantee that
    	    # all the centroid has at most numb_coord coordinates
    	    epsilon = 0.0000001
    	    return min(max_radii)-epsilon
        if numb_within==self.num_coords:
            return float('inf')
