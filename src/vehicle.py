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

	def __str__(self):
		iden	 = "ID:  " + str(id(self))
		location = "Location:  "+ str(self.location)
		package	 = "Package:  " + str(self.package)
		return iden + "\n" + location + "\n" + package + "\n"

