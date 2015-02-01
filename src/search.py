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

    """docstring for Search
	N: Number of vehicles.
	K: Number of packages
	H: Height of map
	W: Width of map 
	"""

    def __init__(self, K, N, H, W):
        super(Search, self).__init__()
        # initialize state space
        self.StateSpace = S.StateSpace(K, K, H, W)
        self.vehicle_priority_q = Queue.PriorityQueue(maxsize=N)


test = Search(1, 2, 5, 5)
test.StateSpace.closest_dropoff(0)

