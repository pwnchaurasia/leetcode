import abc

from lld.hotel_booking_system.enums import PaymentStatus


class BasePayment:
    def __init__(self, amount):
        self.amount = amount
        self.status = PaymentStatus.PENDING

    @abc.abstractmethod
    def charge(self):
        pass

    @abc.abstractmethod
    def refund(self):
        pass

class UPIPayment(BasePayment):
    def __init__(self, user, amount):
        super().__init__(amount)
        self.user = user

    def charge(self):
        print("Payment done")
        self.status = PaymentStatus.PAID

    def refund(self):
        print("Payment refunded")
