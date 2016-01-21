import numpy as np
import matplotlib.pyplot as plt
import DataManagement
import time
import OrientedBoundHyperBox
import Projections
import PrintData


t0 = time.clock()

myData = DataManagement.clsDataIO()

list_cls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)
#list_cls = myData.returnCheckerBoardFunction(100,3,1,0.5)


obbs = [OrientedBoundHyperBox.clsOBHB(obj_data = idata)	for idata in list_cls]

#min_break_at = obbs[1].kernelDensityEstimation(False)
nobb = obbs[1].breakThisBondingBoxUsingKDE()

PrintData.clsPrint.print2dmodel(nobb)


print(time.clock() - t0)
print(list_cls[0].x_mean)
print(list_cls[0].word_ref_center)



print(time.clock() - t0)




