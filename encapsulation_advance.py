class BankUser:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Cannot set negative balance")
        else:
            self._balance = amount

    def add_funds(self, amount):
        if amount < 0:
            print("Cannot add negative funds")
        else:
            self._balance += amount
            print(f"Added {amount}. New balance: {self._balance}")

class Vault:
    def __init__(self, code):
        self.__code = code
    
    def unlock(self, attempt_code):
        if attempt_code == self.__code:
            print("Vault unlocked successfully!")
        else:
            print("Incorrect code. Access denied.")

class Car:

    __slots__ = ['make', 'year']    

    def __init__(self, make,year):
        self.make = make
        self.year = year
    
