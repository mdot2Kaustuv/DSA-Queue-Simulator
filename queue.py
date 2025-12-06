from collections import deque
from dataclasses import dataclass

@dataclass
class Vehicle :
    id : int
    time : float
    lane : str


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


