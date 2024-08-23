'''def primenumber():
    n=int(input('enter a number:'))
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                print('not a prime number')
                break
        else:
            print('prime number')
    else:
        print('not a prime number')
for i in range(1,11):
    primenumber()   
    
    
    
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
def evennumbers(ll,ul):
    for n in range(ll,ul+1):
        if iseven(n):
            print(n)
evennumbers(1,10)


def primenumbers():
    for n in range(ll,ul+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n) 
ll=int(input('enter a lower limit:'))
ul=int(input('enter a upper limit:'))
primenumbers()



#printing the poliprime numbers in given range

def ispolindrome(n):
    d=n
    s=0
    while d>0:
        r=d%10
        s=s*10+r
        d=d//10
    if n==s:
        return True
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def poliprime():
    for n in range(ll,ul+1):
        if ispolindrome(n) and isprime(n):
            print(n)
ll=int(input('enter a lower limit:'))
ul=int(input('enter a upper limit:'))
poliprime()


#printing emirp numbers in given range
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def polindrome(n):
    d=n
    reverse=0
    while d>0:
        r=d%10
        reverse=reverse*10+r
        d=d//10
    if n==reverse:
        return True
    else:
        return False
def reverse(n):
    d=n
    rev=0
    while d>0:
        r=d%10
        rev=rev*10+r
        d=d//10
    return rev
def emirpnumber():
    for n in range(ll,ul+1):
        rev=reverse(n)
        if isprime(n) and not polindrome(n) and isprime(rev):
            print(n)
ll=int(input('enter a lower limit:'))
ul=int(input('enter a upper limit:'))
emirpnumber()

#printing armstrong numbers in  a given range
def isarmstrong(n):
    d=n
    s=0
    l=len(str(n))
    while d>0:
        r=d%10
        s+=r**l
        d=d//10
    if n==s:
        return True
    else:
        return False
def armstrongnumber():
    for n in range(ll,ul+1):
        if isarmstrong(n):
            print(n)
ll=int(input('enter a lower limit:'))
ul=int(input('enter a upper limit:'))
armstrongnumber()

    
    
def sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum(n//10)
n=int(input('enter a number:'))
print(sum(n))

add=lambda x,y:x+y
print(add(10,20))


def multiply(n):
    return n*10
print(list(map(multiply,l)))


l=[10,20,30,40]
print(list(map(lambda n:n*10,l)))


l=['1','2','3','4']
nl=[]
for i in l:
    k=int(i)
    nl.append(k)
print(nl)

l=['1','2','3','4']
print(list(map(int,l)))

l=(list(map(int,input().split( ))))
print(l)

l=[1,3,4,6,7]
print(list(filter(lambda n:n%2==0,l)))

l=[1,2,3,6,5,2]
import functools
print(functools.reduce(lambda x,y:x if x>y else y,l))

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('enter a number:'))
print(factorial(n))


def sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum(n//10)
n=int(input('enter a number: '))
print(sum(n))

#opps  // defining a generic and specific properties 

class Bank():
    bank_name='kotak'
    bank_ifsc=1234
    bank_rai=5
    bank_address='Bangalore'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
raj=Bank('rajendra',98765,10000,'Chittoor')
kiran=Bank('kiran kumar',656786,20000,'piler')
hari=Bank('Harish',856,30000,'nellore')
print(kiran.bank_ifsc)
print(raj.name)
print(kiran.balance)
print(kiran.address)
print(raj.balance)
print(Bank.bank_address)'''


'''s=input('enter a string:')
l=0
for i in s:
    l+=1
print(l)'''


s='dlrow olleH'
print(s[::-1])
































    

