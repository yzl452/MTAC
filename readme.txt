# MTAC custom code

This custom code is used to generate the clustered correlation heatmap in Figure 6B.

## Installation

Unzip the custom_code.zip.

## Usage

##1. Generate MTAC matrix for multiple VPs.

Collect DESeq2 output files for each VP, put them in the same folder and run generate_matrix.py

Example:
cd custom_code\demo\DESeq2_file
python generate_matrix.py

Expected output:
MTAC_matrix.bed

##2. Calculate the pairwise pearson's correlation for each NDR, and do the clustering analysis.

Run cluster_matrix.py in a folder containing the MTAC_matrix.bed

Example:
cd custom_code\demo\correlation_matrix
python cluster_matrix.py

Expected output: 
pearson_correlation.txt, clustered_pearson_correlation.txt

##3. Make the heatmap.

Run make_plot.py in a folder containing the clustered_pearson_correlation.txt

Example:
cd custom_code\demo\clustered_correlation_matrix
python make_plot.py

Expected output:
heatmap.png

## License
MIT



