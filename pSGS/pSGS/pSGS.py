import numpy as np
import matplotlib.pyplot as plt
import DataManagement
import time
import OrientedBoundHyperBox
import Projections
import PrintData

t0 = time.clock()

myData = DataManagement.clsDataIO()

listcls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)


OBHB = [OrientedBoundHyperBox.clsOBHB(obj_data = idata)	for idata in listcls]


PrintData.clsPrint.print2dmodel(OBHB)



print(time.clock() - t0)
print(ListCls[0].xmean)
print(ListCls[0].word_ref_center)



print(time.clock() - t0)




