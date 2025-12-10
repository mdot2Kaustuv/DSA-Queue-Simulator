
class Vehicle :
    def __init__ (self,id,lane,time) :
        self.id = id
        self.lane = lane
        self.time = time

    def __str__ (self) :
        return f'{self.id} {self.lane} {self.time}'


class queue :
    def __init__(self):
        self.queue = []

    def is_empty (self) :
        return len(self.queue) == 0

    def enqueue(self,Vehicle):
        self.queue.append(Vehicle )

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

class lane :
    def __init__(self):
        self.lanes ={}
        for k in ["A","B","C","D"]:
            self.lanes[k]= queue()
            self.priority = False


    def enqueue(self,Vehicle,road):
        self.lanes[road].enqueue(Vehicle)

    def dequeue(self,road):
        if self.lanes[road].is_empty() :
            raise KeyError
        self.lanes[road].dequeue()

    def size(self,road):
        return self.lanes[road].size()

    def is_empty(self,road):
        return self.lanes[road].is_empty()

    














