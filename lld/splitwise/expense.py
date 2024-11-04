class Expense:
    def __init__(self, amount, description, payer, participants):
        self.amount = amount
        self.description = description
        self.payer = payer
        self.participants = participants  # List of User instances

    def __repr__(self):
        return f"Expense({self.description}, Amount: {self.amount}, Payer: {self.payer.name})"

