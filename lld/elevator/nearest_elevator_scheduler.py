from abc import ABC, abstractmethod

from lld.elevator.enums import ElevatorState


# Scheduler interface
class Scheduler(ABC):
    @abstractmethod
    def schedule(self, request, elevators):
        pass

# Nearest elevator scheduler
class NearestElevatorScheduler(Scheduler):
    def schedule(self, request, elevators):
        best_elevator = None
        min_distance = float('inf')

        for elevator in elevators:
            distance = abs(elevator.current_floor - request.source_floor)
            if distance < min_distance and elevator.state == ElevatorState.IDLE:
                min_distance = distance
                best_elevator = elevator

        if best_elevator:
            best_elevator.add_destination(request.source_floor)
            if request.destination_floor:
                best_elevator.add_destination(request.destination_floor)
            return best_elevator
        return None