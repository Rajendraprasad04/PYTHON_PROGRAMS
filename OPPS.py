'''class Bank():
    bank_name='SBI'
    bank_ifsc=1234
    bank_roi=6
    bank_address='kizikistan'
rajendra=Bank()
kiran=Bank()
print(Bank.bank_name)
print(rajendra.bank_name)
print(kiran.bank_name)
Bank.bank_roi=5
print(rajendra.bank_roi)
rajendra.bank_ifsc=4325
print(rajendra.bank_ifsc)
rajendra.bank_mobile=9182323
print(rajendra.bank_mobile)

class Bank():
    bank_name='SBI'
    bank_roi=5
    bank_ifsc=1234
    bank_address='kizikistan'
    def __init__(self,n,a,b,ad):
        self.name=n
        self.age=a
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of the custemer {self.name}')
        print(f'age of the custemer {self.age}')
        print(f'balance of the custemer {self.balance}')
        print(f'address of the custemer {self.address}')
deva=Bank('devaraj',20,10000,'bangalore')
harish=Bank('harish',24,20000,'chennai')
deva.customer_details()
harish.customer_details()
print(deva.name)
print(harish.address)


class Bank():
    bank_name='SBI'
    bank_roi=5
    bank_ifsc=1234
    bank_address='kizikistan'
    def __init__(self,n,a,b,ad):
        self.name=n
        self.age=a
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of customer {self.name}')
        print(f'age of customer {self.age}')
        print(f'balance of customer {self.balance}')
        print(f'address of customer {self.address}')
    def withdraw(self):
        amount=int(input('enter amount how much you want:'))
        if self.balance>=amount:
            self.balance-=amount
            print('successfully your amount withdrwan ')
            print(f'balance of customer {self.balance}')
        else:
            print('insufficient amount or funds')
            print(f'balance of customer {self.balance}')
    def deposite(self):
        amount=int(input('enter a amount:'))
        if amount>0:
            self.balance+=amount
            print(f'balance of customer {self.balance}')
            print('your deposite is done')
        else:
            print('enter amount more than 0')
raj=Bank('rajendra',21,10000,'bangalore')
minnu=Bank('chandini',20,20000,'chittoor')
raj.customer_details()
minnu.customer_details()
Bank.customer_details(raj)
raj.withdraw()
minnu.deposite()'''

def outer(arg):
    print('outer is started')
    print(arg)
    def inner():
        print('inner function is started')
        print(arg)
        print('inner function is defined')
    print('outer function is defined')
    return inner
@outer
def wish():
    print('wish function is started')
    print('wish function is ended')
wish()
                   
    






















































































