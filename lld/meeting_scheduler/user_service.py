from lld.meeting_scheduler.users import User


class UserService:

    @staticmethod
    def register_user(name, email, password):
        user = User(name=name, email=email, password=password)
        return True


    @staticmethod
    def remove_user(user):
        User.remove_user(user)

