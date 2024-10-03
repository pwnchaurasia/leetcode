from enum import Enum


class RoomTypes(Enum):
    SINGLE_BED = 'SINGLE_BED'
    DOUBLE_BED = 'DOUBLE_BED'
    SUIT = 'SUIT'

class RoomStatus(Enum):
    VACANT = 'VACANT'
    OCCUPIED = 'OCCUPIED'


class PaymentStatus(Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'
    REJECTED = 'REJECTED'
    REFUNDED = 'REFUNDED'

class PaymentMethod(Enum):
    UPI = 'UPI'
    CARD = 'CARD'
    PAYPAL = 'PAYPAL'