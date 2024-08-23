from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    def deposite(self):
        pass
    def balance(self):
        pass
class rajendra(ATM):
    def withdraw(self):
        print('withdraw the money')
    def deposite(self):
        print('deposite the money')
    def balance(self):
        print('check the balance')
R=rajendra()
R.withdraw()
R.deposite()
R.balance()
        