import numpy as np

class Augmentacja:
    def __init__(self, x_points, y_points):

        if len(x_points) != len(y_points):
            raise ValueError("Length of x_points and y_points must be equal")
            
        self.x = np.array(x_points)
        self.y = np.array(y_points)
        self.n_points = len(self.x)
        
    def get_points(self):
        return self.x, self.y
        
    def get_points_as_tuples(self):
        return list(zip(self.x, self.y))