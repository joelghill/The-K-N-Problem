# Joel Hill
# jgh719
# 10344729

import Queue
import statespace


class State(object):
    """
    Class representing a state of search
    """
    vehicles = None
    active_vehicles = None
    inactive_vehicles = None
    state_space = None
    pending_deliveries = None

    # packages awaiting pickup from a truck
    packages = None

    # number of deliveries left
    deliveries = None

    #total distance traveled by all trucks
    total_dist = 0

    def __init__(self, v, p, space):
        super(State, self).__init__()
        self.vehicles = v
        self.active_vehicles = []
        self.inactive_vehicles = Queue.Queue()
        self.pending_deliveries = Queue.Queue()
        #pop all the vehicles into the inactive Q
        for v in self.vehicles:
            self.inactive_vehicles.put(v)
        self.packages = p
        self.deliveries = len(self.packages)
        self.state_space = space

    def complete(self):
        if self.deliveries == 0:
            return True
        else:
            return False

    def make_delivery(self, v):
        """
        Take vehicle with package, move to package location, and update distances driven.
        :param vehicle:
        :return:
        """
        vehicle = v
        if not vehicle.package:
            return
        else:
            dist = (self.state_space.distance(vehicle.location, vehicle.package.pickup)
                    + self.state_space.distance(vehicle.package.pickup, vehicle.package.dropoff))
            vehicle.distance_driven += dist
            self.total_dist += dist
            vehicle.path = list(vehicle.path)
            vehicle.path.append(self.state_space.positions[vehicle.package.pickup])
            vehicle.path.append(self.state_space.positions[vehicle.package.dropoff])
            vehicle.location = vehicle.package.dropoff
            self.state_space.pickups.remove(vehicle.package.pickup)
            self.state_space.dropoffs.remove(vehicle.package.dropoff)
            self.packages.remove(vehicle.package)
            self.state_space.deliveries.append(vehicle.package)
            vehicle.package = None
            self.deliveries -= 1

    def deliver_packages(self):
        while not self.pending_deliveries.empty():
            self.make_delivery(self.pending_deliveries.get())

    def assign_next_package(self):
        pq = Queue.PriorityQueue()
        for packages in self.packages:
            cost_and_vehicle = self.cost_of_package(packages)
            pq.put((cost_and_vehicle[0], (packages, cost_and_vehicle[1])))
        best = pq.get()
        vehicle = best[1][1]
        package = best[1][0]
        vehicle.package = package
        self.pending_deliveries.put(vehicle)
        return

    def closest_active_vehicle(self, position):
        pq = Queue.PriorityQueue(maxsize=0)
        #add all vehicles in priority q based on distance from position
        for vehicles in self.active_vehicles:
            pq.put((self.state_space.distance(position, vehicles.location), vehicles))
        #return top of priority q
        return pq.get()

    def cost_of_package(self, package):
        """
        Cost of package and vehicle associated with cost
        :param package:
        :return: (cost, vehicle)
        """
        cost = self.state_space.closest_pickup(package.dropoff)[0]
        distance_and_vehicle = self.closest_active_vehicle(package.pickup)
        #add distance to closest vehicle to cost
        cost += distance_and_vehicle[0]
        return cost, distance_and_vehicle[1]

    def finished(self):
        return self.deliveries == 0

    def __str__(self):
        string = "Deliveries left:  " + str(self.deliveries) + "\n"
        string += "Active vehicles:  " + str(len(self.active_vehicles)) + "\n"
        string += "Total distance driven:  " + str(self.total_dist) + "\n"
        string += "Size of packages list in state space:  " + str(len(self.state_space.packages))
        for vehicles in self.active_vehicles:
            string += str(vehicles)
        return string