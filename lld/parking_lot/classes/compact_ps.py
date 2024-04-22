from interface.parking_spot import ParkingSpot

class CompactParkingSpot(ParkingSpot):
    def __init__(self, id, reserve) -> None:
        super().__init__(id, reserve)
    
