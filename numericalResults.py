import sklearn as sk
import numpy as np
import scipy as sp
from icecream import ic
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def dataResults(data: list, data_features: list, default_features: list, name: str):

    unique_classes, counts = np.unique(default_features, return_counts=True)
    max_count = np.max(counts)

    for i, unique_class in enumerate(unique_classes):

        difference = max_count - counts[i]

        if difference > 0:
            
            dataframe = pd.DataFrame(data[data_features == unique_class], columns=['x', 'y'])
            correlation_matrix = dataframe.corr()
            sns.heatmap(correlation_matrix, annot=True, cbar=False)
            plt.show()

            ic(unique_class)
            ic(sp.stats.pearsonr(dataframe['x'], dataframe['y']))


    pearson_cov = sp.stats.pearsonr(data[:, 0], data[:, 1])

    pca1D = sk.decomposition.PCA(n_components=1)
    data = pca1D.fit_transform(data)

    desc = pd.DataFrame(data, columns=[f'{name}']).describe()
    variance = np.var(data)
    
    ic(pearson_cov, variance, desc)

    print('---------------------------------------------------------------------------------------------------------------')

    return pearson_cov, variance, desc

# def correlationResults(*datasets_to_correlate_with_features: list, default_dataset: list, default_features: list):

#     unique_classes, counts = np.unique(default_features, return_counts=True)
#     max_count = np.max(counts)

#     for i, unique_class in enumerate(unique_classes):

#         difference = max_count - counts[i]

#         if difference > 0:
            
#             for dataset in datasets_to_correlate_with_features[0]:  
#                 print(unique_class)          
#                 dataframe = pd.DataFrame(dataset[datasets_to_correlate_with_features[1] == unique_class], columns=['x', 'y'])
#                 correlation_matrix = dataframe.corr()
#                 sns.heatmap(correlation_matrix, annot=True, cbar=False)
#                 plt.show()
#                 print(sp.stats.pearsonr(dataframe['x'], dataframe['y']))


#     ic(unique_classes, counts, max_count)