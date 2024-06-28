from lld.payment_gateway.core.enums import PaymentMethod


class User:
    def __init__(self, name, mobile):
        self.__name = name
        self.__mobile = mobile
        self.payment_methods = []
        self.default_payment_method = PaymentMethod.BANK.name
