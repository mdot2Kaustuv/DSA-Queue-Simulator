

class Queues:
    def __init__(self):
        self.queue = []

    def is_empty (self) :
        return len(self.queue) == 0

    def enqueue(self,vehicle):
        self.queue.append(vehicle)

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


