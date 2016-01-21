import DataModel
import numpy as np

class clsProjectionOverAxis(object):
	"""description of class"""

	def __init__(self, data :np.ndarray , world_ref_center:np.ndarray , axis:np.ndarray):
		self.data_to_world_ref_center = data - world_ref_center
		self.mod_pi = [np.linalg.norm(pi) for pi in axis]
		self.projection_over_pi = []
		self.min = []
		self.max = []
		self.delta_lambda = []
		self.volume = 1.0
		self.box_ref_center = []
		self.dimension = data.shape[1]

		for i in range(0,self.dimension):
			projection_over_pi = np.array(np.dot(self.data_to_world_ref_center, axis[i,:]) / self.mod_pi[i])
			vmin = projection_over_pi.min(0)
			vmax = projection_over_pi.max(0)
			self.projection_over_pi.append(projection_over_pi)
			self.min.append(vmin)
			self.max.append(vmax)
			delta_lambda = (np.array(vmax) - np.array(vmin))/2.0
			self.delta_lambda.append(delta_lambda)
			self.volume *= self.volume * delta_lambda 

		#self.center = center + 0.5 * np.dot(np.array(self.min) + np.array(self.max),axis)
		#o min e max se referem ao centro na coordenada do box, para a coordenada do mundo devemos transformar
		# de acordo com o centro do mundo e a matriz de rotação dada pelos autovetores.
		self.box_ref_center = world_ref_center + 0.5 * np.dot(axis.transpose(),np.array(self.min) + np.array(self.max))



	def myAxis(self, i:int, axis:np.ndarray):
		return  self.delta_lambda[i] * axis[i,:]


	def returnOrientedBoundingBox(self ,axis : np.ndarray):
		point = []
		point.append(self.box_ref_center + self.myAxis(0,axis) + self.myAxis(1,axis))
		point.append(self.box_ref_center - self.myAxis(0,axis) + self.myAxis(1,axis))
		point.append(self.box_ref_center - self.myAxis(0,axis) - self.myAxis(1,axis))
		point.append(self.box_ref_center + self.myAxis(0,axis) - self.myAxis(1,axis))
		point.append(self.box_ref_center + self.myAxis(0,axis) + self.myAxis(1,axis))

		return point;

	@property
	def density(self):
		return self.data_to_world_ref_center.size/self.volume

			#projection_over_Pi = 
			


		

	






