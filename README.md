# Traffic Management System using Queue Data Structure

## Assignment Details

**Name**: Kaustuv Bhandari  
**Roll Number**: 11  
**Course**: COMP202 - Data Structures and Algorithms  
**Submitted to**: Rupak Ghimire  
**Date**: 2025-12-27

---

## Table of Contents

- [What is This Project?](#what-is-this-project)
- [Output Demo](#output-demo)
- [Why This Project?](#why-this-project)
- [Main Features](#main-features)
- [How Does It Work?](#how-does-it-work)
- [DSA Concepts Used](#dsa-concepts-used)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Files](#project-files)
- [Understanding the Code](#understanding-the-code)
---

## What is This Project?

This is a **4-way traffic intersection simulator** built with Python and Pygame. It shows how **Queue data structure** works in real life!

Instead of using fixed timers like normal traffic lights, this project uses **Queue logic** and **Priority Queue** to control traffic flow. When Road A (north side) gets too crowded (more than 10 cars), the system gives it priority until it clears up.

**Real-world use**: This is how modern smart traffic lights work in big cities!

---
## Simulator Demo

+[Simulator Demo] (https://raw

.githubusercontent.com/mdot2Kaustuv/DSA

-Queue-Simulator/main/Simulator.mp4

)


The simulation shows:
- 4 roads (A, B, C, D) meeting at an intersection
- Cars moving and stopping at red lights
- Traffic lights changing based on queue size
- Priority mode activating when Road A gets crowded

---

## Why This Project?

As a DSA student, we learn about **Queues** in theory. But where do we actually use them? This project answers that!

### Learning Goals:
1. Understand how Queue data structure works practically
2. Learn about FIFO (First In First Out) operations
3. See how Priority Queue makes decisions
4. Practice multi-threading in Python
5. Build something visual and interesting!

---

## Main Features

### 1. Smart Priority System
- Normal mode: All roads get turns equally (round-robin)
- Priority mode: Road A gets priority when it has 10+ vehicles
- Priority keeps serving until only 5 vehicles remain
- Then goes back to normal mode

### 2. Realistic Traffic
- Vehicles arrive randomly (like real traffic)
- Cars maintain safe distance from each other
- Red light = Stop, Green light = Go
- No crashes or overlapping

### 3. Visual Simulation
- Built with Pygame library
- Different colored cars for easy tracking
- Real-time traffic light indicators
- Smooth 60 FPS animation

### 4. Left-Hand Traffic (LHT)
- Follows Nepal/UK driving rules
- Lane 1 is the controlled lane
- Lane 2 is the additional lane

### 5. Data Recording
- Every vehicle is logged in `Traffic.data` file
- Format: `VehicleID, Lane, Road, Timestamp`
- Can be used for analysis later

---

## How Does It Work?

### Simple Explanation:

```
Step 1: Generator creates vehicles randomly
         ↓
Step 2: Vehicles join queues (one queue per lane)
         ↓
Step 3: Traffic Controller checks queue sizes
         ↓
Step 4: If Road A > 10 cars → Priority Mode
        Otherwise → Normal Round-Robin
         ↓
Step 5: Green light for selected road
         ↓
Step 6: Vehicles leave queue (dequeue) and cross
         ↓
Step 7: Repeat!
```

### Producer-Consumer Pattern:

**Producer** (Generator.py):
- Creates vehicles continuously
- Adds them to queues (enqueue operation)

**Consumer** (Traffic_controller.py):
- Removes vehicles from queues (dequeue operation)
- Controls when vehicles can cross

**Visualizer** (Simulator.py):
- Shows everything on screen
- Makes it look realistic

---

## DSA Concepts Used

### 1. Queue (Main Data Structure)

```
Queue = First In, First Out (FIFO)

Example:
Car 1 arrives → [Car1]
Car 2 arrives → [Car1, Car2]
Car 3 arrives → [Car1, Car2, Car3]
Green light!
Car 1 leaves  → [Car2, Car3]
Car 2 leaves  → [Car3]
```

**Operations in my project**:
- `enqueue()` - Add vehicle to queue
- `dequeue()` - Remove vehicle from queue
- `size()` - Check how many vehicles waiting
- `is_empty()` - Check if queue is empty

**Time Complexity**: All operations are O(1) - very fast!

### Time Complexity Analysis:

| Operation | Complexity | Explanation |
|-----------|------------|-------------|
| `enqueue()` | O(1) | Just append to end of list |
| `dequeue()` | O(1) | Remove from front (pop first element) |
| `size()` | O(1) | Return length of list |
| `is_empty()` | O(1) | Check if length is 0 |
| `peek()` | O(1) | Look at first element |

**Why O(1)?** These operations don't depend on how many vehicles are in the queue. Whether there's 1 car or 100 cars, the operation takes the same time!

### 2. Priority Queue Logic

Not a traditional priority queue, but similar idea:

```
if Road_A_vehicles > 10:
    serve_Road_A_continuously()
else:
    serve_all_roads_equally()
```

### 3. Multi-level Queue Structure

```
LaneManager
  ├── Road A
  │     ├── Lane 1 (Queue)
  │     ├── Lane 2 (Queue)
  │     └── Lane 3 (Queue)
  ├── Road B (same structure)
  ├── Road C (same structure)
  └── Road D (same structure)
```

Total: 4 roads × 3 lanes = 12 separate queues!

### 4. Space Complexity

**Overall Space Complexity**: O(n) where n = total number of vehicles

```
Space used:
- Each vehicle: O(1) space (fixed attributes)
- Each queue: O(k) where k = vehicles in that queue
- Total queues: 12
- Total space: O(n) where n = sum of all vehicles
```

**Example**:
- 10 vehicles in system = 10 × vehicle_size memory
- 100 vehicles = 100 × vehicle_size memory
- Linear growth!

### 5. Algorithm Analysis

#### Priority Mode Algorithm

```
Time Complexity: O(m) where m = vehicles in priority road
Space Complexity: O(1) - no extra space needed

while priority_road_vehicles > 5:
    dequeue_one_vehicle()  # O(1)
    # Loop runs m times
```

#### Round-Robin Algorithm

```
Time Complexity: O(4 × k) = O(k) where k = vehicles served per cycle
Space Complexity: O(1)

for each road in [A, B, C, D]:  # O(4)
    serve_up_to_5_vehicles()      # O(5) = O(1)
```

---

## Installation

### What You Need:

1. **Python 3.13** (or any Python 3.x version)
2. **Pygame library** (for graphics)

### Step 1: Install Python

Download from: https://www.python.org/downloads/

Check if installed:
```bash
python --version
```

### Step 2: Install Pygame

```bash
pip install pygame
```

Verify it worked:
```bash
python -c "import pygame; print('Pygame installed!')"
```

### Step 3: Download This Project

```bash
git clone https://github.com/mdot2Kaustuv/DSA-Queue-Simulator.git
cd DSA-Queue-Simulator
```

Or download ZIP from GitHub and extract it.

### Folder Structure:

```
DSA-Queue-Simulator/
├── src/
│   ├── Generator.py          # Creates vehicles
│   ├── Queues.py             # Queue data structure
│   ├── Roads.py              # Road with 3 lanes
│   ├── Lanes.py              # Manages all roads
│   ├── Vehicles.py           # Vehicle class
│   ├── Trafficlights.py      # Light states (Red/Green)
│   ├── Traffic_controller.py # Main control logic
│   ├── Simulator.py          # Visual simulation
│   └── Traffic.data          # Log file
├── README.md
└── Simulator.mp4             # Demo video
```

---

## How to Run

### Method 1: Just Run Simulator (Easiest!)

```bash
cd DSA-Queue-Simulator
python src/Simulator.py
```

That's it! A window will open with the simulation.

### Method 2: Run Generator Separately (For Testing)

Terminal 1:
```bash
python src/Generator.py
```
You'll see output like:
```
2480,2,C,1766727594.3392065
4851,1,A,1766727595.8201047
```

Terminal 2:
```bash
python src/Simulator.py
```

### Using IDE (VS Code, PyCharm):

1. Open the `DSA-Queue-Simulator` folder
2. Open `src/Simulator.py`
3. Click Run button
4. Done!

---

## Project Files

### Core Files:

**1. Vehicles.py** - Vehicle class
```
class Vehicle:
    - id: unique number
    - lane: which lane (1, 2, or 3)
    - road: which road (A, B, C, or D)
    - time: when it was created
```

**2. Queues.py** - Basic Queue implementation
```
enqueue()  # Add vehicle
dequeue()  # Remove vehicle
size()     # Count vehicles
is_empty() # Check if empty
```

**3. Roads.py** - One road with 3 lanes
```
class Road:
    - Has 3 queues (one per lane)
    - enqueue(), dequeue(), size()
```

**4. Lanes.py** - Manages all 4 roads
```
class LaneManager:
    - Controls Road A, B, C, D
    - Routes vehicles to correct road and lane
```

**5. Trafficlights.py** - Light states
```
State 1 = RED (stop)
State 2 = GREEN (go)
```

**6. Traffic_controller.py** - Brain of the system!
```
- Checks queue sizes
- Decides which road gets green light
- Handles priority mode
- Uses round-robin for normal mode
```

**7. Generator.py** - Creates vehicles
```
- Random vehicle ID
- Random road choice
- Random timing (exponential distribution)
- Saves to Traffic.data
```

**8. Simulator.py** - Visual display
```
- Creates Pygame window
- Draws roads and lights
- Animates vehicle movement
- Runs everything together
```

---

## Understanding the Code

### Queue Operations (Queues.py)

```
# Creating a queue
queue = Queues()

# Adding vehicles (enqueue)
queue.enqueue(vehicle1) 
queue.enqueue(vehicle2) 

# Removing vehicles (dequeue)
first = queue.dequeue()  

# Checking size
count = queue.size()   

# Checking if empty
empty = queue.is_empty() 
```

### Priority Logic (Traffic_controller.py)

```
# Check if priority needed
def priority_condition_met(self):
    return self.lm.size("A", 1) > 10  # More than 10 cars?

# Main control loop
def run(self):
    while True:
        if priority_condition_met():
            serve_priority()     # Keep Road A green
        else:
            serve_normal_cycle() # Round-robin all roads
```

### Round-Robin Algorithm

```
roads = ["A", "B", "C", "D"]
for road in roads:
    if has_vehicles(road):
        set_green_light(road)
        serve_up_to_5_vehicles()
        move_to_next_road()
```

---

## How to Modify

### Change Traffic Density

In `Generator.py`:
```python
delay = 1.0  # Change to 0.5 for more traffic
             # Change to 2.0 for less traffic
```

### Change Priority Settings

In `Traffic_controller.py`:
```python
self.priority_threshold = 10  # Change to 15 for less priority
self.priority_min = 5         # Change to 3 to exit faster
```

### Change Priority Road

In `Traffic_controller.py`:
```python
self.priority_road = "A"  # Change to "B", "C", or "D"
```

### Change Vehicle Speed

In `Simulator.py`, find `VisualVehicle` class:
```python
self.speed = 4  # Change to 6 for faster, 2 for slower
```

### Change Window Size

In `Simulator.py`:
```python
WINDOW_WIDTH = 900   # Change to 1200 for bigger
WINDOW_HEIGHT = 900  # Change to 1200 for bigger
```

---

## Problems I Faced

### 1. Threading Issues
**Problem**: Generator and Controller running at same time caused errors

**Solution**: Used Python's threading module carefully, made LaneManager shared between threads

### 2. Visual Vehicles vs Logical Vehicles
**Problem**: Pygame vehicles and queue vehicles were different

**Solution**: Created two types - logical (in queue) and visual (on screen), synchronized them

### 3. Collision Detection
**Problem**: Cars were overlapping

**Solution**: Added distance checking before creating new visual vehicles

### 4. Priority Mode Stuck
**Problem**: System stayed in priority mode forever

**Solution**: Added exit condition (serve until count drops to 5)

### 5. Data File Growing Too Large
**Problem**: Traffic.data kept getting bigger

**Solution**: Can delete file anytime, or clear it with `> src/Traffic.data`

---
---

## What I Learned

1. **Queue is super useful** - Perfect for waiting lines
2. **FIFO makes sense** - First come, first served is fair
3. **Priority changes everything** - Emergency lanes work same way
4. **Threading is tricky** - Multiple things happening at once
5. **Visual helps understanding** - Seeing it makes DSA concepts clear

---

## References

6. **GeeksforGeeks - Queue Data Structure**
   - URL: https://www.geeksforgeeks.org/queue-data-structure/
   - Used for: Basic queue operations reference

7. **Programiz - Python Queue**
   - URL: https://www.programiz.com/dsa/queue
   - Used for: Implementation examples

8. **Real Python - Threading**
   - URL: https://realpython.com/intro-to-python-threading/
   - Used for: Multi-threading implementation

### Python Documentation

9. **Python Official Documentation**
   - Threading module: https://docs.python.org/3/library/threading.html
   - Time module: https://docs.python.org/3/library/time.html
   - Random module: https://docs.python.org/3/library/random.html

10. **Pygame Documentation**
    - Official docs: https://www.pygame.org/docs/
    - Used for: Graphics and animation


### Course Materials

15. **COMP202 Course Lecture Notes**
    - Instructor: Rupak Ghimire
    - Topics: Queue operations, FIFO principle, Time complexity

16. **COMP202 Lab Materials**
    - Queue implementation exercises
    - Algorithm analysis practice

### Video Tutorials Referenced

17. **"Queue Data Structure Explained"** - YouTube
    - For visual understanding of enqueue/dequeue

18. **"Python Threading Tutorial"** - YouTube
    - For understanding concurrent execution



*Project completed: December 27, 2025*
