from Bank import Bank

account_dict = {}
ID_dict = {}
# Save Data in excel file for later use
def create_new_account():
    name = input("Enter the name of the customer: ")
    age = int(input("Enter the age of the customer: "))
    gender = input("Enter the gender of the customer: ")
    ID = input("Enter the ID of the customer: ")
    initial_deposit = float(input("Enter the initial deposit: "))
    while initial_deposit <= 0.0:
        print("invalide the initial deposit, Please enter a positive number or \"q\" to quit")
        data = input()
        if data == "q":
            return
        else:
            initial_deposit = float(data)
    pin = input("Enter the PIN number: ")
    user = Bank(ID, name, age, gender, pin)
    user.deposit(initial_deposit)
    account_dict[user.accontID] = user
    ID_dict[user.ID] = user.accontID
    print(f"Account created for {user.name} with accountID {user.accontID}")


def login():
    accountID = input("Enter the accountID:")
    accountPin = input("Enter the PIN number:")
    if accountID in account_dict.keys() and accountPin == account_dict[accountID].pin:
        print(f"Welcome {account_dict[accountID].name}")
    else:
        print("Invalid accountID or PIN")
        return
    while True:
        inputVal = int(input("""Enter 1 for deposit
        2 for withdraw
        3 for view balance
        4 for logout
        5 for change PIN
        6 for transfer money:"""))
        if inputVal == 1:
            amount = float(input("Enter the amount to deposit: "))
            account_dict[accountID].deposit(amount)
        elif inputVal == 2:
            amount = float(input("Enter the amount to withdraw: "))
            account_dict[accountID].withdraw(amount)
        elif inputVal == 3:
            account_dict[accountID].viewBalance()
        elif inputVal == 4:
            return
        elif inputVal == 5:
            accountPin = input("Enter the new PIN number: ")
            account_dict[accountID].pin = accountPin
            return
        elif inputVal == 6:
            accountID_transfer = input("Enter the accountID of the customer: ")
            if accountID_transfer in account_dict.keys():
                amount = float(input("Enter the amount to transfer: "))
                if amount > account_dict[accountID].balance:
                    account_dict[accountID].withdraw(amount)
                    account_dict[accountID_transfer].deposit(amount)
                else:
                    print("Insufficient funds")
            else:
                print("Invalid accountID")
        else:
            print("Invalid input, please try again")
    


if __name__ == '__main__':
    create_new_account()
    login()


