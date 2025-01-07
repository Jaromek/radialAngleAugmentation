import numpy as np
import Coordinate as co
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
from typing import List

class DataUtils:
    section_angle_number = 1

    def __init__(self , section_angle_number:int):
        self.section_angle_number = section_angle_number
        
    def max_radious_object(data_xy):
        max_object = max(data_xy, key=lambda data_xy: data_xy.getR())
        return max_object
    
    def setPhiShift(data_xy):
        co.Coordinate.shiftPhi = DataUtils.max_radious_object(data_xy).getPhi()
        return co.Coordinate.shiftPhi
    
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
    
    def listed_class(data)->List[co.Coordinate]:
        return [co.Coordinate(point[0], point[1]) for point in data]
    


    

if __name__ == '__main__':
    tab:List[co.Coordinate] = []
