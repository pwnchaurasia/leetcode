class Expense:
    def __init__(self, amount, description, payer, participants):
        self.amount = amount
        self.description = description
        self.payer = payer
        self.participants = participants

    def split_expense(self):
        """Splits the expense among participants and updates their balances."""
        split_amount = self.amount / len(self.participants)
        for participant in self.participants:
            if participant == self.payer:
                participant.balance += (self.amount - split_amount)
            else:
                participant.balance -= split_amount

    def __repr__(self):
        return f"Expense({self.description}, Amount: {self.amount}, Payer: {self.payer.name})"