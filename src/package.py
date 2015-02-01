# Joel Hill
# jgh719
# 10344729

# Class to represent package
import random
import networkx as nx
import matplotlib.pyplot as plt


class Package(object):
    name = None
    dropoff = None
    pickup = None
    delivered = False

    """Package contains a pickup and dropoff location"""

    def __init__(self, size):
        super(Package, self).__init__()
        self.dropoff = random.randint(1, size)
        self.pickup = random.randint(1, size)

    def __str__(self):
        iden = "ID:  " + str(id(self))
        name = "Name:  " + self.name
        drop = "DropOff Node:  " + str(self.dropoff)
        pick = "Pickup Location:  " + str(self.pickup)
        d = "Delivered:  " + str(self.delivered)
        return iden + "\n" + name + "\n" + drop + "\n" + pick + "\n" + d + "\n"
