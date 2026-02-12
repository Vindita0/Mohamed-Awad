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
                continue
            password = input("Enter the password: ")
            if password in self.accounts.items():
                print("The password is exist already, change it.")
                sleep(2)
                continue
            try:
                balance = int(input("Enter the Balance: "))
                break
            except ValueError:
                print("Invalid input, try again.")
                sleep(2)
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
new = System()
new.create()
new.deposit()
print(new.accounts)