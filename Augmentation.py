import Coordinate as co
import DataUtils as du
import SectionUtils as sec
from sklearn.datasets import make_blobs
from icecream import ic


n_angles = 5

x_train, y_train = make_blobs(n_samples=11000, centers=1, random_state=42, cluster_std=1.0)

x_train = du.DataUtils.normalize_data(x_train)

x_train = du.DataUtils.remove_outliers_lof(x_train)

x_train = du.DataUtils.shift_to_mass_center(x_train)

x_train = du.DataUtils.listed_class(x_train)

shifted_phi = du.DataUtils.setPhiShift(x_train)

max_r = du.DataUtils.max_radious_object(x_train).getPhi()