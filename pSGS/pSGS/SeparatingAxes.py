import SeparatingAxes

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

	

		