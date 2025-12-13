from Queues import Queues
from Vehicles import Vehicle
from Roads import Road

class LaneManager:
    def __init__(self, lane_number):
        self.roads = {
            "A": Road("A"),
            "B": Road("B"),
            "C": Road("C"),
            "D": Road("D")
        }

    def enqueue(self,road,lane,vehicle):
        self.roads[road].enqueue(lane,vehicle)

    def dequeue(self,road,lane,vehicle):
        self.roads[road].dequeue(lane,vehicle)

    def size(self,road,lane):
        return self.roads[road].size(lane)


