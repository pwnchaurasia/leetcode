

from march_Job_hunt.lld.bank_account_management.customer import Customer
from march_Job_hunt.lld.bank_account_management.enums import AccountType

# create customer


if __name__ == "__main__":
    customer1 = Customer(name="pawan", pan="abcd")
    account = Customer.create_account(account_type=AccountType.SAVINGS)
    customer1.add_bank_account(account=account)


    account.withdraw(amount=500)

    account.deposit(amount=500)
    print(account.balance)

    account.account_statement()

    account.withdraw(amount=200)

    print(account.balance)

    account.account_statement()

    print(account.balance)

    customer2 = Customer(name="Samael", pan="kgpo")
    account2 = Customer.create_account(account_type=AccountType.SAVINGS)
    customer2.add_bank_account(account=account)

    account.transfer_money(pay_to_account=account2, amount=1000)

    account.transfer_money(pay_to_account=account2, amount=100)

    print(f"Account statement of {account=}")
    account.account_statement()
    print(account.balance)

    print(f"Account statement of {account2=}")
    account2.account_statement()
    print(account2.balance)