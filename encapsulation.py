class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) / 1.8

class Lock:
    def __init__(self, pin):
        self.__pin = pin  

    def verify(self, input_pin):
        return input_pin == self.__pin
    
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Cannot set negative balance")
        else:
            self._balance = amount