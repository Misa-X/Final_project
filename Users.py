
class User:
    def __init__(self,username, password): # to accept only 2 arguments, no need to initialize every instance with all those arguments
        self.first_name = ""
        self.last_name = ""
        self.username = username
        self.password = password

    def getfirstName(self):
        return self.first_name

    def getlastName(self):
        return self.last_name

    def getusername(self):
        return self.username

    def getpassword(self):
        return self.password

    def setfirstName(self, first_name):
        self.first_name = first_name

    def setlastName(self, last_name):
        self.last_name = last_name

    def setusername(self, username):
        self.username = username

    def setpassword(self, password):
        self.password = password

