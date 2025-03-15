# Request class
from lld.elevator.enums import Direction


class Request:
    def __init__(self, source_floor, destination_floor=None):
        self.source_floor = source_floor
        self.destination_floor = destination_floor
        self.direction = Direction.UP if destination_floor > source_floor else Direction.DOWN

    def __lt__(self, other):
        return self.source_floor < other.source_floor