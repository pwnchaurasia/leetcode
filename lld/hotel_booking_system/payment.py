import abc

from lld.hotel_booking_system.enums import PaymentStatus


class BasePayment(metaclass=abc.ABCMeta):
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
        print(f"Charging {self.amount} via UPI for {self.user}")
        self.status = PaymentStatus.PAID
        return True

    def refund(self):
        print(f"Refunding {self.amount} to {self.user} via Card")
        self.status = PaymentStatus.REFUNDED
        return True


class CardPayment(BasePayment):
    def __init__(self, user, amount):
        super().__init__(amount)
        self.user = user

    def charge(self):
        print(f"Charging {self.amount} via Card for {self.user}")
        self.status = PaymentStatus.PAID
        return True

    def refund(self):
        print(f"Refunding {self.amount} to {self.user} via Card")
        self.status = PaymentStatus.REFUNDED
        return True