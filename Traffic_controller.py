from Roads import Road
from Lanes import LaneManager
from  Trafficlights import Lights

class TrafficController:
 vehicle_time = 1.5  #Time for a vehicle to pass
 high_priority = 10
 low_priority = 5

def __init__(self) :
    self.lights = {
        "A":Lights() ,
        "B": Lights(),
        "C": Lights()
    }

    self.lane_manager = LaneManager()
    self.priority_mode = False

