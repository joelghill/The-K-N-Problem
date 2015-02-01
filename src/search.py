#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Joel Hill
# jgh719
# 10344729


import statespace as S
import Queue


class Search(object):
    StateSpace = None
    vehicle_priority_q = None
    active_vehicles = []

    """docstring for Search
    N: Number of vehicles.
    K: Number of packages
    H: Height of map
    W: Width of map
    """

    def __init__(self, K, N, H, W):
        super(Search, self).__init__()
        # initialize state space
        self.StateSpace = S.StateSpace(K, N, H, W)
        self.vehicle_priority_q = Queue.PriorityQueue(maxsize=0)
        self.populate_v_q()

    def new_vehicle_priority(self, package):
        """
        Priority to sort pickup locations
        :param package: package to pick up
        :return: difference in distances between the pickup and garage, or pickup and nearest other dropoff
        """
        close_drop_dist = self.StateSpace.closest_dropoff(package)[0]
        garage_dist = len(self.StateSpace.shortest_path(self.StateSpace.garage, package.pickup))
        return garage_dist - close_drop_dist

    def populate_v_q(self):
        for package in self.StateSpace.packages:
            self.vehicle_priority_q.put_nowait((self.new_vehicle_priority(package), package))

test = Search(5, 2, 5, 5)
print test.StateSpace.print_status()
print test.StateSpace.closest_dropoff(test.StateSpace.packages[0])
print test.vehicle_priority_q.get()[1]
