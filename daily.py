from time import sleep
from clear import clear
class System:
    def __init__(self):
        self.accounts = {}
    def create(self):
        while True:
            name = input("Enter the name: ")
            if name in self.accounts:
                print("This name is exist aleardy, change it")
                sleep(2)
                clear()
                continue
            while True:
                password = input("Enter the password: ")
                passwords = [self.accounts[i]["password"] for i in self.accounts]
                if password in passwords:
                    print("This password is here already, change it.")
                    sleep(2)
                    continue
                else:
                    break
            try:
                balance = int(input("Enter the Balance: "))
                break
            except ValueError:
                print("Invalid input, enter numbers only.")
                sleep(2)
                clear()
                continue
        self.accounts[name] = {"balance": balance,
                               "password": password}
    def deposit(self):
        ask_name = input("Enter the name of the account: ")
        ask_password = input("Enter the password: ")
        if ask_name in self.accounts and self.accounts[ask_name]["password"] == ask_password:
            while True:
                try:
                    dep = float(input("Enter the deposit balance: "))
                    if dep < 0:
                        print("Invalid input, enter number greater than or equal 0.")
                        sleep(2)
                        continue
                    break
                except ValueError:
                    print("Invalid input, try again.")
                    sleep(2)
                    continue
            self.accounts[ask_name]["balance"] += dep
        if ask_name not in self.accounts:
            print("There is no account like this name.")
            sleep(2)
        elif self.accounts[ask_name]["password"] != ask_password:
            print("The password not correct!")
            sleep(2)
    def withdraw(self):
        ask_name = input("Enter the name of the account: ")
        ask_password = input("Enter the password: ")
        if ask_name in self.accounts and self.accounts[ask_name]["password"] == ask_password:
            while True:
                try:
                    withdraw = float(input("Enter the number that you wanna withdraw: "))
                    if withdraw < 0:
                        print("Invalid input, enter number geater than or equal 0.")
                        sleep(2)
                        continue
                    if withdraw > self.accounts[ask_name]["balance"]:
                        print("The number override.")
                        print(f"Your balance is: {self.accounts[ask_name]["balance"]}")
                        sleep(2)
                        continue
                    break
                except ValueError:
                    print("Invalid input, try again.")
                    sleep(2)
                    continue
            print("Withdrawing...")
            sleep(2)
            self.accounts[ask_name]["balance"] -= withdraw
        if ask_name not in self.accounts:
            print("There is no account like this name.")
            sleep(2)
        elif self.accounts[ask_name]["password"] != ask_password:
            print("The password not correct!")
            sleep(2)
    def Display(self):
        ask_name = input("Enter the name of the account: ")
        ask_password = input("Enter the password: ")
        if ask_name in self.accounts and self.accounts[ask_name]["password"] == ask_password:
            print("Displaying...\n")
            sleep(2)
            print(f"Name: {ask_name.title()}")    
            print(f"Balance: {self.accounts[ask_name]["balance"]}")
            if self.accounts[ask_name]["balance"] < 100:
                print("Low balance warning.")
            print("-" * 30)
        if ask_name not in self.accounts:
            print("There is no account like this name.")
            sleep(2)
        elif self.accounts[ask_name]["password"] != ask_password:
            print("The password not correct!")
            sleep(2)
    def all_accounts(self):
        print("Displaying...\n")
        sleep(2)
        for i in self.accounts:
                    print(f"Name: {i.title()}")    
                    print(f"Balance: {self.accounts[i]["balance"]}")
                    if self.accounts[i]["balance"] < 100:
                        print("Low balance warning.")
                    print("-" * 30)
new = System()
while True:
    clear()
    print("Hello in the Bank System!")
    print("""
What are you need?
1.Create Account
2.Deposit
3.Withdraw
4.Show Balance
5.Show All Accounts
6.Exit
""")
    try:
        choice = int(input("Enter the number of your choice: "))
    except ValueError:
        print("Invalid input, try again.")
        sleep(2)
        continue
    if choice == 1:
        clear()
        new.create()
        print("Adding...")
        sleep(2)
    elif choice == 2:
        clear()
        new.deposit()
        print("Depositing...")
        sleep(2)
    elif choice == 3:
        clear()
        new.withdraw()
    elif choice == 4:
        clear()
        new.Display()
        nsk = input("Press Enter:")
    elif choice == 5:
        clear()
        new.all_accounts()
        nan = input("Pass Enter:")
    elif choice == 6:
        print("Happy to see you bay.")
        break
    else:
        print("Invalid input, please choice form the numbers above.")
        sleep(2)
        continue