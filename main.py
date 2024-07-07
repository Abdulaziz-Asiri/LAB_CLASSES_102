from bankAccount import *
from art import *
from colorama import *
from numpy import *
account1 = BankAccount("Ali")
account2 = BankAccount("khalid")

print(account1.get_balance())
print(account1.deposit(15))
print(account1.withdraw(10))
print(account1.get_balance())
print(account1.get_account_holder())
print(account1.get_account_number())
print(Fore.BLUE+account2.get_account_number())