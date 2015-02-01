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
        print "DropOffs:  "
        print self.dropoffs

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

    def expand_node(self, node, queue, visited):
        """
        Method to expand nodes for BFS
        :rtype : None
        :param node: nod to expand
        :param queue: unexpanded nodes
        :param visited: list of visited nodes
        :return:
        """
        neighbours = nx.all_neighbors(self.space, node)
        while True:
            try:
                n = neighbours.next()
                if node not in visited:
                    queue.put(n)
            except StopIteration:
                break
        return

    def visit_node(self, node, visited, visit_function):
        """

        :param node: Node to visit
        :param visited: list of previously visted nodes
        :param visit_function: Function to perform on node
        :return: result of visit_function or None if node visited
        """

        assert isinstance(visited, list)
        visited.append(node)
        return visit_function(node)

    def valid_dropoff(self, node):
        if node in self.dropoffs:
            return True
        else:
            return False
        
    def closest_dropoff(self, package):
        """
        Finds closest dropoff point from node1
        :param node1: node from graph
        :return: distance to nearest dropoff, dropoff node.
        """
        #print "Finding closest dropoff to " + str(node1)
        node1 = package.pickup
        own_drop = package.dropoff
        q = Queue.Queue()
        visited = []
        self.expand_node(node1, q, visited)
        #print "q empty?"
        #print q.empty()
        while not q.empty():
            #print "q not empty"
            #print "Size of q is:  " + str(q.qsize())
            n = q.get()
            #print "Node retrieved: " + str(n)
            if n not in visited:
                self.expand_node(n, q, visited)
                #print "Node not visited yet...."
                if self.visit_node(n, visited, self.valid_dropoff) and n is not own_drop:
                    return len(self.shortest_path(n, node1)), n





