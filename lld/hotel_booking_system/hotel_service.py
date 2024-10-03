from lld.hotel_booking_system.hotel import Hotel


class HotelService:
    __available_hotels = []

    @classmethod
    def search_hotels(cls, hotel_id=None, hotel_name=None, hotel_location=None, distance_rage=15):
        if hotel_id:
            results = [hotel for hotel in cls.__available_hotels if hotel.get_hotel_id() == hotel_id]
            return results
        if hotel_name:
            results = [hotel for hotel in cls.__available_hotels if hotel.get_hotel_name() == hotel_name]
            return results
        if hotel_location:
            results = [hotel for hotel in cls.__available_hotels if hotel.get_location() <= distance_rage]
            return results
        return cls.__available_hotels

    @classmethod
    def __add_hotel(cls, hotel):
        cls.__available_hotels.append(hotel)

    @classmethod
    def show_hotel_rooms(cls, hotel):
        return hotel.get_rooms()

    @classmethod
    def booking_request(cls, hotel, room, days):
        is_room_booked = hotel.book(room, days)
        if is_room_booked:
            print("Room booked")
        else:
            print("Not booked")
        return is_room_booked

    @classmethod
    def calculate_cost(cls, hotel, room, count, days):
        return hotel.calculate_cost(room, count, days)
