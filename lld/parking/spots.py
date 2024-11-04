from lld.parking.enums import SpotStatusEnum
from datetime import datetime


class Spots:
    spots = []
    def __init__(self, spot_id, spot_type):
        self.status = SpotStatusEnum.VACANT
        self.spot_type = spot_type
        self.spot_id = spot_id
        self.booking_start_time = None
        self.booking_end_time = None

    def __repr__(self):
        return f"Spot {self.spot_id} for {self.spot_type} is {self.status}"

    def mark_occupied(self, status):
        self.status = SpotStatusEnum.OCCUPIED
        self.booking_start_time = datetime.now()
        print(f"{self}")

    def mark_vacant(self):
        self.status = SpotStatusEnum.VACANT
        self.booking_end_time = datetime.now()
        print(f"{self}")
    
    def refresh_spot(self):
        self.booking_start_time = None
        self.booking_end_time = None
        self.status = SpotStatusEnum.VACANT
        print(f"Spot {self} refreshed")