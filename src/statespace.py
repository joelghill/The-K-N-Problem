# Joel Hill
# jgh719
# 10344729

import networkx as nx

class StateSpace(object):

	size 		= 50
	vehicles 	= []
	packages 	= []
	garage		= None

	space 		= None

	"""
	Contains vehicles, graph, packages
	N: Number of vehicles. 1 by default
	K: Number of packages
	M: size of map
	"""
	def __init__(self, N = 1, K = 1, M = None):
		super(StateSpace, self).__init__()

		#set size of map
		if(M != None): self.size = M

		self.space 	  = self.generateSpace(self.size)
		self.vehicles = self.generateVehicles(N)
		self.packages = self.generatePackages(K)


	def generateSpace(self, n):
		""" return graph of n size"""
		return nx.grid_2d_graph(4, 4, periodic=True, create_using=None)

	def generateVehicles(self, number):
		vehicles = []
		"""TODO"""
		return vehicles

	def generatePackages(self, number):
		packages = []
		"""TODO"""
		return packages

	def unit_test(self):
		print "test"
		return

test_space = StateSpace()
test_space.unit_test()




