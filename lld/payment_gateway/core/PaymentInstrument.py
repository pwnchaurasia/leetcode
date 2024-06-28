from typing import Dict, List

from lld.payment_gateway.core.enums import PaymentMethod
from lld.payment_gateway.core.users import User


class PaymentInstrument:
    PaymentInstruments: List[Dict] = []
    def __init__(self, user: User, method: PaymentMethod):
        self.__user = user
        self.__method = method


    def add_payment_method(self):
        self.PaymentInstruments.append({'user': self.__user, 'method': self.__method})

    def delete_payment_method(self):
        pass

    def update_payment_method(self):
        pass

    def list_all_payment_method(self, user):