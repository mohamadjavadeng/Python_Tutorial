class User():
    NumberOfUsers = 0
    def __init__(self, ID, name, age, gender):
        self.ID = ID
        self.name = name
        self.age = age
        self.gender = gender
    
    def personal_info(self):
        print("Personal information:")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Bank(User):
    bankUser = 0
    def __init__(self, ID, name, age, gender,pin):
        super().__init__(ID, name, age, gender)
        Bank.addUser()
        self.pin = pin
        self.accontID = "290038"+str(Bank.bankUser)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")
        return self.balance
    
    def viewBalance(self):
        print("Balance: "+str(self.balance))

    def account_info(self):
        print("Personal information:")
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Account ID: {self.accontID}")
        print(f"Balance: ${self.balance}")

    @classmethod
    def addUser(cls):
        cls.bankUser += 1



if __name__ == '__main__':
    user1 = Bank(12, "MJ", 30, "Male")
    user1.account_info()

    user2 = Bank(14, "Donya", 31, "female")
    user2.account_info()