from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import mode
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE
from sklearn.metrics import confusion_matrix
sns.set()

digits = load_digits()
print(digits.data.shape) #(1797, 64) 1797 broja u 64 koordinate (8x8 matrice), koordinate su osvetljenje
print(digits.data) #tacke

#stampa pojedinacne tacke sa osvjetljenjima
'''
for i in digits.data:
    print(i)
    print(sum(i))'''

# postavljanje početnih centara
kmeans = KMeans(n_clusters=10, random_state=0) #KMeans algoritam koji koristimo
clusters = kmeans.fit_predict(digits.data) #ubacuje tacke u model
print(kmeans.cluster_centers_.shape) #(10, 64) , deset tacka (to su centri)

# prikaz početnih centara
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

plt.show()

# labele date u skladu sa klasterima
labels = np.zeros_like(clusters) #dodjeljuju se klusterima najblize tacke [0 0 0 ... 0 0 0]\n[0 1 2 ... 8 9 8]
print(labels)
for i in range(10):
    mask = (clusters == i) 
    labels[mask] = mode(digits.target[mask])[0] #svaka tacka dobije cluster koji jooj pripada

print(digits.target)
print(accuracy_score(digits.target, labels)) #0.7440178074568725


mat = confusion_matrix(digits.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=digits.target_names,
            yticklabels=digits.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

# Project the data: this step will take several seconds
tsne = TSNE(n_components=2, init='random', random_state=0)
digits_proj = tsne.fit_transform(digits.data)

# Compute the clusters
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(digits_proj)

# Permute the labels
labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask])[0]

# Compute the accuracy
print(accuracy_score(digits.target, labels))
mat = confusion_matrix(digits.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=digits.target_names,
            yticklabels=digits.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()




