from datetime import datetime
import random

from lld.food_delivery.enums import ChargeTypes, PaymentStatuses
from lld.food_delivery.payment import UPIPayment, StripePayment, CardPayment


class PaymentFactory:
    @staticmethod
    def get_payment_method(user, charge_type, amount):
        if charge_type == ChargeTypes.UPI.value:
            return UPIPayment(user=user, charge_type=charge_type, amount=amount)
        elif charge_type == ChargeTypes.CARD.value:
            return CardPayment(user=user, charge_type=charge_type, amount=amount)
        elif charge_type == ChargeTypes.STRIPE.value:
            return StripePayment(user=user, charge_type=charge_type, amount=amount)
        else:
            return ValueError('Invalid charge type')


class PaymentService:
    payments = []

    @classmethod
    def payment(cls, user, restaurant, charge_type, amount):
        payment = PaymentFactory.get_payment_method(user, charge_type, amount)
        payment.charge()
        print("Payment done")
        data = {
            'user': user,
            'restaurant': restaurant,
            'charge_type': charge_type,
            'amount': amount,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'payment_id': random.randint(1000000, 9999999),
            'status': PaymentStatuses.SUCCESS.value,
        }
        cls.payments.append(data)
        return True, data['payment_id']

    @classmethod
    def refund(cls, payment_id):
         payment = filter(lambda record: record['payment_id'] == payment_id, cls.payments)[0]
         if payment:
             payment_instance = PaymentFactory.get_payment_method(payment['charge_type'], payment['amount'])
             payment_instance.refund()
            # update the payment status to refunded here

    @classmethod
    def list_all_payments(cls):
        return cls.payments