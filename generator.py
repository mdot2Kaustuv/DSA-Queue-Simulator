import random
from queue import Vehicle
import time


LANES = ["A","B","C","D"]


def generate_vehicle (mean_interval = 2.0):
    while True :
        road = random.choice(LANES)
        vehicle_id = random.randint(1,10000)
        interval = random.expovariate(1.0 / mean_interval)
        time.sleep(interval)

def record_vehicles() :
    pass




