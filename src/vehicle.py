# Joel Hill
# jgh719
# 10344729


class Vehicle(object):
    location = None
    package = None
    distance_driven = 0
    path = []

    """docstring for Vehicle"""

    def __init__(self, location):
        super(Vehicle, self).__init__()
        self.location = location
        #self.path.append(location)
        self.path = list([location])

    def __str__(self):
        iden = "ID:  " + str(id(self))
        location = "Location:  " + str(self.location)
        package = "Package:  " + str(self.package)
        dist = "Distance driven:  " + str(self.distance_driven)
        path = "Path taken:  " + str(self.path)
        return iden + "\n" + location + "\n" + package + "\n" + dist + "\n" + path

