import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.cluster.hierarchy as sch
import seaborn as sns
import glob

def cluster_corr_ward(corr_array, inplace=False):
    pairwise_distances = sch.distance.pdist(corr_array, metric='euclidean')
    linkage = sch.linkage(pairwise_distances, method='ward')
    cluster_distance_threshold = pairwise_distances.max()/2
    idx_to_cluster_array = sch.fcluster(linkage, cluster_distance_threshold, criterion='distance')
    idx = np.argsort(idx_to_cluster_array)
    if not inplace:
        corr_array = corr_array.copy()
    if isinstance(corr_array, pd.DataFrame):
        return corr_array.iloc[idx, :].T.iloc[idx, :]
    return corr_array[idx, :][:, idx]

matrix = pd.read_csv("MTAC_matrix.bed", sep="\t")
correlation = matrix.set_index("GeneID").T.corr(method="pearson")
correlation.to_csv("pearson_correlation.txt", sep="\t", index=False)
clustered = cluster_corr_ward(correlation)
clustered.to_csv("clustered_pearson_correlation.txt", sep="\t", index=False)
