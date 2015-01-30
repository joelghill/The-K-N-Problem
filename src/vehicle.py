# Joel Hill
# jgh719
# 10344729

class Vehicle(object):

	location = None
	package	 = None
	goal	 = None

	"""docstring for Vehicle"""
	def __init__(self, location):
		super(Vehicle, self).__init__()
		self.location = location
