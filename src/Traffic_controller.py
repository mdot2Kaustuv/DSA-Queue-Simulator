from Trafficlights import TrafficLight
import time

from src.Lanes import LaneManager


class TrafficController:
    def __init__(self, shared_lm):
        self.roads = ["A", "B", "C", "D"]
        self.lm = shared_lm
        self.lights = {
            "A": TrafficLight(),
            "B": TrafficLight(),
            "C": TrafficLight(),
            "D": TrafficLight(),
        }
        self.priority_road = "A"
        self.priority_threshold = 10
        self.priority_min = 5
        self.service_delay = 0.5


    def vehicle_served(self, current_active_road):

        total_waiting = 0
        others_count = 0

        for r in self.roads:
            if r != current_active_road:

                total_waiting += self.lm.size(r, 2)
                others_count += 1

        if others_count == 0:
            return 1

        average = int(total_waiting / others_count)
        return max(1, average)

    def set_active_light(self, active_road):
        for road in self.roads:
            if road == active_road:
                self.lights[road].set_green()
            else:
                self.lights[road].set_red()

    def get_controlled_cars_count(self, road):
        return self.lm.size(road, 2)

    def service_free_lanes(self):
        for road in self.roads:
            if self.lm.size(road, 3) > 0:
                self.lm.dequeue(road, 3)

    def dequeue_controlled_vehicle(self, road):
        # Priority to Lane 2, then Lane 1
        for lane in [2, 1]:
            if self.lm.size(road, lane) > 0:
                self.lm.dequeue(road, lane)
                return True
        return False

    def priority_condition_met(self):
        return self.lm.size(self.priority_road, 2) > self.priority_threshold

    def serve_priority(self):
        print(f"!!! PRIORITY MODE: {self.priority_road} !!!")
        self.set_active_light(self.priority_road)

        # Serve until count drops below 5
        while self.lm.size(self.priority_road, 2) > self.priority_min:
            self.service_free_lanes()

            served = self.dequeue_controlled_vehicle(self.priority_road)
            if served:
                print(f"   -> Priority Vehicle leaving {self.priority_road}")
                time.sleep(self.service_delay)
            else:
                break

    def serve_normal_cycle(self):
        # LOGIC FIX 2: Include ALL roads (A, B, C, D) in normal rotation
        all_roads = ["A", "B", "C", "D"]

        for road in all_roads:
            # Check priority interrupt
            if self.priority_condition_met():
                return

            vehicle_count = self.get_controlled_cars_count(road)

            if vehicle_count > 0:
                self.set_active_light(road)
                calculated_limit = self.vehicle_served(road)
                cars_to_serve = min(vehicle_count, calculated_limit)


                for _ in range(cars_to_serve):
                    self.service_free_lanes()

                    served = self.dequeue_controlled_vehicle(road)
                    if served:
                        print(f"   -> Vehicle leaving {road}")
                        time.sleep(self.service_delay)

    def run(self):
        print("Traffic Controller Started.")
        while True:
            self.service_free_lanes()

            if self.priority_condition_met():
                self.serve_priority()
            else:
                self.serve_normal_cycle()

            time.sleep(0.1)

if __name__ == "__main__":
    lm = LaneManager()
    traffic_controller = TrafficController(lm)
    traffic_controller.run()