Traffic Management System and DSA Queue Management System
Title
Assignment: 1

Name: Kaustuv Bhandari

Roll Number: 11

Course: COMP202

Submitted to: Rupak Ghimire

Date: 2025-12-27

Overview
This project simulates a 4-way traffic intersection using Python and Pygame. The core objective of this project is to demonstrate the practical use of Data Structures and Algorithms (DSA).

This project demonstrates the use of Queue and Priority Queue algorithms to simulate a four-way junction using linear data structures to manage vehicle flow and traffic light transitions based on real-time lane conditions. Unlike standard traffic lights which use timers, this simulation uses a Priority Queue logic. If North most lane (Road A, Lane 1) traffic exceeds more than 10, the system prioritizes the lane AL2 to handle the traffic congestion.

Output
System Overview
The system follows a Producer-Consumer pattern. The Generator produces vehicle data (incoming traffic), while the Simulator and Traffic_Controller consume that data to manage the junction flow using data structures.

Generator.py: Produces vehicle data (incoming traffic) by randomly determining the Vehicle ID, Time, road, and lane, then writes it to the Traffic.data file.

Traffic_controller.py & Trafficlights.py: Traffic_controller.py monitors these queues, triggering a high-priority state if lane AL1 exceeds 10 vehicles, ensuring it is served first until the count drops below 5. Trafficlights.py switches lights between State 1 (Red/Stop) and State 2 (Green/Go).

Queues.py, Lanes.py, & Roads.py: Implements the linear logic where vehicles enter (enqueue) and exit (dequeue) the junction.

Simulator.py: Integrates these components using Pygame to visually render the junction, manage traffic light states (Red/Green), and ensure safety by preventing deadlocks through strict state management.

Features
Intelligent Priority Management: The system actively monitors the queue length of Lane AL2. When congestion exceeds 10 vehicles, it activates a "Priority Mode" that overrides standard cycles to grant a continuous green light until the lane count is reduced to 5 or fewer.

Left-Hand Traffic (LHT) Standard: The simulation is designed to follow LHT protocols, which are the standard driving rules in regions like Nepal and the UK.

Real-Time Graphical Visualization: Utilizing Pygame, the simulator.py script provides a high-fidelity visualization featuring animated vehicle movement, realistic lane markings, and glowing traffic light indicators.

Traffic Generation: Using a producer-consumer architecture, Generator.py simulates varying traffic loads by writing vehicle data to Traffic.data, which the simulator then polls to update internal lane queues.

Installation and Prerequisites
This project requires Python 3.13 to run smoothly and as intended. You will also need to install the external library Pygame for visualization.

1. Install Dependencies
Pygame is the only external dependency required. Open your terminal or command prompt and run:

Bash

pip install pygame
2. Setup
Clone the repository:

Bash

git clone https://github.com/pxrbat/traffic-light-simulation-dsa.git
Ensure your folder format looks like this:

Plaintext

/DSA-Queue-Simulator/
├── src/
│   ├── Generator.py
│   ├── Lanes.py
│   ├── Queues.py
│   ├── Roads.py
│   ├── Simulator.py
│   ├── Traffic_controller.py
│   ├── Traffic.data
│   ├── Vehicles.py
├── .gitignore
├── README.md
└── Simulator.mp4
Execution Instructions
After cloning the repository, access the directory:

Bash

cd traffic-light-simulation-dsa
If you have an IDE, you can directly run the project by opening Simulator.py. Otherwise, use the command line:

Starting Generator.py:

Bash

python src/Generator.py
Example Output: 2480,2,C,1766727594.3392065

(This window can be kept open or closed as Simulator.py will automatically run it.)

Starting the Simulator:

Bash

python src/Simulator.py
Output: A Pygame window with the simulation.
