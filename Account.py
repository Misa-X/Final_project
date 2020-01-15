class Account:

    def __init__(self,balance):
        self.balance = balance

    def getbalance(self):
        return self.balance

    def setbalance(self, balance):
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit >> "))
        if amount > 0:
            self.balance += amount
            print("RP", amount, "has been deposited into your account !")
        else:
            print("Invalid Amount !")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw >> "))
        if amount < self.balance:
            self.balance -= amount
            print("Your balance is : ", self.balance)
        else:
            print("Unavailable amount !")


    def checkbalance(self):
        print("Your Balance is : ", self.balance)


    def transfer(self,list):
        print("Enter details of destination account")
        destName = input("Enter name >> ").lower()
        amount = float(input("Enter amount you want to transfer >>"))

        if amount > self.balance:
            print("Unavailable funds! ")

        else:
            self.balance -= amount
            if destName in list.keys():  # look for the name in list.keys
                Cust = list[destName]  # variable is equal to the customer object
                new_balance = Cust.account.balance + amount
                Cust.account.setbalance(new_balance)

            print(amount, "was successfully transferred to ", destName)
            print("Your Balance is : ", self.balance)
