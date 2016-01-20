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
	def print2dmodel(OBHB):
		plot_color = ['r', 'g', 'y', 'c', 'm', 'b', 'k']
		plot_style = ['o', '*', 'h', 's', 'd'] 
		plot_repo = [ x+y for x in plot_color for y in plot_style]

		box = [iobb.returnBox()	 for iobb in OBHB]

		for i in range(len(box)):
			plt.plot(OBHB[i].data[:,0],OBHB[i].data[:,1],plot_repo[i])
			plt.plot(box[i][:,0],box[i][:,1],plotColor[i]+'-')


		
		plt.axis('equal')

		plt.show()