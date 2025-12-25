from Queues import Queues
class Road:
    def __init__(self,road_id):
        self.road = road_id
        self.lanes = {
            1 : Queues() ,
            2 : Queues(),
            3 : Queues()
        }

    def enqueue(self,lane,vehicle):
        self.lanes[lane].enqueue(vehicle)

    def dequeue(self,lane):
        self.lanes[lane].dequeue()

    def size(self,lane):
        return self.lanes[lane].size()



