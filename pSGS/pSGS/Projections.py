import DataModel
import numpy as np

class clsProjectionOverAxis(object):
	"""description of class"""

	def __init__(self, data :np.ndarray , world_ref_center:np.ndarray ):
		self.data_to_world_ref_center = data - world_ref_center
		self.projection_over_pi = []
		self.min = []
		self.max = []
		self.delta_lambda = []
		self.volume = 1.0
		self.box_ref_center = []
		self.dimension = data.shape[1]
		self.cov = np.cov(data.transpose())
		w, v = np.linalg.eig(self.cov)
		self.pi = v
		self.Lambda = w
		self.mod_pi = [np.linalg.norm(pi) for pi in self.cov]

		for i in range(0,self.dimension):
			projection_over_pi = np.array(np.dot(self.data_to_world_ref_center, self.pi[i,:]) / self.mod_pi[i])
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
		self.box_ref_center = world_ref_center + 0.5 * np.dot(self.cov.transpose(),np.array(self.min) + np.array(self.max))


	def improveDataFitness(self):
		i = 1
		pass
	

	def myAxis(self, i:int):
		return  self.delta_lambda[i] * self.pi[i,:]


	def returnOrientedBoundingBox(self):
		point = []
		point.append(self.box_ref_center + self.myAxis(0) + self.myAxis(1))
		point.append(self.box_ref_center - self.myAxis(0) + self.myAxis(1))
		point.append(self.box_ref_center - self.myAxis(0) - self.myAxis(1))
		point.append(self.box_ref_center + self.myAxis(0) - self.myAxis(1))
		point.append(self.box_ref_center + self.myAxis(0) + self.myAxis(1))

		return point;

	@property
	def density(self):
		return self.data_to_world_ref_center.size/self.volume

			#projection_over_Pi = 
			


		

	






