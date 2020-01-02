import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import copy

df = pd.DataFrame({
		'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
		'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
	})

np.random.seed(2)

k = 3

centroids = {
	i+1 : [np.random.randint(0, 80), np.random.randint(0, 80)]
	for i in range(k)

}


colmap = {1:'r', 2:'g', 3:'b'}

# fig = plt.figure(figsize=(5,5))
# plt.scatter(df['x'], df['y'], color='k')  # totalpoint fig and same color

# for i in centroids.keys():
# 	plt.scatter(*centroids[i], color=colmap[i]) # centroids points color to red/green/blue

# plt.xlim(0, 80)
# plt.ylim(0, 80)

# plt.show()



def assignment(df, centroids):
	for i in centroids.keys():
		df['distance_from_{}'.format(i)] = (
			np.sqrt(
				(df['x']-centroids[i][0]) ** 2 +
				(df['y']-centroids[i][1]) ** 2
			)

		)

	centroids_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]

	df['closest'] = df.loc[:, centroids_distance_cols].idxmin(axis=1)  #返回每行最小只的列名
	df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))  #去掉列名的前缀， 只保留ID
	df['color'] = df['closest'].map(lambda x: colmap[x])  # 颜色

	return df

df = assignment(df, centroids)

# print(df.head())



# fig = plt.figure(figsize=(5,5))
# plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')  # 通过颜色df['color']划分Cluster
# for i in centroids.keys():
# 	plt.scatter(*centroids[i], color=colmap[i])  # 标识Centroid Point
# plt.xlim(0, 80)
# plt.ylim(0, 80)

# plt.show()


old_centroids = copy.deepcopy(centroids)

def update(k):  #根据第一次算出的Cluster ,重新计算Cluster 的mean(x, y) 作为新的Centriods
	for i in centroids.keys():
		centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
		centroids[i][1] = np.mean(df[df['closest'] == i]['y'])

	return k


centroids = update(centroids)

# fig = plt.figure(figsize=(5,5))
# ax = plt.axes()
# plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.3, edgecolor='k')
# for i in centroids.keys():
# 	plt.scatter(*centroids[i], color=colmap[i])
# 	plt.scatter(*old_centroids[i], color='k', edgecolor=colmap[i])
# plt.xlim(0, 80)
# plt.ylim(0, 80)

# for i in old_centroids.keys():
# 	old_x = old_centroids[i][0]
# 	old_y = old_centroids[i][1]

# 	dx = (centroids[i][0]-old_centroids[i][0]) * 0.75
# 	dy = (centroids[i][1]-old_centroids[i][1]) * 0.75

# 	ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])

# plt.show()


# repeat Assignment Stage
df = assignment(df, centroids)

# fig = plt.figure(figsize=(5,5))
# plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')  # 通过颜色df['color']划分Cluster
# for i in centroids.keys():
# 	plt.scatter(*centroids[i], color=colmap[i])  # 标识Centroid Point
# plt.xlim(0, 80)
# plt.ylim(0, 80)

# plt.show()


# Continue until all assigned categories don't change any color
while True:
	closest_centroids = df['closest'].copy(deep=True)
	centroids = update(centroids)
	df = assignment(df, centroids)
	if closest_centroids.equals(df['closest']):
		break


fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')

for i in centroids.keys():
	plt.scatter(*centroids[i], color=colmap[i])

plt.xlim(0, 80)
plt.ylim(0, 80)

plt.show()
	

	
	




	











