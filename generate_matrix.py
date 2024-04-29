import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.cluster.hierarchy as sch
import seaborn as sns
import glob

def MTAC_matrix():
    file_list = glob.glob("*.txt")
    listID = []
    for i in range(0, len(file_list)):
        data = pd.read_csv(file_list[i], sep="\t")
        data_FC = data[data["log2(FC)"] > 0.7]
        data_sig = data_FC[data_FC["P-adj"] < 0.05]
        listID.extend(data_sig["GeneID"].to_list())
    data_all_ID = pd.DataFrame({"GeneID":listID})
    data_all_ID.to_csv("data_all_ID.bed", index=False, sep="\t")
    ID = pd.read_csv("data_all_ID.bed", sep="\t")
    ID_unique = ID.sort_values(by=["GeneID"]).drop_duplicates().reset_index(drop=True)
    for i in range(0, len(file_list)):
        data = pd.read_csv(file_list[i], sep="\t")
        data_filtered = data[data["GeneID"].isin(ID_unique["GeneID"])].reset_index(drop=True)
        data_short = pd.concat([data_filtered["GeneID"], data_filtered["log2(FC)"]], axis=1)
        ID_unique = ID_unique.merge(data_short, how="left", on=["GeneID"])
        ID_unique.rename({'log2(FC)': file_list[i].split(".")[0]}, axis=1, inplace=True)
    ID_unique.to_csv("MTAC_matrix.bed", index=False, sep="\t")

MTAC_matrix()
