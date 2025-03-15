

class Group:
    GROUPS = []
    def __init__(self, group_name, owner):
        self.group_name = group_name
        self.owner = owner
        self.members = []

    def create_group(self):
        self.GROUPS.append(self)

    def add_members(self, user):
        self.members.append(user)