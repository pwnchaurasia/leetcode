import threading
import time
from lld.elevator.buttons import Button
from lld.elevator.elevator_control_system import ElevatorControlSystem
from lld.elevator.nearest_elevator_scheduler import NearestElevatorScheduler

if __name__ == "__main__":
    num_elevators = 3
    scheduler = NearestElevatorScheduler()
    control_system = ElevatorControlSystem(num_elevators, scheduler)

    # Start elevators
    control_system.start_elevators()

    # Start processing requests in a separate thread
    threading.Thread(target=control_system.process_requests, daemon=True).start()

    # Simulate external and internal buttons
    external_button_floor_0 = Button(control_system, 0)
    external_button_floor_3 = Button(control_system, 3)
    internal_button_elevator_0 = Button(control_system, 0)

    # Simulate button pressesR
    external_button_floor_0.press(5)  # External request from floor 0 to 5
    time.sleep(2)
    external_button_floor_3.press(7)  # External request from floor 3 to 7
    time.sleep(2)
    internal_button_elevator_0.press(4)  # Internal request inside elevator 0 to floor 4

    # Keep the main thread alive
    time.sleep(10)