from abc import ABC, abstractmethod
from enums.account_status import AccountStatus


class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        None