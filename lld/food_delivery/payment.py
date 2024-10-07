import abc


class BasePayment(metaclass=abc.ABCMeta):
    def __init__(self, user, charge_type, amount):
        self.user = user
        self.charge_type = charge_type
        self.amount = amount

    @abc.abstractmethod
    def charge(self):
        pass

    @abc.abstractmethod
    def refund(self):
        pass



class UPIPayment(BasePayment):
    def __init__(self, user, charge_type, amount):
        super().__init__(user, charge_type, amount)

    def charge(self):
        print("Charged customer")
        return True

    def refund(self):
        print("Refunded customer")
        return True

class CardPayment(BasePayment):
    def __init__(self, user, charge_type, amount):
        super().__init__(user, charge_type, amount)

    def charge(self):
        print("Charged customer")
        return True

    def refund(self):
        print("Refunded customer")
        return True

class StripePayment(BasePayment):
    def __init__(self, user, charge_type, amount):
        super().__init__(user, charge_type, amount)

    def charge(self):
        print("Charged customer")
        return True

    def refund(self):
        print("Refunded customer")
        return True