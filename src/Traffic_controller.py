

from Roads import Road
from Lanes import LaneManager
from  Trafficlights import TrafficLight
import time

class TrafficController:
    def __init__(self):
        self.roads = ["A", "B", "C", "D"]
        self.t = 2
        self.lm = LaneManager()
        self.lights = {
            "A" : TrafficLight(),
            "B" : TrafficLight(),
            "C" : TrafficLight(),
            "D" : TrafficLight(),

        }
        self.priority_road = "A"
        self.priority_lane =2

    def vehicle_served(self) :
        normal_lanes = ["B", "C", "D"]
        total_vehicles = sum(self.lm.size(road, 2) for road in normal_lanes)
        n = len(normal_lanes)
        if total_vehicles == 0:
            return 0
        average = int (total_vehicles / n)
        return max (1, average)

    def priority(self):
        prioritycount = self.lm.size(self.priority_road, self.priority_lane)
        return prioritycount > 10

    def serve_if_priority(self):
       for road in self.roads :
           if road!=self.priority_road:
               self.lights[road].set_red()

       self.lights[self.priority_road].set_green()

       while self.lm.size(self.priority_road, self.priority_lane) >= 5:
           vehicle_count = self.lm.size(self.priority_road, self.priority_lane)
           self.lm.dequeue(self.priority_road, self.priority_lane)


       self.lights[self.priority_road].set_green()


    def serve_normal(self) :
        normalroads = ["B","C","D"]
        lane = 2

        for road in normalroads:
            vehiclecount = self.vehicle_served()
            vehicle_number = self.lm.size(road,lane)

            if vehicle_number > 0 :
                self.lights[road].set_green()

                for nonactiveroad in self.roads :
                        self.lights[nonactiveroad].set_red()

                green_time = vehiclecount*self.t

                for i in range( vehiclecount):
                    self.lm.dequeue(road, lane)
                    time.sleep(self.t)


                self.lights[road].set_red()




    def run(self):
        cycle = 0

        while True:
            cycle += 1

            if self.priority() :
                self.serve_if_priority()
            else :
                self.serve_normal()
                time.sleep(self.t)



controller = TrafficController()
controller.run()





