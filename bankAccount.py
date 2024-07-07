import random
import string
class BankAccount:
    usedAccountNumber = set()

    def __init__ (self, account_holder:str , initial_balance = 0 ):
        self.account_holder = account_holder
        self.__initialBalance = initial_balance 
        self.accountNumber = self.generateAccountNumber() 
                

    def generateAccountNumber (self):
        while True:
            account_number = ''.join(random.choices(string.digits, k=10))
            if account_number not in BankAccount.usedAccountNumber:
                BankAccount.usedAccountNumber.add(account_number)
                return account_number

    def deposit (self, depositMoney:int):
        self.__initialBalance = self.__initialBalance + depositMoney
        return self.__initialBalance

    def withdraw(self, withdrawMoney:int):
        if withdrawMoney > self.__initialBalance:
            raise Exception("Sorry, You are broke go to work!")
        self.__initialBalance = self.__initialBalance - withdrawMoney
        return self.__initialBalance

    def get_balance(self):
        return f"Your Balance is :{self.__initialBalance}"

    def get_account_holder(self):
        return f"Account holder name is : {self.account_holder}"
    def get_account_number(self):
        return f"Account number is :{self.accountNumber}"
