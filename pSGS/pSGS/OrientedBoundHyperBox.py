import numpy as np
import DataModel
import Projections

class clsOBHB(DataModel.clsData,object):
	"""description of class"""



	def __init__(self, setid = 0, incollision = 0, breaks = 0, data = [], objData = DataModel.clsData()):

		if len(objData.data)==0:
			DataModel.clsData.__init__(self,setid,incollision,breaks,data)
		else:
			DataModel.clsData.__init__(self,objData.setid,objData.incollision,objData.breaks,objData.data)
			
		self.projections = Projections.clsProjectionOverAxis(self.data,self.WordRefcenter,self.Pi)

		#prj = Projections.clsProjectionOverAxis(List2.data,List2.xmean,List2.Pi)



	def evaluateBoundingBox(self):
		if dimension == 0:
			return []


	def returnBox(self):
		return np.array(self.projections.returnOrientedBoundingBox(self.Pi)) 











