import sklearn as sk
import numpy as np
import scipy as sp
from icecream import ic

def dataResults(data):

    pearson_cov = sp.stats.pearsonr(data[:, 0], data[:, 1])

    pca1D = sk.decomposition.PCA(n_components=1)
    pca1D.fit(data)

    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    ic(pearson_cov, mean, median, variance)

    return pearson_cov, mean, median, variance