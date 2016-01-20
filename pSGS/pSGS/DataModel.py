import numpy as np

class clsData(object):
	"""description of class"""


	def __init__(self, set_id = 0, incollision = 0, breaks = 0, data = []):
		self.set_id =set_id
		self.in_collision = incollision
		self.breaks = breaks
		self.data =  np.array(data)
		self.xmean = np.array(0)
		self.word_ref_center = np.array(0)
		self.cov = np.array(0)
		self.pi = np.array(0)
		self.Lambda = np.array(0)

		self.setData(data)

			

	def setData(self, data = []):
		if len(data) != 0:
			self.data = np.array(data)
		if self.data.size > 0:
			self.cov = np.cov(self.data.transpose())
			w, v = np.linalg.eig(self.cov)
			self.pi = v
			self.Lambda = w
			self.xmean = self.data.mean(0)
			min = self.data.min(0)
			max = self.data.max(0)
			self.word_ref_center = (max + min)/2.0



	def AddItem(self, item):
		if self.data is None:
			self.data = np.array(item) 
		else:
			newitem = np.array(item)
			lenshape =  len(self.data.shape)
			if newitem.shape == self.data.shape[1:lenshape]:
				self.data = np.vstack((self.data,newitem))
			else:
				print('not possible to concatenate, vector with different size')




	@property
	def datalen(self):
		return len(self.data)

	@property
	def dimension(self):
		return self.data.shape[1]
		
