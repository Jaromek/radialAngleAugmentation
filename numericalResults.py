import sklearn as sk
import numpy as np
import scipy as sp
from icecream import ic
import pandas as pd

def dataResults(data: list, name: str):

    pearson_cov = sp.stats.pearsonr(data[:, 0], data[:, 1])

    pca1D = sk.decomposition.PCA(n_components=1)
    data = pca1D.fit_transform(data)

    desc = pd.DataFrame(data, columns=[f'{name}']).describe()
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)    
    

    ic(pearson_cov, mean, median, variance, desc)

    

    return pearson_cov, mean, median, variance