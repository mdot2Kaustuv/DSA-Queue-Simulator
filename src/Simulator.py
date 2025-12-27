import pygame
import threading
import sys
import time
from Lanes import LaneManager
from Traffic_controller import TrafficController
from Generator import generator

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
LANE_WIDTH = 40
ROAD_WIDTH = LANE_WIDTH * 2
COLOR_BG = (34, 139, 34)
COLOR_ROAD = (50, 50, 50)
COLOR_YELLOW = (255, 215, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 50, 50)
COLOR_GREEN = (50, 255, 50)
COLOR_ORANGE = (255, 165, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Traffic Simulation")
font = pygame.font.SysFont('Arial', 16, bold=True)


class VisualVehicle:
    def __init__(self, logical_vehicle):
        self.id = logical_vehicle.id
        self.road = logical_vehicle.road
        self.lane = logical_vehicle.lane
        self.speed = 4
        self.crossed_stop_line = False

        # Lane calculation
        if self.lane == 1:
            lane_offset = LANE_WIDTH / 2
        else:
            lane_offset = LANE_WIDTH + LANE_WIDTH / 2

        # Setup positions and direction
        if self.road == "A":  #  top  DOWN
            self.x = CENTER_X - lane_offset
            self.y = -40
            self.dir = (0, 1)
            self.stop_boundary = CENTER_Y - ROAD_WIDTH - 10
            self.angle = 180
        elif self.road == "B":  #  bottom  UP
            self.x = CENTER_X + lane_offset
            self.y = WINDOW_HEIGHT + 40
            self.dir = (0, -1)
            self.stop_boundary = CENTER_Y + ROAD_WIDTH + 10
            self.angle = 0
        elif self.road == "C":  #  right  LEFT
            self.x = WINDOW_WIDTH + 40
            self.y = CENTER_Y - lane_offset
            self.dir = (-1, 0)
            self.stop_boundary = CENTER_X + ROAD_WIDTH + 10
            self.angle = 90
        elif self.road == "D":  #  left  RIGHT
            self.x = -40
            self.y = CENTER_Y + lane_offset
            self.dir = (1, 0)
            self.stop_boundary = CENTER_X - ROAD_WIDTH - 10
            self.angle = 270

        # Create sprite
        self.image = pygame.Surface((18, 32), pygame.SRCALPHA)
        colors = [(100, 150, 255), (255, 100, 100), (100, 255, 100), (255, 255, 100)]
        color = colors[self.id % len(colors)]
        pygame.draw.rect(self.image, color, (0, 0, 18, 32), border_radius=4)
        pygame.draw.rect(self.image, (200, 200, 255), (2, 2, 14, 10), border_radius=2)
        self.image = pygame.transform.rotate(self.image, self.angle)

    def check_stop_line(self):
        if self.crossed_stop_line:
            return True

        if self.road == "A":
            return self.y > self.stop_boundary
        elif self.road == "B":
            return self.y < self.stop_boundary
        elif self.road == "C":
            return self.x < self.stop_boundary
        elif self.road == "D":
            return self.x > self.stop_boundary
        return False

    def update(self, light_is_green, vehicle_ahead):
        if not self.crossed_stop_line:
            self.crossed_stop_line = self.check_stop_line()

        should_move = True

        if not self.crossed_stop_line and not light_is_green:
            dist_to_line = abs((self.y if self.road in "AB" else self.x) - self.stop_boundary)
            if dist_to_line < 10:
                should_move = False

        if vehicle_ahead:
            distance = self.get_distance_to(vehicle_ahead)
            if distance < 50:
                should_move = False

        if should_move:
            self.x += self.dir[0] * self.speed
            self.y += self.dir[1] * self.speed

    def get_distance_to(self, other_vehicle):
        if self.road == "A":
            return other_vehicle.y - self.y
        elif self.road == "B":
            return self.y - other_vehicle.y
        elif self.road == "C":
            return self.x - other_vehicle.x
        elif self.road == "D":
            return other_vehicle.x - self.x
        return float('inf')

    def draw(self, surface):
        surface.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))


