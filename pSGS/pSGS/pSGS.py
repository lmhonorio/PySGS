import numpy as np
import matplotlib.pyplot as plt
import copy
import time

import DataManagement
import OrientedBoundHyperBox
import Projections
import SeparatingAxes
import PrintData



t0 = time.time()

myData = DataManagement.clsDataIO()

#list_cls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)
list_cls = myData.returnCheckerBoardFunction(50,2,1,0.3)

obhbs = OrientedBoundHyperBox.clsListofOBHB(list_cls)

has_collision, separating_axes, MtrCol = SeparatingAxes.clsCollisionTest.TestAllAgainstAll(obhbs)

print('colisao: ' + str(bool(has_collision)) + ' , ' + str(len(separating_axes.separatin_axes)))
							 
print(time.time() - t0)
print(list_cls[0].x_mean)
print(list_cls[0].word_ref_center)



print(time.time() - t0)
PrintData.clsPrint.print2dmodel(obhbs)
i=1



