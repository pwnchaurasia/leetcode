from abc import ABC, abstractmethod

class ParkingTicket:
    def __init__(self, id, parking_spot, parking_spot_type, date_time) -> None:
        self.id = id
        self.parking_spot = parking_spot
        self.parking_spot_type = parking_spot_type
        self.date_time = date_time