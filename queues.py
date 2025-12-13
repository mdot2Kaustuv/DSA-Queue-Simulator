
class queue :
    def __init__(self):
        self.queue = []

    def is_empty (self) :
        return len(self.queue) == 0

    def enqueue(self,Vehicle):
        self.queue.append(Vehicle)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

class LaneStats :
    def __init__(self):
        self.lanes ={}
        for road in ["W","X","Y","Z"]:
            for lane in ["A","B","C"]:
                self.lanes[f"{road}{lane}"]= queue()
        self.priority = False

    def enqueue(self,Vehicle):
        k = f"{Vehicle.road}{Vehicle.lane}"
        self.lanes[k].enqueue(Vehicle)

    def dequeue(self,road,lane):
        key = f"{road}{lane}"
        if self.lanes[key].is_empty():
            return None
        return self.lanes[key].dequeue()

    def size(self,road,lane):
        return self.lanes[f"{road}{lane}"].size()

    def is_empty(self,road,lane):
        return self.lanes[f"{road}{lane}"].is_empty()

