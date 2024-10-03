import random

from lld.hotel_booking_system.enums import RoomTypes, RoomStatus


class Rooms:
    def __init__(self, hotel_id, room_type, price, room_number):
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.price = price
        self.status = RoomStatus.VACANT
        self.booked_till = None
        if room_type == RoomTypes.SINGLE_BED:
            self.room_number = "00" + str(room_number)
        elif room_type == RoomTypes.DOUBLE_BED:
            self.room_number = "11" + str(room_number)
        elif room_type == RoomTypes.SUIT:
            self.room_number = "22" + str(room_number)
        else:
            print("Invalid room type")

    def status(self):
        return self.status

    def book(self, till_date):
        if self.occupy():
            self.booked_till = till_date
            print("Room booked")
            return True
        print("Room not booked")
        return False

    def occupy(self):
        if self.status == RoomStatus.OCCUPIED:
            print("Room already occupied")
            return False
        self.status = RoomStatus.OCCUPIED
        print(f"Room {self.room_number} booked")
        return True

    def vacate(self):
        self.status = RoomStatus.VACANT
        self.booked_till = None
        print(f"Room {self.room_number} vacated")
        return True