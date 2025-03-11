import datetime


class Ledger:
    LEDGER = {}
    """
        "account_number" :[] this list would store all the things that happened to that account
    """
    def __init__(self, account, transaction_type=None, amount=None):
            self.account = account
            self.transaction_type = transaction_type
            self.amount = amount

    def make_entry(self):
        if not self.transaction_type or not self.amount:
            raise ValueError("Transaction type and amount must not be None")
        else:
            data = {
                "transaction_type": self.transaction_type,
                "amount": self.amount,
                "date": datetime.datetime.now()
            }
            if self.account in self.LEDGER:
                account = self.LEDGER[self.account]
                account.append(data)
            else:
                self.LEDGER[self.account] = [data]
            print("Ledger entry created")

    def statement(self):
        if self.account not in self.LEDGER:
            print("No entry found")
            return False
        else:
            return self.LEDGER[self.account]