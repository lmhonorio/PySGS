import numpy as np
import matplotlib.pyplot as plt
import copy
import time

import DataManagement
import OrientedBoundHyperBox
import Projections
import SeparatingAxes
import PrintData



t0 = time.clock()

myData = DataManagement.clsDataIO()

#list_cls = myData.returnBananaDataset((100,100), (2.0,1.0), 1.7, 0.2)
list_cls = myData.returnCheckerBoardFunction(50,2,1,0.55)


obbs = [OrientedBoundHyperBox.clsOBHB(obj_data = idata)	for idata in list_cls]

print('volume inicial')
print(obbs[0].projections.box_volume)
print(obbs[1].projections.box_volume)

#OrientedBoundHyperBox.clsOBHB.improveDataFitness(obbs)
   
#obbs[0].projections = obbs[0].projections.improveDataFitness()
#obbs[1].projections = obbs[1].projections.improveDataFitness()
   

ok, separating_axes, MtrCol = SeparatingAxes.clsCollisionTest.CollisionTest(obbs[0],obbs[1],True)

print('colisao: ' + str(ok) + ' , ' + str(len(separating_axes.separatin_axes)))

print(time.clock() - t0)
print(list_cls[0].x_mean)
print(list_cls[0].word_ref_center)



print(time.clock() - t0)
PrintData.clsPrint.print2dmodel(obbs)
i=1



