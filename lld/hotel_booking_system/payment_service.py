from datetime import datetime
import random

from lld.hotel_booking_system.enums import PaymentMethod
from lld.hotel_booking_system.payment import UPIPayment, CardPayment


class PaymentFactory:
    @staticmethod
    def get_payment_method(payment_method, user, amount):
        if payment_method == PaymentMethod.UPI.value:
            return UPIPayment(user, amount)
        elif payment_method == PaymentMethod.CARD.value:
            return CardPayment(user, amount)
        else:
            return ValueError("Not allowed payment method")





class PaymentService:
    payment_records = []

    @classmethod
    def payment(cls, user, hotel, amount, payment_method):
        payment_instance = PaymentFactory.get_payment_method(payment_method, user, amount)
        try:
            payment_instance.charge()
            print("payment done successfully")
            data = {
                'user': user,
                'hotel': hotel,
                'amount': amount,
                'payment_method': PaymentMethod.UPI,
                'date': datetime.now().strftime('%Y-%m-%d'),
                'payment_id': random.randint(1000000, 9999999)

            }
            cls.payment_records.append(data)
            return True, data['payment_id']
        except Exception as e:
            print(f"Error: {str(e)}")
            return False, None

    @classmethod
    def refund(cls, payment_id):
        payment = filter(lambda record: record['payment_id'] == payment_id, cls.payment_records)
        if payment:
            payment_instance = PaymentFactory.get_payment_method(payment['payment_method'], payment['user'], payment['amount'])
            payment_instance.refund()
            print("Amount refunded successfully")
            return True
        return False
