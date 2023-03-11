def show_balance(balance):
    print("Current Balance: $" + str(balance))


def deposit(balance):
    amount = (input("Enter amount to deposit: "))
    return (float(balance) + float(amount))


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if float(balance) < float(amount):
        print("You do not have the sufficient funds")
        return balance
    return (balance - float(amount))


def logout(name):
    print("Goodbye " + name + "!")
