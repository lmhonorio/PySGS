import numpy as np
import matplotlib.pyplot as plt
import OrientedBoundHyperBox
import DataManagement
import DataModel
import Projections

class clsPrint(object):
	"""description of class"""
	def __init__(self):
		pass

	@staticmethod
	def print2dModel(OBHB):
		plotColor = ['r', 'g', 'y', 'c', 'm', 'b', 'k']
		plotStyle = ['o', '*', 'h', 's', 'd'] 
		plotRepo = [ x+y for x in plotColor for y in plotStyle]

		box = [iobb.returnBox()	 for iobb in OBHB]

		for i in range(len(box)):
			plt.plot(OBHB[i].data[:,0],OBHB[i].data[:,1],plotRepo[i])
			plt.plot(box[i][:,0],box[i][:,1],plotColor[i]+'-')


		
		plt.axis('equal')

		plt.show()