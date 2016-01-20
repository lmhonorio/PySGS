import numpy as np
import DataModel
import Projections

class clsOBHB(DataModel.clsData,object):
	"""description of class"""



	def __init__(self, set_id = 0, in_collision = 0, breaks = 0, data = [], obj_data = DataModel.clsData()):

		if len(obj_data.data)==0:
			DataModel.clsData.__init__(self,set_id,in_collision,breaks,data)
		else:
			DataModel.clsData.__init__(self,obj_data.set_id,obj_data.in_collision,obj_data.breaks,obj_data.data)
			
		self.projections = Projections.clsProjectionOverAxis(self.data,self.word_ref_center,self.pi)

		#prj = Projections.clsProjectionOverAxis(List2.data,List2.xmean,List2.Pi)



	def evaluateBoundingBox(self):
		if dimension == 0:
			return []


	def returnBox(self):
		return np.array(self.projections.returnOrientedBoundingBox(self.pi)) 











