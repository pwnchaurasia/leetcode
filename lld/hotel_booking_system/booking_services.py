from lld.hotel_booking_system.hotel_service import HotelService
from lld.hotel_booking_system.notification import Notification
from lld.hotel_booking_system.payment_service import PaymentService


class BookingServices:
    __bookings = []


    @classmethod
    def list_hotels(cls, hotel_id, name, location):
        return HotelService.search_hotels(hotel_id=hotel_id, hotel_name=name, hotel_location=location)

    @classmethod
    def show_rooms(cls, hotel_id):
        return HotelService.show_hotel_rooms(hotel_id)

    @classmethod
    def book_room(cls, hotel, room, days, user, payment_method):
        calculate_cost = cls.calculate_cost(hotel, room, days=days)
        is_payment_done, payment_id = PaymentService.payment(user=user, amount=calculate_cost, payment_method=payment_method)
        if is_payment_done:
            booking_done = HotelService.booking_request(hotel=hotel, room=room, days=days)
            if booking_done:
                Notification(user, "Booking was successful.").send()
                data = {
                    'hotel': hotel,
                    'user': user,
                    'room': room,
                    'days': days,
                    'payment_id': payment_id
                }
                cls.__bookings.append(data)
            else:
                Notification(user, "Booking not done successful.").send()
                PaymentService.refund(payment_id)

    @classmethod
    def calculate_cost(cls, hotel, room, days):
        return HotelService.calculate_cost(hotel, room, days)