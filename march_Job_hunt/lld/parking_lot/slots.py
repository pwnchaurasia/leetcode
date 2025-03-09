from march_Job_hunt.lld.parking_lot.enums import SpotStatus


class Slot:
    ID = 0
    def __init__(self, vehicle_type, spot_type):
        self._vehicle_type = vehicle_type
        self._spot_type = spot_type
        Slot.ID += 1
        self._id = Slot.ID
        self._status = SpotStatus.VACANT

    def mark_occupied(self):
        self._status = SpotStatus.OCCUPIED
        print("Spot is occupied")


    def mark_vacant(self):
        self._status = SpotStatus.VACANT
        print("Spot is Vacant")
