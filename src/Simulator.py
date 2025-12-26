import pygame
import random
import math
from Lanes import LaneManager
from Traffic_controller import TrafficController
from Generator import generate_vehicle

# --- Pygame Configuration ---
WIDTH, HEIGHT = 800, 800
ROAD_WIDTH = 120
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

# Colors
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class PygameTrafficSim:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Traffic Intersection Simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)

        # 1. Shared Logic
        self.lm = LaneManager()
        self.controller = TrafficController(self.lm)

        # 2. Road Positions (for drawing)
        # Coordinates for where the roads enter the screen
        self.road_coords = {
            "A": {"pos": (WIDTH // 2, 100), "dir": (0, 1)},  # North
            "B": {"pos": (WIDTH - 100, HEIGHT // 2), "dir": (-1, 0)},  # East
            "C": {"pos": (WIDTH // 2, HEIGHT - 100), "dir": (0, -1)},  # South
            "D": {"pos": (100, HEIGHT // 2), "dir": (1, 0)}  # West
        }

    def draw_static_roads(self):
        # Draw background roads
        pygame.draw.rect(self.screen, GRAY, (WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, HEIGHT))  # Vertical
        pygame.draw.rect(self.screen, GRAY, (0, HEIGHT // 2 - ROAD_WIDTH // 2, WIDTH, ROAD_WIDTH))  # Horizontal
        # Intersection Box
        pygame.draw.rect(self.screen, (30, 30, 30),
                         (WIDTH // 2 - ROAD_WIDTH // 2, HEIGHT // 2 - ROAD_WIDTH // 2, ROAD_WIDTH, ROAD_WIDTH))

    def draw_status(self):
        # Show car counts for each road
        y_offset = 20
        for road_id in ["A", "B", "C", "D"]:
            count = self.lm.size(road_id, 2) + self.lm.size(road_id, 1) + self.lm.size(road_id, 3)
            light_state = "GREEN" if self.controller.lights[road_id].is_green() else "RED"
            color = GREEN if light_state == "GREEN" else RED

            txt = self.font.render(f"Road {road_id}: {count} cars | {light_state}", True, color)
            self.screen.blit(txt, (20, y_offset))
            y_offset += 25

    def run(self):
        # Event for spawning cars
        SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_EVENT, 1200)  # Spawn every 1.2s

        # Timer for the controller (replacement for time.sleep)
        CONTROLLER_TICK = pygame.USEREVENT + 2
        pygame.time.set_timer(CONTROLLER_TICK, 500)  # Run logic every 0.5s

        running = True
        while running:
            self.screen.fill((100, 150, 100))  # Grass background
            self.draw_static_roads()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Update shared manager when cars are generated
                if event.type == SPAWN_EVENT:
                    v = generate_vehicle(delay=0.1)
                    self.lm.enqueue(v.road, v.lane, v)

                # Run your controller logic without freezing the window
                if event.type == CONTROLLER_TICK:
                    self.controller.service_free_lanes()
                    if self.controller.priority_condition_met():
                        # We trigger serve_priority logic manually here to avoid its internal while True loop
                        self.controller.set_active_light(self.controller.priority_road)
                        self.controller.dequeue_controlled_vehicle(self.controller.priority_road)
                    else:
                        # Simple rotation for the demo
                        current_road = self.controller.roads[int(pygame.time.get_ticks() / 3000) % 4]
                        self.controller.set_active_light(current_road)
                        self.controller.dequeue_controlled_vehicle(current_road)

            # Draw Lights and Visual Car Indicators
            for road_id, info in self.road_coords.items():
                # Draw Light
                l_color = GREEN if self.controller.lights[road_id].is_green() else RED
                pygame.draw.circle(self.screen, l_color, info["pos"], 15)

                # Draw "Cars" as dots based on queue size
                q_size = self.lm.size(road_id, 2)
                for i in range(min(q_size, 10)):  # Cap at 10 dots for visuals
                    offset = (i + 1) * 25
                    car_x = info["pos"][0] - (info["dir"][0] * offset)
                    car_y = info["pos"][1] - (info["dir"][1] * offset)
                    pygame.draw.rect(self.screen, BLUE, (car_x - 5, car_y - 5, 10, 10))

            self.draw_status()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    sim = PygameTrafficSim()
    sim.run()