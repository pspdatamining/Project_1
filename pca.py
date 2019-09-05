#should optimize most of the steps later

import numpy as np
import pandas as pd

#setting random seed
np.random.seed(0)

pca_a = pd.read_csv('pca_a.txt', 
                    delimiter="\t", 
                    index_col=False, 
                    header=None, 
                    names=["feature_1", "feature_2", "feature_3", "feature_4", "disease"])
# print(pca_a)

# with open('pca_a.txt') as file:
#     pca_a = []
#     for line in file:
#         # print(line)
#         pca_a.append(line)

mean_1 = pca_a["f_1"].mean()
mean_2 = pca_a["f_2"].mean()
mean_3 = pca_a["f_3"].mean()
mean_4 = pca_a["f_4"].mean()

mean_vector = np.array([[mean_1],[mean_2],[mean_3],[mean_4]])

cov_mat = pca_a.cov() #implement covariance matrix function

#find eigenvectors and eigenvalues