def draw_env(surface, controller):
    surface.fill(COLOR_BG)
    # Roads
    pygame.draw.rect(surface, COLOR_ROAD, (CENTER_X - ROAD_WIDTH, 0, ROAD_WIDTH * 2, WINDOW_HEIGHT))
    pygame.draw.rect(surface, COLOR_ROAD, (0, CENTER_Y - ROAD_WIDTH, WINDOW_WIDTH, ROAD_WIDTH * 2))

    # Stop Lines
    pygame.draw.line(surface, COLOR_WHITE, (CENTER_X - ROAD_WIDTH, CENTER_Y - ROAD_WIDTH - 5),
                     (CENTER_X, CENTER_Y - ROAD_WIDTH - 5), 4)  # A
    pygame.draw.line(surface, COLOR_WHITE, (CENTER_X, CENTER_Y + ROAD_WIDTH + 5),
                     (CENTER_X + ROAD_WIDTH, CENTER_Y + ROAD_WIDTH + 5), 4)  # B
    pygame.draw.line(surface, COLOR_WHITE, (CENTER_X + ROAD_WIDTH + 5, CENTER_Y - ROAD_WIDTH),
                     (CENTER_X + ROAD_WIDTH + 5, CENTER_Y), 4)  # C
    pygame.draw.line(surface, COLOR_WHITE, (CENTER_X - ROAD_WIDTH - 5, CENTER_Y),
                     (CENTER_X - ROAD_WIDTH - 5, CENTER_Y + ROAD_WIDTH), 4)  # D

    pygame.draw.line(surface, COLOR_YELLOW, (CENTER_X, 0), (CENTER_X, WINDOW_HEIGHT), 3)
    pygame.draw.line(surface, COLOR_YELLOW, (0, CENTER_Y), (WINDOW_WIDTH, CENTER_Y), 3)

    light_coords = {
        "A": (CENTER_X - ROAD_WIDTH - 30, CENTER_Y - ROAD_WIDTH - 30),
        "B": (CENTER_X + ROAD_WIDTH + 30, CENTER_Y + ROAD_WIDTH + 30),
        "C": (CENTER_X + ROAD_WIDTH + 30, CENTER_Y - ROAD_WIDTH - 30),
        "D": (CENTER_X - ROAD_WIDTH - 30, CENTER_Y + ROAD_WIDTH + 30)
    }
    for road, pos in light_coords.items():
        col = COLOR_GREEN if controller.lights[road].is_green() else COLOR_RED
        pygame.draw.circle(surface, (30, 30, 30), pos, 20)
        pygame.draw.circle(surface, col, pos, 15)
        label = font.render(road, True, COLOR_WHITE)
        surface.blit(label, (pos[0] - 5, pos[1] - 35))


def main():
    lm = LaneManager()

    class SafeController(TrafficController):
        def __init__(self, shared_lm):
            super().__init__(shared_lm)
            self.delay = 3.0

        def set_active_light(self, active_road):
            super().set_active_light(active_road)
            time.sleep(2.0)

        def dequeue_controlled_vehicle(self, road):
            if self.lm.size(road, 1) > 0:
                return True
            return False

    controller = SafeController(lm)

    visual_vehicles = []

    t_ctrl = threading.Thread(target=controller.run, daemon=True)
    t_ctrl.start()
    t_gen = threading.Thread(target=generator, args=(lm,), daemon=True)
    t_gen.start()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        for road in ["A", "B", "C", "D"]:
            for lane in [1, 2]:
                q_size = lm.size(road, lane)
                visuals_in_lane = [v for v in visual_vehicles
                                   if v.road == road and v.lane == lane and not v.crossed_stop_line]

                if len(visuals_in_lane) < q_size:
                    vid = int(time.time() * 1000)
                    new_veh = VisualVehicle(type('', (object,), {"road": road, "lane": lane, "id": vid})())

                    safe = True
                    if visuals_in_lane:
                        last = visuals_in_lane[-1]
                        if new_veh.get_distance_to(last) < 60:
                            safe = False

                    if safe:
                        visual_vehicles.append(new_veh)

        vehicles_to_remove = []
        for v in visual_vehicles:
            is_green = controller.lights[v.road].is_green()

            ahead = None
            min_dist = 9999
            for other in visual_vehicles:
                if other.road == v.road and other.lane == v.lane and other.id != v.id:
                    dist = v.get_distance_to(other)
                    if 0 < dist < min_dist:
                        min_dist = dist
                        ahead = other

            v.update(is_green, ahead)

            if v.crossed_stop_line and not getattr(v, 'dequeued_from_backend', False):
                if lm.size(v.road, v.lane) > 0:
                    lm.dequeue(v.road, v.lane)
                    v.dequeued_from_backend = True

            if (v.x < -100 or v.x > WINDOW_WIDTH + 100 or
                    v.y < -100 or v.y > WINDOW_HEIGHT + 100):
                vehicles_to_remove.append(v)

        for v in vehicles_to_remove:
            if v in visual_vehicles:
                visual_vehicles.remove(v)

        draw_env(screen, controller)
        for v in visual_vehicles:
            v.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()





