

"""
1. Will have multiple level,
2. Will have space for different vehicle types, [petrol, ev] - [Car, van, bus, bike]
3. Time based parking, will be charged, a base fare, and then per hour X additional X amount
4. Pay at exit

"""
from march_Job_hunt.lld.parking_lot.enums import VehicleType, VehicleOperationType
from march_Job_hunt.lld.parking_lot.parking import Parking




if __name__ == "__main__":
    parking = Parking(name="Vigyan Vihar")

    parking.add_spot(vehicle_type=VehicleType.CAR,
                     operation_type=VehicleOperationType.PETROL, count=20)


