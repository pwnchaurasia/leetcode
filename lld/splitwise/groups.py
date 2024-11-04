from lld.splitwise.expense import Expense


class Group:
    groups = []

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.members = [owner]
        self.expenses = []
        self.balances = {owner: 0}  # Tracks balance per user in the group
        Group.groups.append(self)
        # self.add_member(owner)

    def add_member(self, user):
        """Adds a user to the group."""
        if user not in self.members:
            self.members.append(user)
            self.balances[user] = 0

    def add_expense(self, amount, description, payer, participants):
        """Adds an expense and updates individual balances within the group."""
        if len(participants) == 1 and participants[0] == "all":
            participants = self.members
        expense = Expense(amount, description, payer, participants)
        self.expenses.append(expense)
        self.update_balances(expense)

    def update_balances(self, expense):
        """Splits the expense among participants and updates group balances."""
        split_amount = expense.amount / len(expense.participants)
        for participant in expense.participants:
            if participant == expense.payer:
                self.balances[participant] += (expense.amount - split_amount)
            else:
                self.balances[participant] -= split_amount
            participant.balance = self.balances[participant]

    def get_balance_report(self):
        """Returns the balance report for the group."""
        return {user.name: balance for user, balance in self.balances.items()}


    def __repr__(self):
        return f"Group({self.name}, Owner: {self.owner.name})"
