# K-Means-Python
A K-means clustering algorithm coded in the Python language.


# Algorithm description
The K-Means clustering algorithm is an unsupervised algorithm that is popular way to characterize data in statistical analysis. In order to run, it needs data points and initial clusters. It then gives the user clusters of data points that are close to or similar to each other. The best way to use this algorithm is to first look at the data, and choose centroids that are placed close to what are intuitively observed to be clusters. 

This is an iterative algorithm. for each iteration, points are assigned to the closest centroid. After all points are assigned, the centroids are recalculated by taking the average position of all points assigned to it. The current iteration is then finished, and assignments are reset. This process continues until centroids remain the same for 2 iterations. 
 
# Program description 
The program is split into 2 parts, the data template and the code itself. The data template contains the format that the code needs in order to read the data. The data that is input into the template includes centroids, data points, the number of data points and the number of centroids. An example is also provided. The program itself is written in Python, and uses the data in the template to output clusters in the form of text and a colored plot. The program requires the "pandas", "numpy" and "matplotlib.pyplot" librarys. 

