import DataPrepUtils as dp
import Coordinate as co
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import pandas as pd
import random

import GeometryUtils as gu

#tworzenie zbiory danych dwu wymiarowych x_train oraz y_train za pomocą funkcji make_blobs z sklearn.datasets.
#Jest w tym zbiorze danych 500 punktów otoczonych wokół jednego centrum, które zostały stworzone w oparciu o jedno odchylenie standardowe
x_train, y_train = make_blobs(n_samples=500, centers=1, random_state=42, cluster_std=1.0)

#pokazywanie że w x_train znajdują się dwie kolumny o liczbie wierszy 300

#skalowanie danych Standardowym skalowaniem z biblioteki sklearn.preprocesing
x_train = dp.DataPrepUtils.normalize_data(x_train)

#aplikowanie metody LOF
x_train = dp.DataPrepUtils.remove_outliers_lof(x_train)

#przesunięcie danych do środka masy
x_train = dp.DataPrepUtils.shift_to_mass_center(x_train)

phi = co.Coordinate.getPhi(co.Coordinate(1, 1))
r = co.Coordinate.getR(co.Coordinate(x_train[0][0], x_train[0][1]))

print(phi)
print(r)