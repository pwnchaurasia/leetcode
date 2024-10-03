from datetime import datetime
import random

from lld.hotel_booking_system.enums import PaymentMethod
from lld.hotel_booking_system.payment import UPIPayment


class PaymentService:
    payment_records = []

    @classmethod
    def payment(cls, user, hotel, amount, payment_method):
        if payment_method == PaymentMethod.UPI:
            UPIPayment(user, amount).charge()
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
        return False, None

    @classmethod
    def refund(cls, payment_id):
        payment = filter(lambda record: record['payment_id'] == payment_id, cls.payment_records)
        UPIPayment(payment[0]['user'], payment[0]['amount']).refund()
        print("Amount refunded successfully")
        return True
