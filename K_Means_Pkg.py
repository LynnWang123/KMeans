from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.DataFrame({
		'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
		'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
	})


kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
print(kmeans)

colmap = {1:'r', 2:'g', 3:'b'}

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5,5))
colors = map(lambda x: colmap[x+1], labels)


plt.scatter(df['x'], df['y'], color=list(colors), alpha=0.5, edgecolor='k')

for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])


plt.xlim(0, 80)
plt.ylim(0, 80)

plt.show()

