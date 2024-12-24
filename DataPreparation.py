import numpy as np
import Coordinate as co
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor

class DataPreparation:

    @staticmethod
    def shift_to_mass_center(array):
        mean_x = np.mean(array[:, 0])
        mean_y = np.mean(array[:, 1])
        shifted_array = array - [mean_x, mean_y]
        return shifted_array
    
    
    @staticmethod
    def remove_outliers_lof(data, n_neighbors=20):
        lof = LocalOutlierFactor(n_neighbors=n_neighbors)
        outliers = lof.fit_predict(data)
        return data[outliers == 1]
    
    
    @staticmethod
    def normalize_data(data):
        scaler = StandardScaler()
        return scaler.fit_transform(data)
    

    @staticmethod
    def data_to_polar(data):
        polar_data = [[co.Coordinate.getR(point) , co.Coordinate.getPhi(point)] for point in data]
        return polar_data
    

    @staticmethod
    def sort_data(data):
        return sorted(data, key=lambda x: x[0])

        