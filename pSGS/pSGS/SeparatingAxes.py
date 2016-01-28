import SeparatingAxes
import OrientedBoundHyperBox

import numpy as np



class clsSeparatingAxis(object):
	"""clsSeparatingAxis

		The clsSeparatingAxes is mostly a strycture that stores the values of tested axes that separates two hyperboxes

		Examples:
			<to do>

		Attributes:
			n_pi : the id of the separating axis
			id_hb_1 : identification of the first hyperbox that is separated by axes(n_pi)
			id_hb_1 : identification of the second hyperbox
			separating_distance: if positive, there is no collision happening and the value is the size of the projective 
					distance over axes(n_pi)
			centers_distance: distance of the centers of hyperbox_1 and hyperbox_2 over projection axis n_pi
    
		Properties:
			none

		Author:
			(LEO) Leonardo de Mello Honorio 

		Last Modified:
			(LEO) : 25/01/2016

		Version:
			v0.1
	 """


	def __init__(self, n_pi:int, id_hb_1:int, id_hb_2:int, separating_distance:float, centers_distance:float ):
		"""
		@n_pi:int
	@id_hb_1: int
	@id_hb_2: int
	@separating_distance: float
	@centers_distance: float
		"""
		self.n_pi = n_pi
		self.id_hb_1 = id_hb_1 
		self.id_hb_2 = id_hb_2
		self.separating_distance = separating_distance
		self.centers_distance = centers_distance



class clsSeparatingAxesList(object):
	"""clsSeparatingAxesList

		The clsSeparatingAxesList is just a list to store clsSeparatingAxes component

		Examples:
			<to do>

		Attributes:
			<>
    
		Properties:
			none

		Author:
			(LEO) Leonardo de Mello Honorio 

		Last Modified:
			(LEO) : 25/01/2016

		Version:
			v0.1
	 """

	def __init__(self):

		self.separatin_axes = []



	def addAxis(self, n_pi=0, id_hb_1=0, id_hb_2=0, separating_distance=0.0, centers_distance=0.0, separatin_axis = None ):
		"""
		@n_pi: int
		@id_hb_1: int
		@id_hb_2: int
		@separating_distance: float
		@centers_distance: float
		"""
		if separatin_axis == None:
			new_axis = SeparatingAxes.clsSeparatingAxis(n_pi, id_hb_1, id_hb_2, separating_distance, centers_distance)
			self.separatin_axes.append(new_axis)
		else:
			self.separatin_axes.append(separatin_axis)


	def clearAxes(self):
		self.separatin_axes.clear()


class clsCollisionTest(object):
	
	def __init__(self):
		pass

	
	@staticmethod
	def CollisionTest(obhb_1, obhb_2, rec):
		"""
		@obhb_1: clsOBHB
		@obhb_2: clsOBHB
		@rec: bool
		returns an int
		"""
		separating_axes = SeparatingAxes.clsSeparatingAxesList()
		 
		vCenter = obhb_1.word_ref_center - obhb_2.word_ref_center
		Axes = []
		has_collision = 1
		MtrCol = []
		Dcenter = []
		dcol = []
		M12 = 0;
		M21 = 0;
		#for the two OBHBs
		for i in range(0,obhb_1.dimension):
			Dcenter.append(np.dot(vCenter,obhb_1.projections.pi[i,:])/np.linalg.norm(obhb_1.projections.pi[i,:]))
			
			#for each dimension
			#projection at each
			sum_projection_over_pi = 0
			for j in range(0,obhb_1.dimension):
				sum_projection_over_pi += abs(np.dot(obhb_1.projections.pi[i,:],obhb_2.projections.axes[j])/np.linalg.norm(obhb_1.projections.pi[i,:]))


			dcol.append(abs(Dcenter[i]) - abs(sum_projection_over_pi) - abs(obhb_1.projections.delta_lambda[i]))
			M12 = abs(min(dcol[i],0))
			MtrCol.append(M12)
			if (dcol[i] > 0):
				has_collision = 0
				separating_axes.addAxis(i,obhb_1.set_id, obhb_2.set_id, dcol[i], np.sign(Dcenter[i]))

		if rec == True:
			has_collision_2, rAxis , M21 = SeparatingAxes.clsCollisionTest.CollisionTest(obhb_2,obhb_1,False) # obhb_2.testCollision(obhb_1,False)
			for individual_axis in rAxis.separatin_axes:
				separating_axes.addAxis(separatin_axis = individual_axis)
			has_collision = min(has_collision, has_collision_2)
			MtrCol.append(M21[0])


		return has_collision, separating_axes, MtrCol 



	@staticmethod
	def TestAllAgainstAll(obhbs):
		"""
		@obhbs:OrientedBoundHyperBox.clsListofOBHB
		@obhb_2: clsOBHB
		@rec: bool
		returns a tuple (has_collision, separating_axes, MtrCol)
		"""
		has_collision = 1
		separating_axes = SeparatingAxes.clsSeparatingAxesList()
		MtrCol = []

		isize = len(obhbs.obhbs)
		
		for i in range(0,isize):
			for j in range(i+1,isize):
				if obhbs[i].set_id != obhbs[j].set_id:

					has_collision_2, rAxis , M21 = SeparatingAxes.clsCollisionTest.CollisionTest(obhbs[i],obhbs[j],True)

					for individual_axis in rAxis.separatin_axes:
						separating_axes.addAxis(separatin_axis = individual_axis)
						has_collision = min(has_collision, has_collision_2)
						MtrCol.append(M21[0])




		return has_collision, separating_axes, MtrCol 