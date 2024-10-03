from lld.hotel_booking_system.enums import RoomStatus
from lld.hotel_booking_system.rooms import Rooms


class Hotel:
    def __init__(self, hotel_id, hotel_name, hotel_address):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address
        self.rooms = []

    def add_rooms(self, room_type, count, price):
        """Creating rooms for the hotel with room type and count and there price"""
        for i in range(1, count+1):
            room = Rooms(room_type=room_type, price=price, hotel_id=self.hotel_id, room_number=i)
            self.rooms.append(room)
        print(f"{count} rooms added for room type {room_type}")


    def get_rooms(self):
        rooms = [room for room in self.rooms if room.status == RoomStatus.VACANT]
        return rooms

    def get_hotel_id(self):
        return self.hotel_id

    def get_hotel_name(self):
        return self.hotel_name

    def get_hotel_address(self):
        return self.hotel_address

    def get_location(self):
        # convert this in long lat
        return self.get_hotel_address()

    def book(self, room, days):
        if room.book(days):
            print(f"Room {room} is booked in the hotel {self} for {days} days")
            return True
        return False

    def calculate_cost(self, room, days):
        cost = room.price * days
        print(f"Room {room} cost for {days} days is {cost}")
        return cost