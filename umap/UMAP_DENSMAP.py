import umap
import hdbscan
import matplotlib.pyplot as plt
from sys import displayhook
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

dft = pd.read_csv('../TSNE/10bar_DATA_NODIM.csv')
dft = dft.set_index(dft.columns[0])

min_dist_param = 1.0 #0.5 #0    # Default parameter for UMAP
n_neigh_param = 50 #40 #30    # Default parameter for UMAP

cluster_sel_param = 0.5 #0.7 #0.63 #  Default parameter for HDBSCAN_2D or HDBSCAN_HD
min_samp_param = 20 #10 #1       #  Default parameter for HDBSCAN_2D or HDBSCAN_HD
min_cluster_param = 60 #40 #50   #  Default parameter for HDBSCAN_2D or HDBSCAN_HD

embeddings_em = umap.UMAP(densmap=True,
                    n_neighbors=n_neigh_param,
                    min_dist=min_dist_param,
                    n_components=2,
                    random_state=200,
                    low_memory=False).fit_transform(dft)
clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_param, min_samples=min_samp_param,
                                        cluster_selection_epsilon=cluster_sel_param).fit(embeddings_em)
cluster_labels = clusterer.labels_

fig, ax = plt.subplots()
figname_bl = (f'TEST1')
scatter = plt.scatter(
    embeddings_em[:, 0], embeddings_em[:, 1], c=cluster_labels, cmap='Spectral', s=15)
# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)
# Set plot title and axis labels
# Set plot title and axis labels
#plt.title(''f'{Data_projection} + {Data_clustering}''')
plt.xlabel('UMAP-1')
plt.ylabel('UMAP-2')

plt.savefig(figname_bl, dpi=300)