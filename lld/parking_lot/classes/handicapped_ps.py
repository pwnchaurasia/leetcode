from interface.parking_spot import ParkingSpot
from enums.parking_spot_type import ParkingSpotType
class HandicappedParkingSpot(ParkingSpot):
    def __init__(self, number) -> None:
        super().__init__(number, ParkingSpotType.HANDICAPPED)
    
