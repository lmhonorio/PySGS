import numpy as np
import DataModel
import random


class clsDataIO(object):
	"""clsDataIO

The clsDataIO encapsulates functions to read data from files. 
It also implements several well-know test functions such as the checkerboard and banana function

Examples:
    obj = ImageTest.clsImage(<filename>)
    tuple = obj.imageShape

Attributes:
    imagemName:
    imagem:
    
Properties:
Author:
    (LEO) Leonardo de Mello Honorio 

Last Modified:
    (LEO) : 18/01/2016

Version:
    v0.1


COMMONLY USED COMMANDS
		np.array
		np.matrix
		np.column_stack
		random


"""



	def __init__(self, *args):
		if len(args) == 1:
			pass


#a n-dimentional array where columns are features and lines new instances

	def initCheckerBoardFunction(self, Ndata : int, nx : int, ny : int, delta : float):
		"""initCheckerBoardFunction

	Generates two classes similar to a chekerBoard table. One classe would be in the same position 
	as the black part of the board and the second in the white one

	Parameters:
	INPUT:
		Ndata: number of instance of each quadrant
		nx: number of quadrants in x
		ny: number of quadrants in y
		delta: scramble factor, a lower delta means more entangled classes
	OUTPUT:
		cls1, cls2 : objects from classData with encapsulates all data from a given sub-class.

	Example:
		import LoadData
		import matplotlib.pyplot as plt
		myData = LoadData.clsWorkingData()
		cls1, cls2 = myData.initCheckerBoardFunction(50,2,2,0.5)
		plt.plot(cls1.data[:,0],cls1.data[:,1],'g*')
		plt.plot(cls2.data[:,0],cls2.data[:,1],'rd'),
		plt.show()

	Modified:
		(LEO) : 17/01/2016

	Version:
		v0.1

"""

		cls1 = DataModel.clsData(1,1,0)
		cls2 = DataModel.clsData(0,1,0)
		data1 = []
		data2 = []
		i1 = 0
		i2 = 0

		for k in range(0,Ndata):
			for i in range(0,nx):
				for j in range(0,ny):
					if divmod(i+j,2)[1]==1:
						dx = - delta + 2.0 * delta * random.random()
						dy = - delta + 2 * delta * random.random()
						data1.append([i + dx, j + dy])
						i1 += 1
					else:
						dx = - delta + 2.0 * delta * random.random()
						dy = - delta + 2.0 * delta * random.random()
						data2.append([i + dx, j + dy])
						i2 += 1

		data1 = np.matrix(data1)
		data2 = np.matrix(data2)

		cls1.setData(data1)
		cls2.setData(data2)

		return cls1, cls2


	def returnBananaDataset(self, N: (int, int) , p:(float,float), r : float, s : float):
		"""initCheckerBoardFunction

	Generates two classes similar to two bananas - semi-circle classes. One classe is mirrowed and shifted related to another.

	Parameters:
	INPUT:
		N: (int,int) tuple, indicating the number of instances of each class
		p: (float,float) a tuple responsible for shifting the center of each class
		r: the ray of the "bananas"
		s: scramble factor, a higher s means more entangled classes
	OUTPUT:
		cls1, cls2 : objects from classData with encapsulates all data from a given sub-class.

	Example:
		import LoadData
		import matplotlib.pyplot as plt
		myData = LoadData.clsWorkingData()
		cls1, cls2 = myData.returnBananaDataset((200,200), (1.0,1.0), 1.7, 0.2)
		plt.plot(cls1.data[:,0],cls1.data[:,1],'g*')
		plt.plot(cls2.data[:,0],cls2.data[:,1],'rd'),
		plt.show()

	Modified:
		(LEO) : 17/01/2016

	Version:
		v0.1

"""
		cls1 = DataModel.clsData(1,1,0)
		cls2 = DataModel.clsData(0,1,0)

		
		domaina = np.array(0.125*np.pi + np.random.rand(N[0],1)*1.25*np.pi)
		data1 = np.matrix(np.column_stack((r*np.sin(domaina),r*np.cos(domaina)))) + np.matrix(np.random.rand(N[0],2))
		cls1.setData(data1)

		domainb = np.array(0.375*np.pi - np.random.rand(N[0],1)*1.25*np.pi)
		data2 = np.matrix(np.column_stack((r*np.sin(domainb) - p[0],r*np.cos(domainb)- p[1]))) + np.matrix(np.random.rand(N[0],2))
		cls2.setData(data2)

		return cls1,cls2


	def returnLineSegmentDataset(self, p:(float,float), r : float):
		"""initCheckerBoardFunction


		v0.1

"""
		cls1 = DataModel.clsData(1,1,0)
		cls2 = DataModel.clsData(0,1,0)

		
		x = np.array(np.arange(p[0],p[1],r)).transpose()
		n = x.shape[0]
		y = np.array(x) + np.random.rand(1,n)*r
		data = np.vstack((x,y))

		cls1.setData(data.transpose())

		return cls1


	def returnPointsDataset(self):
		"""initCheckerBoardFunction


		v0.1

"""
		cls1 = DataModel.clsData(1,1,0)
		cls2 = DataModel.clsData(0,1,0)

		px = [-2.,-2.,2.,2.]
		py = [-2.,2.,-2.,2.]
		
		x = np.array(px).transpose()
		n = x.shape[0]
		y = np.array(py).transpose()
		data = np.vstack((x,y))

		cls1.setData(data.transpose())

		return cls1,cls1






