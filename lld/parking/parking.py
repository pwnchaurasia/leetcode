import threading

from lld.parking.enums import VehicleTypeEnum, SpotStatusEnum
from lld.parking.spots import Spots


class Parking:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.__initialized = False
        return cls._instance


    def __init__(self, name, address, car_count, motorcycle_count, van_count):
        if self.__initialized:
            return

        self.spots = []
        self.total_car_spots = car_count
        self.total_motorcycle_spots = motorcycle_count
        self.total_van_spots = van_count
        self.name = name
        self.address = address

        self.total_occupied = 0
        self.total_spots_count = {
            VehicleTypeEnum.CAR: 0,
            VehicleTypeEnum.MOTORCYCLE: 0,
            VehicleTypeEnum.VAN: 0,
        }


        self.total_vacant = car_count + motorcycle_count + van_count

        self.occupied_spot_count = {
            VehicleTypeEnum.CAR: 0,
            VehicleTypeEnum.MOTORCYCLE: 0,
            VehicleTypeEnum.VAN: 0,
        }

        self.__initialized = True

    def create_parking(self,):
        spots = []
        spot_id = 1
        for c in range(self.total_car_spots):
            spot = Spots(spot_id=1, spot_type=VehicleTypeEnum.CAR)
            spots.append(spot)
            spot_id += 1
        print(f"Created {self.total_car_spots} spots for {VehicleTypeEnum.CAR}")

        for m in range(self.total_motorcycle_spots):
            spot = Spots(spot_id=1, spot_type=VehicleTypeEnum.MOTORCYCLE)
            spots.append(spot)
            spot_id += 1
        print(f"Created {self.total_motorcycle_spots} spots for {VehicleTypeEnum.MOTORCYCLE}")

        for m in range(self.total_van_spots):
            spot = Spots(spot_id=1, spot_type=VehicleTypeEnum.VAN)
            spots.append(spot)
            spot_id += 1
        print(f"Created {self.total_van_spots} spots for {VehicleTypeEnum.VAN}")

        self.spots = spots

    def can_place(self, vehicle_type):
        if vehicle_type == self.occupied_spot_count and vehicle_type == self.total_spots_count:
            if self.occupied_spot_count[vehicle_type] < self.total_spots_count[vehicle_type]:
                return True
            print(f"{vehicle_type} is full")
            return False
        print("Not a valid vehicle type")
        return False


    def find_booking_place(self, vehicle_type):
        return next((
            spot for spot in self.spots if spot.spot_type == vehicle_type and spot.status == SpotStatusEnum.VACANT
        ),None)

    def book_a_spot(self, vehicle_type):
        # validate_if_can_be_placed
        # filter out the first place which vacant for that vehicle type and place the vehicle
        if self.can_place(vehicle_type):
            spot = self.find_booking_place(vehicle_type)
            if not spot:
                print("No spot found!!!!")
                return False
            spot.mark_occupied()
            self.occupied_spot_count[vehicle_type] += 1
            return spot

    def leaving_spot(self, spot):
        spot.mark_vacant()
        vehicle_type = spot.vehicle_type
        self.occupied_spot_count[vehicle_type] -= 1
        print("Marked v")










