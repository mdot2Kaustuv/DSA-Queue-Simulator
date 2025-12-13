import random
from Vehicles import Vehicle
import time

data_file = "Traffic.data"
LANES = ["1","2","3"]
road = ["A","B","C","D"]

def record (Vehicle) :
    with open(data_file, "a") as file:
        file.write(f"{Vehicle.id},{Vehicle.lane},{Vehicle.road},{Vehicle.time}\n")

def generate_vehicle (delay = 1.0):
    while True :
        vehicle_road = random.choice(road)
        vehicle_lane = random.choice(LANES)
        vehicle_id = random.randint(1,10000)
        interval = random.expovariate(1.0 / delay)
        time.sleep(interval)
        return Vehicle(vehicle_id,vehicle_lane,vehicle_road,time.time())

def generator():
    while True:
        v=generate_vehicle()
        record(v)


generator()





