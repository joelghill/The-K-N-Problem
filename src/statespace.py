#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Joel Hill
# jgh719
# 10344729

import math
import Queue
import networkx as nx
import vehicle as Vcl
import package as Pkg
import matplotlib.pyplot as plt
import matplotlib as mat


class StateSpace(object):
    # Number of nodes in graph. Default is 20
    size = 20
    vehicles = None
    packages = None
    dropoffs = []
    pickups = []
    garage = None
    positions = {}

    deliveries = []

    space = None

    """
	Contains vehicles, graph, packages
	N: Number of vehicles.
	K: Number of packages
	M: size of map
	"""

    def __init__(self, K=1, N=1, Height=5, Width=5, packages=None):
        super(StateSpace, self).__init__()

        mat.rc("font", family="Arial")
        # set size of map
        self.size = Height * Width

        self.space = self.generateSpace(Height, Width)
        self.generate_garage()
        self.generate_vehicles(N)
        self.generate_packages(K, packages)

    def generateSpace(self, n, m):
        """ return graph of n * m  size"""
        g = nx.grid_2d_graph(n, m, periodic=False, create_using=None)
        self.map_positions(n, m)
        return nx.convert_node_labels_to_integers(g)

    def generate_vehicles(self, number):
        self.vehicles = [Vcl.Vehicle(self.garage) for i in range(number)]

    def generate_packages(self, number, packages=None):
        # give pack package a name and add dropoff to list
        # if list was given, use that
        if packages is not None:
            self.packages = [Pkg.Package() for i in range(len(packages))]
            for package in self.packages:
                newpos = packages.pop()
                package.pickup = newpos[0]
                package.dropoff = newpos[1]
        else:
            #don't fully get python yet....
            self.packages = [Pkg.Package(self.size) for i in range(number)]
        for p in range(len(self.packages)):
            self.packages[p].name = str(p)
            self.dropoffs.append(self.packages[p].dropoff)
            self.pickups.append(self.packages[p].pickup)

    def generate_garage(self):
        self.garage = 0
        return

    def print_status(self):
        print("Graph info:")
        print(nx.info(self.space))
        print("")
        print("Vehicles generated:")
        print("Total:  " + str(len(self.vehicles)))

        for Vcl.Vehicle in self.vehicles:
            print(Vcl.Vehicle)

    def draw_space(self):
        nx.draw_networkx_nodes(self.space, pos=self.positions)

        # add labels
        for delivered in self.deliveries:
            plt.annotate("P" + str(delivered.name), xy=(self.positions[delivered.pickup]))
            plt.annotate("D" + str(delivered.name), xy=(self.positions[delivered.dropoff]))
            plt.annotate("G", xy=(self.positions[self.garage]))

        plt.savefig("output.png")  # save as png

    def map_positions(self, M, N):
        key = 0
        for i in range(0, M):
            for j in range(0, N):
                self.positions[key] = (i, j)
                key += 1

    def distance(self, point1, point2):
        """Given two nodes in the map, calculate the distance"""
        pos1 = self.positions[point1]
        pos2 = self.positions[point2]
        dist_tup = (pos1[0] - pos2[0], pos1[1] - pos2[1])
        dist = math.sqrt((dist_tup[0] ** 2) + (dist_tup[1] ** 2))
        return dist

    def valid_dropoff(self, node):
        if node in self.dropoffs:
            return True
        else:
            return False

    def valid_pickup(self, node):
        return node in self.pickups

    def closest_dropoff(self, package):
        """
        Finds closest dropoff point from package pickup
        TODO: Similar but different to closest_pickup - confusing difference in interface
        :param package: package with pickup location
        :return: (distance to nearest dropoff, dropoff node)
        """
        # print "Finding closest dropoff to " + str(node1)
        pickup = package.pickup
        own_drop = package.dropoff
        # priority Q for closest DO
        pq = Queue.PriorityQueue(maxsize=0)
        for item in self.dropoffs:
            if item is not own_drop:
                pq.put((self.distance(pickup, item), item))
        return pq.get()

    def closest_pickup(self, position):
        """
        Finds nearest pickup position from given position
        :param position:
        :return: (distance to pickup, pickup)
        """
        # print "closest pickup called"
        pq = Queue.PriorityQueue(maxsize=0)
        # add all packages in priority q based on distance from position
        for packages in self.pickups:
            #print "putting in q...."
            pq.put((self.distance(position, packages), packages))
        #return top of priority q
        return pq.get()

    def package_list(self):
        """
        Returns a list representation of the packages in the style [[pickup, dropoff], ...]
        :return: package_list[]
        """
        package_list = []
        for package in self.packages:
            package_list.append(package.data())
        return package_list





