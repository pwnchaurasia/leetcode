# Button class (for both internal and external buttons)
from lld.elevator.request import Request


class Button:
    def __init__(self, control_system, floor):
        self.control_system = control_system
        self.floor = floor

    def press(self, destination_floor=None):
        request = Request(self.floor, destination_floor)
        self.control_system.add_request(request)
        print(f"Button pressed: Floor {self.floor}, Destination {destination_floor}")