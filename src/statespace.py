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
    garage = None
    positions = {}

    space = None

    """
	Contains vehicles, graph, packages
	N: Number of vehicles.
	K: Number of packages
	M: size of map
	"""

    def __init__(self, K=1, N=1, Height=5, Width=5):
        super(StateSpace, self).__init__()

        mat.rc("font", family="Arial")
        # set size of map
        self.size = Height * Width

        self.space = self.generateSpace(Height, Width)
        self.generate_garage()
        self.generate_vehicles(N)
        self.generate_packages(K)


    def generateSpace(self, n, m):
        """ return graph of n size"""
        g = nx.grid_2d_graph(n, m, periodic=False, create_using=None)
        self.map_positions(n, m)
        return nx.convert_node_labels_to_integers(g)


    def generate_vehicles(self, number):
        self.vehicles = [Vcl.Vehicle(self.garage) for i in range(number)]


    def generate_packages(self, number):
        self.packages = [Pkg.Package(self.size) for i in range(number)]
        # give eack package a name and add dropoff to list
        for p in range(len(self.packages)):
            self.packages[p].name = str(p)
            self.dropoffs.append(self.packages[p].dropoff)


    def generate_garage(self):
        self.garage = 0
        return

    def unit_test(self):
        self.draw_space()
        self.print_status()
        self.distance(0, 1)
        return

    def print_status(self):
        print("Graph info:")
        print(nx.info(self.space))
        print("")
        print("Vehicles generated:")
        print("Total:  " + str(len(self.vehicles)))

        for Vcl.Vehicle in self.vehicles:
            print(Vcl.Vehicle)

        print("Packages:")
        for Pkg.Package in self.packages:
            print(Pkg.Package)
            print("")

        print("Nodes: ")
        print(nx.nodes(self.space))

    def draw_space(self):
        self.relable()
        # nx.draw(self.space)
        nx.draw_networkx(self.space, pos=self.positions)
        # nx.draw_networkx(self.space)

        # add labels
        # for node in nx.nodes(self.space):
        # plt.annotate(u"n", xy=(1,1))

        #plt.annotate("annotate", xy=(1, 1))

        #plt.xlabel("X Axis")
        plt.savefig("output.png")  # save as png
        #plt.show()  # display

    def relable(self):
        # mapping = {1:"G"}
        # self.space = nx.relabel_nodes(self.space, mapping, False)
        return

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

    def shortest_path(self, point1, point2):
        """ Use A* to calculate shortest path between nodes """
        return nx.astar_path(self.space, point1, point2, heuristic=self.distance)

    def closest_dropoff(self, node1):
        Q = Queue.Queue()
        dist = 1
        visited = [node1]
        neighbours = nx.all_neighbors(self.space, node1)
        print(neighbours)
        while True:
            try:
                node = neighbours.Next()
                if node in self.dropoffs and node not in visited:
                    return dist, node
                else:
                    if node not in visited:
                        Q.put(node)
            except StopIteration:
                break

                # for node in neighbours:
                # 4if node






