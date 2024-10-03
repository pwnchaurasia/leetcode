import enum


class UserType(enum.Enum):
    RIDER =  "RIDER"
    DRIVER = "DRIVER"


class RideStatus(enum.Enum):
    Requested = "Requested"
    Accepted = "Accepted"
    In_Progress = "In_Progress"
    Completed = "Completed"
    Canceled = "Canceled"


class PaymentMethod(enum.Enum):
    UPI = "UPI"
    CASH = "CASH"
    WALLET = "WALLET"