import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, n_features=2, centers=3, random_state=23)
#print(X)
print(X.shape) #(500, 2)
#print(y) #0,1,2 -> centers=3
print((X.shape[1],)) #(2,) dvije kolone -> n_features=2
print(np.random.random((X.shape[1],))) #vraca izmedju 0 i 1
print(2 * np.random.random((X.shape[1],))) #vraca izmedju 0 i 2
print(2 * (2 * np.random.random((X.shape[1],)) - 1)) # vraca uzmedju -2 do 2; (2 * np.random.random((X.shape[1],)) - 1) -> -1 i 1
#fig = plt.figure(0)
plt.grid(True) #crtanje mreze
plt.scatter(X[:, 0], X[:, 1], c='blue') #crtanje tacaka
#plt.show() #da se vidi
print("-------------------------")
k = 3

clusters = {}
np.random.seed(23)

for idx in range(k):
    center = 2 * (2 * np.random.random((X.shape[1],)) - 1)
    points = []
    cluster = {
        'center': center,
        'points': []
    }
    clusters[idx] = cluster

print(clusters)
#lijepsi prikaz
for key, v in clusters.items():
    print(key, list(v['center']))

plt.scatter(X[:, 0], X[:, 1])
plt.grid(True)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0], center[1], marker='*', c='red')
plt.show()

def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def assign_clusters(X, clusters):
    for idx in range(X.shape[0]): #prolazi kroz sve tacke
        dist = []

        curr_x = X[idx]

        for i in range(k): #prolazi kroz cluster (0,1,2)
            dis = distance(curr_x, clusters[i]['center']) # 'center' zato sto treba pristup rijecniku!
            dist.append(dis) #rastojanje svake tacke od sva 3 clustera
        curr_cluster = np.argmin(dist) #izvlaci argument sa minimalnim rastojanjem; tj index od minimalne vrijednosti
        clusters[curr_cluster]['points'].append(curr_x) # dodajemo tacku koja je na tom indeksu
    return clusters

#utice na pomjeranje clustera
def update_clusters(X, clusters):
    for i in range(k):
        points = np.array(clusters[i]['points']) #izvlaci sve dodjeljene tacke
        if points.shape[0] > 0: #dok god ima tacaka
            new_center = points.mean(axis=0) #trazi srednju vrijednost tacaka i dodjeljuje new_center
            clusters[i]['center'] = new_center 
            clusters[i]['points'] = []
    return clusters

# predikcija klastera za tačke iz skupa X
def pred_cluster(X, clusters):
    pred = [] # indeksi klastera sa najmanjim rastojanjem od date tačke
    for i in range(X.shape[0]): # prolazimo kroz svih 500 tačaka
        dist = [] # dist je lista rastojanja tačke od svih klastera
        for j in range(k):
            dist.append(distance(X[i], clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred

print("---------------------")
clusters = assign_clusters(X, clusters)
print(clusters)
clusters = update_clusters(X,clusters)
print(clusters)
print("---------------------")
pred = pred_cluster(X, clusters)
print(pred)


# Plot the data points with their predicted cluster center
plt.scatter(X[:,0],X[:,1],c = pred)
for i in clusters:
    center = clusters[i]['center']
    plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.show()