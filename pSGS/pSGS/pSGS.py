import numpy as np
import matplotlib.pyplot as plt
import DataManagement
import time
import OrientedBoundHyperBox
import Projections
import PrintData

t0 = time.clock()

myData = DataManagement.clsDataIO()

ListCls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)


OBHB = [OrientedBoundHyperBox.clsOBHB(objData = idata)	for idata in ListCls]


PrintData.clsPrint.print2dModel(OBHB)



print(time.clock() - t0)
print(ListCls[0].xmean)
print(ListCls[0].WordRefcenter)



print(time.clock() - t0)




