from enum import Enum


class UserTypes(Enum):
    CUSTOMER = "CUSTOMER"
    OWNER = "OWNER"
    DELIVERY_PERSON = "DELIVERY_PERSON"


class ChargeTypes(Enum):
    UPI = "UPI"
    CARD = "CARD"
    STRIPE = "STRIPE"

class PaymentStatuses(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

class OrderStatuses(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    IN_PROGRESS = "IN_PROGRESS"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"