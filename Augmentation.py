import Coordinate as co
import DataPrepUtils as dp
import DataUtils as du
import Section as sec
from sklearn.datasets import make_blobs
from icecream import ic

# tab = []
# for i in range(3):
    
#     tab.append(co.Coordinate(random.randint(1, 10), random.randint(1, 10)))
   

# for i in range(3):
#     print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi())  
 
# co.Coordinate.shiftPhi = 3.14/2

# for i in range(3):
#     print(tab[i].getXY(),tab[i].getR(),tab[i].getPhi()) 


# class Augmentation():
#     print("Augmentation")

# print("-----------------")

# # sec = list(filter(lambda x: x.getPhi() < 5.97 and x.getPhi() > 5.17, tab))

# # for s in sec:
# #     print(s.getXY(),s.getR(),s.getPhi()) 


# # max_object = max(tab, key=lambda tab: tab.getR())


# # print(max_object.getXY(),max_object.getR(),max_object.getPhi())


# print(max_r(tab).getXY(),max_r(tab).getR(),max_r(tab).getPhi())

# print("-----------------")

n_angles = 5

x_train, y_train = make_blobs(n_samples=50000, centers=1, random_state=42, cluster_std=1.0)

x_train = dp.DataPrepUtils.normalize_data(x_train)

x_train = dp.DataPrepUtils.remove_outliers_lof(x_train)

x_train = dp.DataPrepUtils.shift_to_mass_center(x_train)

x_train = dp.DataPrepUtils.listed_class(x_train)

shifted_phi = du.DataUtils.setPhiShift(x_train)

max_r = du.DataUtils.max_radious(x_train).getPhi()

# print(shifted_phi)

# print(max_r)

# section_len = sec.Section.list_of_elements_number_in_sections(n_angles, x_train)

# # ic(section_len)
# # ic(len(x_train))
# # ic(sum(section_len))

# # ic(sum(generated_points_per_section))

# # ic(min(generated_points_per_section))

# ic(sec.Section.list_of_elements_number_in_sections(n_angles, x_train))

# ic(sec.Section.number_of_generated_points_per_section(n_angles, x_train, 1000))

# ic(sec.Section.difference_between_generated_points(n_angles, x_train, 1000))

# ic(sec.Section.less_generated_points_list_index(n_angles, x_train, 1000))

# ic(sec.Section.equalize_generated_points(n_angles, x_train, 1000))

# ic(sec.SubSection.list_of_subsections_number_by_section(n_angles, x_train))

# print(x_train[0].getXY(), x_train[0].getR(), x_train[0].getPhi())
# print(len(x_train))
