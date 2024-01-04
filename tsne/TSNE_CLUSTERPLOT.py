from sys import displayhook
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import seaborn as sns
from sklearn import preprocessing
from bioinfokit.visuz import cluster
from sklearn.cluster import DBSCAN
# Input Data file needs to be changed here
dft = pd.read_csv('10bar_DATA_NODIM.csv')
dft = dft.set_index(dft.columns[0])

# displayhook(dft.shape)

# pca_scores = PCA().fit_transform(dft)
# print(pca_scores)
# df_pc = pd.DataFrame(pca_scores)
#df_pc = preprocessing.normalize(dft)
tsne_em = TSNE(n_components=2, perplexity=30, n_iter=1000, learning_rate=200, init= 'random', random_state= 200000).fit_transform(dft)
cluster.tsneplot(score=tsne_em)
get_clusters = DBSCAN(eps=0.5, min_samples=5).fit_predict(dft)
#set(get_clusters)
cluster.tsneplot(figname='TEST1', score=tsne_em, colorlist=get_clusters, 
    colordot=('#713e5a', '#63a375', '#edc79b', '#d57a66', '#ca6680', '#395B50', '#92AFD7', '#b0413e', '#4381c1', '#736ced', '#631a86', '#de541e', '#022b3a', '#000000'), 
    legendpos='upper right', legendanchor=(1.15, 1))
