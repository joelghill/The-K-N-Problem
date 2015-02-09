#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Joel Hill
# jgh719
# 10344729


import statespace as S
import Queue
import state


class Search(object):
    StateSpace = None
    vehicle_priority_q = None
    active_vehicles = []
    current_state = None
    original_package_list = []

    """docstring for Search
    N: Number of vehicles.
    K: Number of packages
    H: Height of map
    W: Width of map
    """

    def __init__(self, K, N, H, W, list=None):
        super(Search, self).__init__()
        # initialize state space
        #print "List is:  " + list
        self.StateSpace = S.StateSpace(K, N, H, W, list)
        self.original_package_list = self.package_list()
        self.vehicle_priority_q = Queue.PriorityQueue(maxsize=0)
        self.populate_v_q()
        self.current_state = state.State(self.StateSpace.vehicles, self.StateSpace.packages, self.StateSpace)

        #get inactive vehicle and give package
        v = self.current_state.inactive_vehicles.get()
        self.current_state.active_vehicles.append(v)
        self.current_state.deliver_packages()
        #self.set_initial_fleet()

    def new_vehicle_priority(self, package):
        """
        Priority to sort pickup locations
        :param package: package to pick up
        :return: difference in distances between the pickup and garage, or pickup and nearest other dropoff
        """
        #case for only one package
        if len(self.StateSpace.packages) == 1:
            return -1
        close_drop_dist = self.StateSpace.closest_dropoff(package)[0]
        garage_dist = len(self.StateSpace.shortest_path(self.StateSpace.garage, package.pickup))
        return  close_drop_dist - garage_dist

    def populate_v_q(self):
        for package in self.StateSpace.packages:
            self.vehicle_priority_q.put_nowait((self.new_vehicle_priority(package), package))

    def set_initial_fleet(self):
        """
        Method to initialize a set of vehicles for initial state.
        If there is more than one vehicle, and there is a package where
        the garage is closer than the nearest other dropoff,
        then it is optimal to start a route with that package.
        :return:
        """
        #print 'setting initial fleet'
        if len(self.StateSpace.vehicles) == 1:
            v = self.current_state.inactive_vehicles.get()
            self.current_state.active_vehicles.append(v)
            return

        while (self.current_state.inactive_vehicles.qsize() > 1
               and not self.vehicle_priority_q.empty()):
            p = self.vehicle_priority_q.get()
            #if the priority is above 0, then it is not optimal to deploy vehicle on start
            if p[0] >= 0:
                break
            else:
                v = self.current_state.inactive_vehicles.get()
                v.package = p[1]
                self.current_state.active_vehicles.append(v)
                self.current_state.pending_deliveries.put(v)

        #grab last inactive vehicle and make active
        v = self.current_state.inactive_vehicles.get()
        self.current_state.active_vehicles.append(v)
        self.current_state.deliver_packages()
        return

    def solve(self):
        while not self.current_state.finished():
            self.current_state.assign_next_package()
            self.current_state.deliver_packages()
            self.current_state.activate_vehicle()
        self.StateSpace.draw_space()
        return self.current_state.total_dist

    def print_current_state(self):
        self.StateSpace.print_status()

    def package_list(self):
        return self.StateSpace.package_list()

    def solution(self):
        if self.current_state.finished():
            self.print_current_state()
        else:
            print "No solution yet. use solve()"

test1 = [[7, 78], [74, 71], [52, 53], [85, 47], [9, 74], [68, 28], [35, 35], [23, 81], [78, 92], [18, 70]]

test2 = [[72, 4], [2, 43], [11, 80], [23, 11], [17, 48]]

test3 = [[30, 84], [14, 89], [7, 93], [52, 66], [12, 45]]

Simple = [[83, 84], [5, 65]]

Simple2 = [[90, 91], [26, 29]]

#20 packages
largetest = [[7091, 7142], [1749, 70], [7377, 8915], [9728, 4863], [2730, 9624], [6794, 193], [825, 9058],
             [850, 5905], [4453, 9832], [1632, 2620], [2476, 987], [2824, 4709], [2614, 8170], [4676, 8712],
             [9715, 258], [2907, 9347], [7883, 1033], [3554, 1468], [5876, 7044], [5916, 2127]]

#max 3 vehicles used
largetestlist2 = \
    [[7337, 9779], [3523, 481], [7051, 2265], [2291, 2881], [1624, 8721], [1581, 3699], [3950, 1277],
     [3620, 97], [3002, 8282], [6036, 1796], [2142, 6060], [3935, 500], [5463, 7449], [8510, 8159],
     [7988, 2904], [2108, 7920], [5456, 9253], [4186, 765], [370, 9154], [3972, 471]]



test = Search(2, 2, 10, 10, Simple2)
#test = Search(5, 1, 10, 10, list([[60, 90], [41, 77], [40, 41], [90, 87], [37, 78]]))
#test2 = Search(5, 1, 10, 10, list(list1))
#print "Test Space Status"
#print test.StateSpace.print_status()
#print "Printing PQ:  "
#print test.current_state
#print "Test package:  " + str(test.current_state.packages[0])
print "Package List:  "
print test.original_package_list
dist1 = test.solve()
#dist2 = test2.solve()

test.solution()

print "Total distance:  " + str(dist1) + "\n"
#print "Total distance with 1 vehicles:  " + str(dist2) + "\n"

