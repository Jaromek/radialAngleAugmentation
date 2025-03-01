import Augmentation as au
import DataUtils as du

def radiousAngleMethod(data, section_count, global_points_gen):
    data = du.DataUtils.listed_class(data)
    phiShiftByMaxRadious = du.DataUtils.getPhiShiftByMaxRadious(data, section_count)
    du.DataUtils.addShiftPhi(data, -phiShiftByMaxRadious)
    au.Augmentation(points=data, section_count=section_count, global_points_gen=global_points_gen)
    du.DataUtils.addShiftPhi(data, phiShiftByMaxRadious)
    return [point.getXY() for point in data]