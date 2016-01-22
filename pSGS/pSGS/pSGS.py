import numpy as np
import matplotlib.pyplot as plt
import DataManagement
import time
import OrientedBoundHyperBox
import Projections
import PrintData
import copy


t0 = time.clock()

myData = DataManagement.clsDataIO()

#list_cls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)
list_cls = myData.returnCheckerBoardFunction(100,3,1,0.5)


obbs = [OrientedBoundHyperBox.clsOBHB(obj_data = idata)	for idata in list_cls]

#PrintData.clsPrint.print2dmodel(obbs)
print('volume inicial')
print(obbs[0].projections.box_volume)
print(obbs[1].projections.box_volume)
PrintData.clsPrint.print2dmodel(obbs)

obbs[0].projections = obbs[0].projections.improveDataFitness()
obbs[1].projections = obbs[1].projections.improveDataFitness()
print('volume final')
print(obbs[0].projections.box_volume)
print(obbs[1].projections.box_volume)
print('--------------------')
#PrintData.clsPrint.print2dmodel(obbs)
#min_break_at = obbs[1].kernelDensityEstimation(False)
#nobb = obbs[1].breakThisBondingBoxUsingKDE()

PrintData.clsPrint.print2dmodel(obbs)


print(time.clock() - t0)
print(list_cls[0].x_mean)
print(list_cls[0].word_ref_center)



print(time.clock() - t0)




