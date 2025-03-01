import Augmentation as au
import DataUtils as du
import numpy as np

def radiousAngleMethodForSingleClass(dataset_data, dataset_target, section_count, global_points_gen):
    
    dataset_data = du.DataUtils.listed_class(dataset_data)
    phiShiftByMaxRadious = du.DataUtils.getPhiShiftByMaxRadious(dataset_data, section_count)
    du.DataUtils.addShiftPhi(dataset_data, -phiShiftByMaxRadious)
    au.Augmentation(points=dataset_data, section_count=section_count, global_points_gen=global_points_gen)
    du.DataUtils.addShiftPhi(dataset_data, phiShiftByMaxRadious)

    return [point.getXY() for point in dataset_data], [dataset_target for targets in range(len(dataset_data))]

def radiousAngleMethod(dataset_data, dataset_targets, section_count):

    unique_classes, counts = np.unique(dataset_targets, return_counts=True)

    for abstractClass in unique_classes:

        difference = abs(np.max(unique_classes) - abstractClass)

        if difference != 0:

            augmented_data, augmented_target = radiousAngleMethodForSingleClass(dataset_data[dataset_targets == abstractClass], abstractClass, section_count, global_points_gen = difference)


        else:
            continue

        dataset_data = np.concatenate((dataset_data, augmented_data), axis=0)
        dataset_targets = np.concatenate((dataset_targets, augmented_target), axis=0)

    return dataset_data, dataset_targets