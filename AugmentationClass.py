
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import math
from matplotlib.patches import Wedge
import random

#funkcja pozwalająca określićodlegość punktu od środka wykresu
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum(point1** 2 + point2**2))

def is_in_radious(radious_point_ref_x, radious_point_ref_y, radious_point_ref_r):
    return radious_point_ref_x**2 + radious_point_ref_y**2 <= radious_point_ref_r**2

#obliczanie najdłuższego dystansu od początku osi
def longest_distance(data):
  tab = []

  for i in range(len(data)):

    center_distance = euclidean_distance(data[i][0], data[i][1])

    tab.append([center_distance,data[i][0],data[i][1]])

  return tab

def angle_vector_point(vector1, vector_points):
    angle = math.acos(np.dot(vector1, vector_points)/(euclidean_distance(vector1[0],vector1[1])*euclidean_distance(vector_points[0],vector_points[1])))
    vector_prod = np.cross(vector1, vector_points)
    if vector_prod > 0:
        angle = angle
    elif vector_prod < 0:
        angle = 2*np.pi - angle
    else:
        return 0
    return angle

#wykorzystywanie metody KNN do usunięcia anomalii. Jeżeli jakiś punkt nie ma wokół siebie 20 sąsiadów to znaczy, że jest w pewnym sensie anomalią,
#więc możemy go odrzucić z naszego zbioru danych
def remove_outliers_lof(data, n_neighbors=20):
    lof = LocalOutlierFactor(n_neighbors=n_neighbors)
    outliers = lof.fit_predict(data)
    return data[outliers == 1]

#funkcja zwraca promienie w danych sektorach, tak aby te sektory miały równe pola
def radious_of_equal_areas(radious, area_count):
    radiouses_of_sector = []
    smallest_r = radious * np.sqrt(area_count)/area_count
    radiouses_of_sector.append(smallest_r)
    for i in range(2,area_count+1):
        radious_i = smallest_r * np.sqrt(i)
        radiouses_of_sector.append(radious_i)
    radiouses_of_sector.insert(0,0)
    return radiouses_of_sector

#funkcja sprawdza czy dany punkt jest zawarty w danym kącie
def is_in_angle(coord_x, coord_y, angle_start, angle_end):
    angle_point_carthesian_coord = angle_vector_point([1,0], [coord_x,coord_y])

    if angle_end - angle_start >= 0:
        if angle_start < angle_point_carthesian_coord <= angle_end:
            return True
        else:
            return False
    else:
        angle_start = angle_start + 2*np.pi
        if angle_start < angle_point_carthesian_coord <= angle_end:
            return True
        else:
            return False


def compare_points(array1, array2):
    # Tablica na różniące się punkty
    difference_tab = []

    # Zaokrąglamy punkty w array2 do porównania
    rounded_array2 = [[round(x, 5), round(y, 5)] for x, y in array2]

    # Porównanie punktów
    for x, y in array1:
        rounded_point = [round(x, 5), round(y, 5)]
        if rounded_point not in rounded_array2:
            difference_tab.append(rounded_point)

    return difference_tab

