import numpy as np
import DataModel
import Projections
import  matplotlib.pyplot as plt
from scipy import stats

class clsOBHB(DataModel.clsData, object):
	"""description of class"""



	def __init__(self, set_id = 0, in_collision = 0, breaks = 0, data = [], obj_data = DataModel.clsData()):

		if len(obj_data.data)==0:
			DataModel.clsData.__init__(self,set_id,in_collision,breaks,data)
		else:
			DataModel.clsData.__init__(self,obj_data.set_id,obj_data.in_collision,obj_data.breaks,obj_data.data)
		
				
		self.projections = Projections.clsProjectionOverAxis(self.data,self.word_ref_center)

		#prj = Projections.clsProjectionOverAxis(List2.data,List2.xmean,List2.Pi)



	def evaluateBoundingBox(self):
		if dimension == 0:
			return []


	def returnBox(self):
		return np.array(self.projections.returnOrientedBoundingBox()) 

	def breakThisBondingBoxUsingKDE(self):
		idx_max_lambda =  np.argmax(self.projections.Lambda)
		c_axis = np.array(self.projections.projection_over_pi[idx_max_lambda])
		i_break = self.kernelDensityEstimation()

		new_data_1 = []
		new_data_2 = []
		for i in range(0,self.dataLen):
			if c_axis[i] < i_break:
				new_data_1.append(self.data[i,:])
			else:
				new_data_2.append(self.data[i,:])


		pcls1 = DataModel.clsData(self.set_id,1,self.breaks)
		pcls2 = DataModel.clsData(self.set_id,1,self.breaks)

		pcls1.setData(new_data_1)
		pcls2.setData(new_data_2)

		new_obb_1 = clsOBHB(obj_data = pcls1)	
		new_obb_2 = clsOBHB(obj_data = pcls2)

		return new_obb_1,new_obb_2


	def kernelDensityEstimation(self, do_plot = False):
		
		#define biggest axis and get its data
		idx_max_lambda =  np.argmax(self.projections.Lambda)
		c_axis = np.array(self.projections.projection_over_pi[idx_max_lambda])

		#get the grid to project onto
		x_grid = np.linspace(c_axis.min(), c_axis.max(), len(c_axis)/2)
		
		#evaluate the KDEpdf
		kde_pdf = stats.gaussian_kde(c_axis).evaluate(x_grid)
		

		i_min,i_max = self.kdeLocalZeroGradient(kde_pdf)

		if (len(i_min) == 0):
			i_min.append(int(len(x_grid)/2))

		if (len(i_max) == 0):
			i_max.append(int(len(x_grid)/2))


		if do_plot:
			plt.plot(x_grid,kde_pdf,'r-')
			if len(i_min) > 0:
				plt.plot(x_grid[i_min],kde_pdf[i_min],'r*')
			if len(i_max) > 0:
				plt.plot(x_grid[i_max],kde_pdf[i_max],'b*')
			plt.show()

		i_lowest = np.argmin(kde_pdf[i_min])

		return x_grid[i_min[i_lowest]]


	def kdeLocalZeroGradient(self,kde:np.ndarray):
		i_len = len(kde)
		i_min = []
		i_max = []

		if i_len > 4:
			for i in range(2,i_len-1):
				last = kde[i-1]
				next = kde[i+1]
				current = kde[i]

				if current < last and current <next:
					i_min.append(i)
					#v_min.append(current)

				if current > last and current > next:
					i_max.append(i)
					#v_max.append(current)

		return i_min,i_max







													   








