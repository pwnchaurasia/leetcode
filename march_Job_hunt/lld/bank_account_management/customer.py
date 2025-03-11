from march_Job_hunt.lld.bank_account_management.account import Account, SavingsAccount, CurrentAccount
from march_Job_hunt.lld.bank_account_management.enums import AccountType
from march_Job_hunt.lld.bank_account_management.utils import generate_account_number


class Customer:

    def __init__(self, name, pan):
        self.name = name
        self.pan = pan
        self.bank_account = {}

    @staticmethod
    def create_account(account_type=AccountType.SAVINGS):
        account_number = generate_account_number()
        if account_type == AccountType.SAVINGS:
            account = SavingsAccount(account_number=account_number, account_type=account_type)
        elif account_type == AccountType.CURRENT:
            account = CurrentAccount(account_number=account_number, account_type=account_type)
        else:
            raise ValueError("Account type not allowed")
        return account

    def add_bank_account(self, account):
        self.bank_account[account.account_number] = account
        print("Bank account added for customer")


    def update_details(self):
        pass



