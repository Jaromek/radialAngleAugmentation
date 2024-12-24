import numpy as np
import Coordinate as co
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor

class DataPreparation():
  
    def shift_to_mass_center(array):
        mean_x = np.mean(array[:, 0])
        mean_y = np.mean(array[:, 1])
        shifted_array = array - [mean_x, mean_y]
        return shifted_array
    

    def remove_outliers_lof(data, n_neighbors=20):
        lof = LocalOutlierFactor(n_neighbors=n_neighbors)
        outliers = lof.fit_predict(data)
        return data[outliers == 1]
    

    def normalize_data(data):
        scaler = StandardScaler()
        return scaler.fit_transform(data)
    
    def data_to_polar(data):
        polar_data = [[data[i].co.Coordinate.getR(), data[i].co.Coordinate.getPhi()] for i in range(len(data))]
        return polar_data


    def sort_data(data):
        key = lambda x: x[1]
        return sorted(data, key=key)
        