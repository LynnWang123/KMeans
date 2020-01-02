# KMeans

1. K_Means_Manual.py

There are 3 steps:
	
	a. Initialisation – K initial “means” (centroids) are generated at random
		
	b. Assignment – K clusters are created by associating each observation with the nearest centroid
		
	c. Update – The centroid of the clusters becomes the new mean
  
  
Assignment and Update are repeated iteratively until convergence.

The end result is that the sum of squared errors is minimised between points and their respective centroids.
