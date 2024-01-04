from sys import displayhook
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn import preprocessing
import csv

#r = pd.read_csv('PORESIZE_MORE10.csv')
r = pd.read_csv('10bar_DATA_NODIM.csv')
features=['PS', 'WS', 'MC','UPTAKE', 'QH']
from sklearn.preprocessing import StandardScaler
dft=r.loc[:,features].values
#print(dft)
displayhook(dft.shape)

dft = StandardScaler().fit_transform(dft)
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(dft)
print(principalComponents.shape)
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
f = open("pca_comp_3D_At10barNODIMNOMCOORD1.csv", "w")
writer = csv.writer(f)
writer.writerows(principalComponents)
f.close()
