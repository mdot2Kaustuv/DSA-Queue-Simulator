class Vehicle :
    def __init__ (self,id,lane,road,time,direction) :
        self.id = id
        self.lane = lane
        self.road = road
        self.time = time
        self.direction = direction


    def __str__(self) :
        return f'{self.id} {self.lane}{self.road} {self.time}'