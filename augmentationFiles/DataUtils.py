import numpy as np
import Coordinate as co
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
from typing import List
import math

class DataUtils:
    section_angle_number = 1

    def __init__(self , section_angle_number:int):
        self.section_angle_number = section_angle_number
        
    def max_radious_object(data_xy):
        max_object = max(data_xy, key=lambda data_xy: data_xy.getR())
        return max_object
    
    def getPhiShiftByMaxRadious(data_xy, n_angles):        
        return DataUtils.max_radious_object(data_xy).getPhi() - np.pi/n_angles

    def getPhiShift():   
        return co.Coordinate.shiftPhi
    
    def mass_center(data):
        mean_x = np.mean(data[:, 0])
        mean_y = np.mean(data[:, 1])
        shift_vector = [mean_x, mean_y]
        return shift_vector

    def shift_by_vector(array, shift_vector):
        if np.array(array).size == 0:
            return array
        shifted_array = np.subtract(array, shift_vector)
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
    

    def addShiftPhi(data, shiftPhi):

        for point in data:
            if point.shiftPhi + shiftPhi < 0:
               shiftPhi_ = 2*math.pi - ((-(point.shiftPhi + shiftPhi)) % (2*math.pi))
            else:
               shiftPhi_ = (point.shiftPhi + shiftPhi) % (2*math.pi)
        
            point.setShiftPhi(shiftPhi_)
        
            if point.phi + shiftPhi < 0:
               shiftPhi_ = 2*math.pi -((-(point.phi + shiftPhi)) % (2*math.pi))
            else:
               shiftPhi_ = (point.phi + shiftPhi) % (2*math.pi)

            point.setPhi(shiftPhi_)  
