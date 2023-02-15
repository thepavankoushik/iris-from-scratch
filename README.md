# Iris Dataset Clustering (without frameworks)

### Quantization Error:

Quantization is any time we simplify a data set by moving each of the many data points to a convenient (nearest, by some metric) quantum point. These quantum points are a much smaller set. For instance, given a set of floats, rounding each one to the nearest integer is a type of quantization.
Clustering is a well-known, often-used type of quantization, one in which we use the data points themselves to determine the quantum points.
Quantization error is a metric of the error introduced by moving each point from its original position to its associated quantum point. In clustering, we often measure this error as the root-mean-square error of each point (moved to the centroid of its cluster).

Code name: qerror.py
Running from command line: Python3 qerror.py iris-data.csv iris-labels.csv
Output: The quantization error of the data is printed. 

### Lloyd’s k-means:

From a theoretical standpoint, k-means is not a good clustering algorithm in terms of efficiency or quality: the running time can be exponential in the worst case and even though the final solution is locally optimal, it can be very far away from the global optimum (even under repeated random initializations). Nevertheless, in practice the speed and simplicity of k-means cannot be beat. Therefore, recent work has focused on improving the initialization procedure: deciding on a better way to initialize the clustering dramatically changes the performance of the Lloyd’s iteration, both in terms of quality and convergence properties.

Code name: llyod.py
Running from command line: Python3 yourprogram.py inputdata k r outputclusters
Output: The labels are stored in the output file and quantization error of the data is printed.

### k-means++:

Dubbed k-means++, the algorithm selects only the first center uniformly at random from the data. Each subsequent center is selected with a probability proportional to its contribution to the overall error given the previous selections. Intuitively, the initialization algorithm exploits the fact that a good clustering is relatively spread out, thus when selecting a new cluster center, preference should be given to those further away from the previously selected centers.

Code name: kmeanspp.py
Running from command line: Python3 yourprogram.py inputdata k r outputclusters
Output: The labels are stored in the output file and quantization error of the data is printed.

### Results

|#| Fuzzy Lloyd | KMeans++   |
| :---:   | :---: | :---: |
|Qerror | 45.831 | 78.9408   |
| Error | 0.4133 | 0.56   |



|#| Fuzzy KMeans++ | KMeans++   |
| :---:   | :---: | :---: |
|Qerror | 29.9923 | 78.9408   |
| Error | 2.9466 | 0.56   |


