import DataModel
import numpy as np

class clsProjectionOverAxis(object):
	"""description of class"""

	def __init__(self, data :np.ndarray , WorldRefcenter:np.ndarray , axis:np.ndarray):
		self.data_to_WorldRefcenter = data - WorldRefcenter
		self.mod_Pi = [np.linalg.norm(pi) for pi in axis]
		self.projection_over_Pi = []
		self.min = []
		self.max = []
		self.deltaLambda = []
		self.volume = 1.0
		self.dimension = data.shape[1]

		for i in range(0,self.dimension):
			Projection_over_pi = np.array(np.dot(self.data_to_WorldRefcenter, axis[i,:]) / self.mod_Pi[i])
			vmin = Projection_over_pi.min(0)
			vmax = Projection_over_pi.max(0)
			self.projection_over_Pi.append(Projection_over_pi)
			self.min.append(vmin)
			self.max.append(vmax)
			Deltalambda = (np.array(vmax) - np.array(vmin))/2.0
			self.deltaLambda.append(Deltalambda)
			self.volume *= self.volume * Deltalambda 

		#self.center = center + 0.5 * np.dot(np.array(self.min) + np.array(self.max),axis)
		#o min e max se referem ao centro na coordenada do box, para a coordenada do mundo devemos transformar
		# de acordo com o centro do mundo e a matriz de rotação dada pelos autovetores.
		self.BoxRefcenter = WorldRefcenter + 0.5 * np.dot(axis.transpose(),np.array(self.min) + np.array(self.max))



	def myAxis(self, i:int, axis:np.ndarray):
		return self.deltaLambda[i] * axis[i,:]


	def returnOrientedBoundingBox(self ,axis : np.ndarray):
		point = []
		point.append(self.BoxRefcenter + self.myAxis(0,axis) + self.myAxis(1,axis))
		point.append(self.BoxRefcenter - self.myAxis(0,axis) + self.myAxis(1,axis))
		point.append(self.BoxRefcenter - self.myAxis(0,axis) - self.myAxis(1,axis))
		point.append(self.BoxRefcenter + self.myAxis(0,axis) - self.myAxis(1,axis))
		point.append(self.BoxRefcenter + self.myAxis(0,axis) + self.myAxis(1,axis))

		return point;

	@property
	def density(self):
		return self.data_to_WorldRefcenter.size/self.volume

			#projection_over_Pi = 
			


		

	






