import threading
import time

from lld.elevator.elevator_car import ElevatorCar


class ElevatorControlSystem:
    def __init__(self, num_elevators, scheduler):
        self.elevators = [ElevatorCar(i) for i in range(num_elevators)]
        self.scheduler = scheduler
        self.request_queue = []
        self.lock = threading.Lock()

    def start_elevators(self):
        for elevator in self.elevators:
            threading.Thread(target=elevator.move, daemon=True).start()

    def add_request(self, request):
        self.request_queue.append(request)

    def process_requests(self):
        while True:
            with self.lock:
                if self.request_queue:
                    request = self.request_queue.pop(0)
                    elevator = self.scheduler.schedule(request, self.elevators)
                    if not elevator:
                        print("No elevator available. Please wait")
            time.sleep(1)

