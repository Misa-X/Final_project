import json # import json allows me to work with json file where i stored all customers data
# import classes that are in the other files to be used in Bank class
from final_project.Customer import Customer
from final_project.Account import Account
from final_project.Admin import Admin

class Bank:

    def __init__(self):
        self.filename = "bank.json"
        self.CustomerList = Loadjson() # a dictionary of Customer objects(contains all the data from json)
        self.admin = None
        self.customer = None


    def adminChoice(self):
        status = True
        while status:  # infinite loop to loop until the user chooses to exit
            print("""\n
                       =====================================
                                 *** FNB BANK ***
                       =====================================
                              *** PICK YOUR CHOICE ***
                       =====================================
                               [1] Create Account
                               [2] Close Account
                               [3] View Accounts
                               [4] Get Number of Users
                               [5] Exit
                       *************************************
                                  """)
            choice = int(input(">>"))
            if choice == 1:
                self.admin.createAccount(self.CustomerList)
            elif choice == 2:
                self.admin.closeAccount(self.CustomerList)
            elif choice == 3:
                self.admin.viewAccounts(self.CustomerList)
            elif choice == 4:
                self.admin.numberUsers(self.CustomerList)
            elif choice == 5:
                self.savejson()  # save changes to the json file and exit
                status = False


    def customerChoice(self):
        status = True
        while status:
            print("""\n
                =====================================
                          *** FNB BANK ***
                =====================================
                      *** PICK YOUR CHOICE ***
                =====================================
                        [1] Deposit
                        [2] Withdraw
                        [3] Check Balance
                        [4] Transfer
                        [5] Exit
                *************************************
                           """)
            choice = int(input(">>"))
            if choice == 1:
                self.customer.account.deposit()
            elif choice == 2:
                self.customer.account.withdraw()
            elif choice == 3:
                self.customer.account.checkbalance()
            elif choice == 4:
                self.customer.account.transfer(self.CustomerList)
            elif choice == 5:
                self.savejson() # save changes to the json file and exit
                status=False

    def savejson(self):
        with open(self.filename, "w") as fp:
            fill = {}
            fill["bankname"] = "FNB Bank"
            fill["Customers"] = {}
            for username, data in self.CustomerList.items():
                fill["Customers"][username] = {
                    "Firstname": data.getfirstName(),
                    "Lastname": data.getlastName(),
                    "Pass": data.getpassword(),
                    "balance": data.getAccount().getbalance()
                }
            json.dump(fill, fp, indent=4)


    def login(self):
        status =True
        while status:
            print("\n\t\t\t\t=====================================================")
            print("\t\t\t\t*****************WELCOME TO FNB BANK*****************")
            print("\t\t\t\t=====================================================")

            print("""\n
                        =====================================
                                  *** FNB BANK ***
                        =====================================
                                 *** LOGIN AS : ***
                        =====================================
                                [1] Admin
                                [2] Customer
                                [3] Exit
                        *************************************
                                   """)
            loginInput = int(input(">> "))

            if 1 == loginInput:
                username = input("Enter username >>").lower()  # used lower() so if user uses capital letters wont give an error
                password = input("Enter password >>").lower()
                if username == "misa" and password == "xirinda":
                    self.admin = Admin("misa","xirinda")
                    self.adminChoice()
                else:
                    print("wrong admin credentials")
            elif 2 ==loginInput:
                username = input("Enter username >> ")
                password = input("Enter password >> ")
                if username in self.CustomerList.keys():
                    self.customer = self.CustomerList[username]
                    if self.customer.password == password:
                        self.customerChoice()
                    else:
                        print("wrong password")
                else:
                    print("username not found")

            elif 3 == loginInput:
                print("\t*** Thank you for choosing our bank ***")
                status = False

            else:
                print("Please choose between the options given!")
                self.login()



def Loadjson():
    with open("bank.json", "r") as f:
        fill = json.load(f)
        CustomerList = {}
        print(fill)
        for key, value in fill["Customers"].items():
            cust1 = Customer(value["Firstname"], value["Pass"])# put the same parameters as in the init method for Customer class
            ac = Account(value["balance"])
            cust1.setAccount(ac)
            cust1.setfirstName(value["Firstname"])
            cust1.setlastName(value["Lastname"])
            CustomerList[key] = cust1

        return CustomerList

Loadjson()
b1 = Bank()  # assign Bank() to b1

b1.login()  # use b1 to refer to every method in Bank()
b1.savejson()
