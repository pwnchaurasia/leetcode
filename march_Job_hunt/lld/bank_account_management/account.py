from abc import abstractmethod, ABC
from threading import Lock

from march_Job_hunt.lld.bank_account_management.enums import AccountStatus, TransactionType
from march_Job_hunt.lld.bank_account_management.ledger import Ledger


class Account(ABC):

    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.status = AccountStatus.ACTIVE
        self._lock = Lock()

    @abstractmethod
    def deposit(self, amount):
        pass


    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):
    MIN_BALANCE = 500

    def deposit(self, amount):
        with self._lock:
            self.balance += amount
            ledger = Ledger(account=self, transaction_type=TransactionType.CREDIT, amount=amount)
            ledger.make_entry()

    def withdraw(self, amount):
        with self._lock:  # Prevents race condition in balance updates
            if amount > self.balance:
                print("Insufficient funds")
                return False
            self.balance -= amount
            ledger = Ledger(account=self, transaction_type=TransactionType.DEBIT, amount=amount)
            ledger.make_entry()

    def check_balance(self):
        print(f"your balance is  {self.balance}")
        return self.balance

    def put_account_on_hold(self):
        self.status = AccountStatus.HOLD

    def close_account(self):
        self.status = AccountStatus.CLOSE

    def account_status(self):
        print(f"Account status is {self.status}")

    def account_statement(self):
        ledger_entries = Ledger(account=self).statement()
        print(f"Total {len(ledger_entries)} found")
        for entry in ledger_entries:
            print(entry)

    def transfer_money(self, pay_to_account, amount):
        if self.balance < amount:
            print("You dont have balance to do this transaction")
            return False
        else:
            self.withdraw(amount=amount)
            pay_to_account.deposit(amount=amount)
            print("Transaction complete")

    def __repr__(self):
        return f"{self.account_number} / {self.status} / {self.account_type}"


class CurrentAccount(Account):

    def __init__(self, account_number, account_type, balance):
        super().__init__(account_number, account_type, balance)
        self.overdraft_limit = 1000

    def deposit(self, amount):
        with self._lock:
            self.balance += amount
            ledger = Ledger(account=self, transaction_type=TransactionType.CREDIT, amount=amount)
            ledger.make_entry()

    def withdraw(self, amount):
        with self._lock:  # Prevents race condition in balance updates
            if amount > self.balance:
                print("Insufficient funds")
                return False
            self.balance -= amount
            ledger = Ledger(account=self, transaction_type=TransactionType.DEBIT, amount=amount)
            ledger.make_entry()

    def check_balance(self):
        print(f"your balance is  {self.balance}")
        return self.balance

    def put_account_on_hold(self):
        self.status = AccountStatus.HOLD

    def close_account(self):
        self.status = AccountStatus.CLOSE

    def account_status(self):
        print(f"Account status is {self.status}")

    def account_statement(self):
        ledger_entries = Ledger(account=self).statement()
        print(f"Total {len(ledger_entries)} found")
        for entry in ledger_entries:
            print(entry)

    def __repr__(self):
        return f"{self.account_number} / {self.status} / {self.account_type}"