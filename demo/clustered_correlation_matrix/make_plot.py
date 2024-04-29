import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.cluster.hierarchy as sch
import seaborn as sns
import glob

matrix = pd.read_csv("clustered_pearson_correlation.txt", sep="\t")
matrix = matrix.set_index("GeneID")
sns.heatmap(matrix, cmap = "RdBu_r", yticklabels=False, xticklabels=False)
plt.savefig('heatmap.png')
