from march_Job_hunt.lld.parking_lot.enums import SpotStatus
from slots import Slot

class Parking:
    def __init__(self, name):
        self._name = name
        self._spots = {}


    def add_spot(self, vehicle_type, operation_type, count):
        key = f"{vehicle_type}_{operation_type}"
        if  key in self._spots:
            print("Vehicle type already added")
            return False
        data = []
        for i in range(count):
            spot = Slot(vehicle_type, operation_type)
            data.append(spot)
        self._spots[key] = data


    def book_spot(self, vehicle_type, operation_type):
        key = f"{vehicle_type}_{operation_type}"

        data = self._spots[key]
        vacant_spots = filter(lambda spot: spot._status == SpotStatus.VACANT, data)
        vacant_spots = list(vacant_spots)
        if len(vacant_spots) <= 0:
            print("No space available to park this vehicle")
            return False

        vacant_spot = vacant_spots[0]
        vacant_spot.mark_occupied()
