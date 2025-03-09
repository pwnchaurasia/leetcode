from datetime import datetime

from march_Job_hunt.lld.parking_lot.enums import AppSettings, PaymentStatus


class SpotBooking:
    SPOT_BOOKING = []
    def __init__(self, spot, registration_number):
        self._spot = spot
        self._registration_number = registration_number
        self._start_time = None
        self._base_pay = AppSettings.BASE_PAY
        self._per_hr_charged = 0
        self._total_pay = 0
        self._end_time = None
        self._status = PaymentStatus.UNPAID


    def book(self):
        self._start_time = datetime.now()
        self.SPOT_BOOKING.append(self)
        print("Spot Booked")

    def calculate_final_payment(self):
        self._end_time = datetime.now()
        self._per_hr_charged = (self._end_time - self._start_time) * AppSettings.PER_HOUR
        self._total_pay = self._base_pay + self._per_hr_charged
        print(f"Total payment {self._total_pay}")


    def exit(self):
        booking = filter(lambda sp: sp == self, self.SPOT_BOOKING)
        booking = list(booking)
        spot_booking = booking[0]

