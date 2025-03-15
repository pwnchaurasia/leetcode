from march_Job_hunt.lld.Splitwise.enums import SplitTypeEnum

class EqualSplit:

    @staticmethod
    def split_equally(amount, members):
        count = len(members)
        each_share = amount/count
        return each_share



class UnEqualSplit:

    @staticmethod
    def split_equally(amount, members):
        count = len(members)
        each_share = amount/count
        return each_share

class PercentageSplit:
    @staticmethod
    def split_equally(amount, members):
        count = len(members)
        each_share = amount / count
        return each_share

class SplitFactory:

    @staticmethod
    def factory(split_type):
        if split_type == SplitTypeEnum.EQUAL:
            return EqualSplit()
        elif split_type == SplitTypeEnum.UNEQUAL:
            return UnEqualSplit()
        elif split_type == SplitTypeEnum.PERCENTAGE:
            return PercentageSplit()


class Expense:
    def __init__(self, group, amount, paid_by, split_type=SplitTypeEnum.EQUAL):
        self.group = group
        self.amount = amount
        self.split_type = split_type


    def add_expense(self, amount, members,):
        factory = SplitFactory.factory(split_type=self.split_type)
        pass

