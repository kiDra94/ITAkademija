import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

iris = pd.read_csv("Iris.csv")
#print(iris.to_string())
x = iris.iloc[:, [0, 1, 2, 3]].values #uzima kolone koje smo naveli! [0, 1, 2, 3], a :, govori koliko vrsta tj redova hocemo
#x = iris.iloc[:5, [0, 1, 2, 3]].values
print(x)
iris.info()
print(iris[0:10])
print("_---------------------_")

# Frequency distribution of species"
iris_outcome = pd.crosstab(index=iris["Species"],  # Make a crosstab
                           columns="count")  # Name the count column

print(iris_outcome)
print("_---------------------_")

iris_setosa = iris.loc[iris["Species"] == "Iris-setosa"]
iris_virginica = iris.loc[iris["Species"] == "Iris-virginica"]
iris_versicolor = iris.loc[iris["Species"] == "Iris-versicolor"]

print(iris_setosa)
print("_---------------------_")

sns.FacetGrid(iris, hue="Species", height=3).map(sns.histplot, "PetalLengthCm").add_legend()
plt.savefig("PentalLengthCm.png") #snima figuru
sns.FacetGrid(iris, hue="Species", height=3).map(sns.histplot, "PetalWidthCm").add_legend()
sns.FacetGrid(iris, hue="Species", height=3).map(sns.histplot, "SepalLengthCm").add_legend()
sns.FacetGrid(iris, hue="Species", height=3).map(sns.histplot, "SepalWidthCm").add_legend()

sns.FacetGrid(iris, hue="Species", height=3).map(sns.distplot, "PetalLengthCm").add_legend()
sns.FacetGrid(iris, hue="Species", height=3).map(sns.distplot, "PetalWidthCm").add_legend()
sns.FacetGrid(iris, hue="Species", height=3).map(sns.distplot, "SepalLengthCm").add_legend()
sns.FacetGrid(iris, hue="Species", height=3).map(sns.distplot, "SepalWidthCm").add_legend()
#plt.show()
print("_---------------------_")