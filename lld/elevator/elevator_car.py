import heapq
import time
import threading

from lld.elevator.display import Display
from lld.elevator.enums import Direction, ElevatorState


class ElevatorCar:
    def __init__(self, elevator_id):
        self.id = elevator_id
        self.current_floor = 0
        self.direction = Direction.IDLE
        self.state = ElevatorState.IDLE
        self.destination_floors = []  # Min-heap for floors in the current direction
        self.lock = threading.Lock()
        self.display = Display(self)

    def add_destination(self, floor):
        with self.lock:
            if floor not in self.destination_floors:
                heapq.heappush(self.destination_floors, floor)

    def move(self):
        while True:
            with self.lock:
                if self.destination_floors:
                    next_floor = heapq.heappop(self.destination_floors)
                    self.state = ElevatorState.MOVING
                    self.direction = Direction.UP if next_floor > self.current_floor else Direction.DOWN
                    print(f"Elevator {self.id} is moving from floor {self.current_floor} to floor {next_floor}")
                    time.sleep(1)  # Simulate time taken to move between floors
                    self.current_floor = next_floor
                    self.display.update(self.current_floor, self.direction)
                    print(f"Elevator {self.id} has reached floor {self.current_floor}")
                    if not self.destination_floors:
                        self.state = ElevatorState.IDLE
                        self.direction = Direction.IDLE
                else:
                    self.state = ElevatorState.IDLE
                    self.direction = Direction.IDLE
            time.sleep(1)
