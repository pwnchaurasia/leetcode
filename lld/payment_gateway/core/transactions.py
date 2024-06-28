from typing import

from lld.payment_gateway.core.enums import PaymentMethod
from lld.payment_gateway.core.users import User


class Transaction:
    def __init__(self, sender: User, receiver: User, method: PaymentMethod, amount: float):
        self.__sender = sender
        self.__receiver = receiver
        self.__method = method
        self.amount = float

    def validate_balance(self, user: User):
    def send_money(self):
        pass