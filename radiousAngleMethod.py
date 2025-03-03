import Augmentation as au
import DataUtils as du
import numpy as np

def radiousAngleMethodForSingleClass(dataset_data, dataset_target, section_count, global_points_gen):

    dataset_data = du.DataUtils.listed_class(dataset_data)
    phiShiftByMaxRadious = du.DataUtils.getPhiShiftByMaxRadious(dataset_data, section_count)
    du.DataUtils.addShiftPhi(dataset_data, -phiShiftByMaxRadious)

    dataset_data = au.Augmentation(points=dataset_data, section_count=section_count, global_points_gen=global_points_gen)
    du.DataUtils.addShiftPhi(dataset_data, phiShiftByMaxRadious)

    return [point.getXY() for point in dataset_data], [dataset_target for targets in range(len(dataset_data))]


def radiousAngleMethod(dataset_data, dataset_targets, section_count):

    unique_classes, counts = np.unique(dataset_targets, return_counts=True)
    max_count = np.max(counts)

    for i, abstractClass in enumerate(unique_classes):

        difference = max_count - counts[i]

        if difference > 0:

            shift_vector = du.DataUtils.mass_center(dataset_data[dataset_targets == abstractClass])

            dataset_data[dataset_targets == abstractClass] = du.DataUtils.shift_by_vector(
                dataset_data[dataset_targets == abstractClass],
                shift_vector
            )

            augmented_data, augmented_target = radiousAngleMethodForSingleClass(
                dataset_data[dataset_targets == abstractClass],
                abstractClass,
                section_count,
                global_points_gen=difference
            )

            shift_vector = [-shift_vector[0], -shift_vector[1]]
            dataset_data[dataset_targets == abstractClass] = du.DataUtils.shift_by_vector(
                dataset_data[dataset_targets == abstractClass],
                shift_vector
            )
            augmented_data = du.DataUtils.shift_by_vector(augmented_data, shift_vector)

        else:
            continue

        

        dataset_data = np.concatenate((dataset_data, augmented_data), axis=0)
        dataset_targets = np.concatenate((dataset_targets, augmented_target), axis=0)

        

    return dataset_data, dataset_targets
