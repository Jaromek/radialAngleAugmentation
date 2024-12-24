import numpy as np

class DataPreparation():

    def shift_to_mass_center(array):
        mass_center_x = np.mean(array[:, 0])
        mass_center_y = np.mean(array[:, 1])
        shifted_array = array - [mass_center_x, mass_center_y]
        return shifted_array
