from Roads import Road

class LaneManager:
    def __init__(self):
        self.roads = {
            "A": Road("A"),
            "B": Road("B"),
            "C": Road("C"),
            "D": Road("D")
        }

    def enqueue(self,road,lane,vehicle):
        if road in self.roads:
            self.roads[road].enqueue(lane,vehicle)

    def dequeue(self,road,lane) :
        self.roads[road].dequeue(lane)

    def size(self,road,lane):
        if road in self.roads :
            return self.roads[road].size(lane)
        return 0

    def get_vehicles(self,road):
        if road in self.roads:
            return self.roads[road].size(2)
        return 0






