# Importing account module from banking_pkg file.
from banking_pkg import account

# The menu for the atm once you login


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# Prints ATM heading.
print("\n          === Automated Teller Machine ===          ")

# Loop to get username for registration.
while True:
    name = input("Enter name to register: ")
    if len(name) <= 10 and len(name) >= 1:
        break
    else:
        print("The maximum name length is 10 characters")

# Loop to get pin for registration.
while True:
    pin = input("Enter PIN: ")
    if len(pin) == 4:
        break
    else:
        print("The pin must be exactly 4 numbers")

# Sets starting balance to zero.
balance = str(0)

# Displays succesful registrstion.
print(name, "has been registered with a starting balance of $" + balance)

# Loop to login and validate information.
while True:
    print("\n          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

# Loop to choose an option from the atm menu once you login.
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
