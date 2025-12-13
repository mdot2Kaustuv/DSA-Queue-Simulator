class Vehicle :
    def __init__ (self,id,lane,road,time) :
        self.id = id
        self.lane = lane
        self.road = road
        self.time = time

    def __str__(self) :
        return f'{self.id} {self.lane}{self.road} {self.time}'