from lld.ride_sharing.enums import PaymentMethod


class Payment:
    def __init__(self, user_id, payment_method, amount):
        self.user_id = user_id
        self.payment_method = payment_method
        self.amount = amount

    def charge(self):
        if self.payment_method == PaymentMethod.UPI:
            return UPIPayment(self.user_id, self.amount).charge()
        elif self.payment_method == PaymentMethod.WALLET:
            return WalletPayment(self.user_id, self.amount).charge()
        elif self.payment_method == PaymentMethod.CASH:
            print("Cash payment accepted")
            return True


class UPIPayment:
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount

    def charge(self):
        if self.amount > 0:
            return True
        return False

class Wallet:
    wallet = {}
    def __init__(self, user_id):
        self.user_id = user_id
        self.wallet[self.user_id] = self.wallet.get(self.user_id, 0)

    def add_money(self, amount):
        self.wallet[self.user_id] += amount

    def pay_money(self, amount):
        current_balance = self.wallet[self.user_id]
        if current_balance >= amount:
            self.wallet[self.user_id] -= amount
            print("Payment done")
            return True
        else:
            print("Cant pay you dont have balance")
            return False

    def my_balance(self):
        return self.wallet[self.user_id]

class WalletPayment:
    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount
        self.wallet = wallet = Wallet(self.user_id)

    def user_balance(self):
        return self.wallet.my_balance()

    def charge(self):
        if self.amount <= 0:
            print("Cant charge negative amount")
            return False
        if self.amount > self.user_balance():
            print("Cant charge more than user balance")
            return False
        return self.wallet.pay_money(self.amount)

