from .Users import User


class Customer(User):

    def __init__(self,  username, password):
        super().__init__(username, password)
        self.account = None  # self.account is of data type Account

    def getAccount(self):
        return self.account

    def setAccount(self,account):
        self.account = account


