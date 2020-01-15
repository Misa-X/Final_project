# import classes that are in the other files to use in Admin class
from .Account import Account
from .Customer import Customer
from .Users import User


class Admin(User):

    def __init__(self,username, password):
        super().__init__(username, password)

    def createAccount(self,list):
        first_name = input("Enter First Name >> ").lower()
        last_name = input("Enter Last Name >> ").lower()
        username = input("Enter Username >>").lower()
        password = input("Enter Password >> ")

        accnt = Account(0)
        ini = Customer(username, password)  # instantiating(making instance of a class)
        # using setter functions to set attributes of instance ini
        ini.setAccount(accnt)
        ini.setfirstName(first_name)
        ini.setlastName(last_name)
        ini.setpassword(password)
        list[username] = ini  # adding ini to the dict containing the customers
        print("Account Successfully created !")


    def closeAccount(self,list):
        username = input("Enter Customer Username >> ")
        ans = input("Are you sure you want to close this account ? (Y/N) >> ").upper()
        if ans == "Y":
            try:
                del list[username]
            except KeyError:
                print("Account not found")

            print("Account successfully closed !")

        else:
            print("Operation Aborted ! ")



    def viewAccounts(self,list):

        cusName = input("Enter Customer Username >> ")
        if cusName in list.keys():
            cust1 = list[cusName]
            print("First Name >> ", cust1.getfirstName())
            print("Last Name >> ", cust1.getlastName())
            print("Account Balance >> ", cust1.getAccount().getbalance())
            print("Customer Username >> ", cust1.getusername())
        else:
            print("Customer not in the database !! ")


    def numberUsers(self,list):
             print("The total Number of Customers is >> ", len(list))


