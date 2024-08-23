'''i=0
while i<=10:
    print(f'5*{i}={5*i}')
    i+=1'''

#WAP to check the given string is polindrome or not withot using slocing
'''s=input('enter astring')
s1=''
for i in s:
    s1=i+s1
print(s1)
if s==s1:
    print('polindrome')
else:
    print('not a polindrome')'''
#angram strings without using sorted merhod
'''
s1=input()
s2=input()
l1=[]
l2=[]
for i in s1:
    l1.append(i.lower())
    l1.sort()
for j in s2:
    l2.append(j.lower())
    l2.sort()
print(l1)
print(l2)
if l1==l2:
    print('angrams')
else:
    print('not a angrams')

#checking login deatailsof user like user name and login deatails
d={'username':'rajendra','password':'asifa'}

username=input('enter a user name')
if d['username']==username:
    password=input('enter a password')
    if d['password']==password:
        print('login successfully')
    else:
        print('invalid credentials')
else:
    print('invalid details')'''

'''
l=[1,2,3,4,5,6,7,8,9,0]
for i in range(len(l)):
    if l[i]%2==0:
        l[i]='even'
    else:
        l[i]='odd'
print(l)'''


'''
#factorial of number by using while loop
n=int(input('enterv a number:'))
fact=1
i=1
while n>=i:
    fact*=i
    i+=1
print(fact)'''
''''

#replace in place of vowels with the their index positions

s=input('enter a string:')
v='AEIOUaeiou'
s1=''
for i in range(len(s)):
    if s[i] in v:
        s1+=str(i)
    else:
        s1+=s[i]
print(s1)'''


'''
n=int(input('enter how many numbers you want:'))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,end=',')
    print(b)
else:
    print(a,b,end=',')
    for i in range(n-2):
        c=a+b
        print(c,end=',')
        a,b=b,c'''

'''
#fibonaci series
a=int(input('enter a value:'))
b=int(input('enter b value:'))
n=int(input('enter how many numbers you want:'))
if n==1:
    print(a)
elif n==2:
    print(a,end=',')
    print(b)
else:
    print(a,end=',')
    print(b,end=',')
    for i in range(n-2):
        c=a+b
        print(c,end=',')
        a,b=b,c'''
'''
*
  *
    *

n=int(input('enter how many rows you want:'))
for i in range(n):
    print('  '*i+'*')'''
'''
      *
    *
  *
*

n=int(input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1)+'*')
    
*   *
  *
*   *
#if n=3 only
n=int(input('enter how many rows you want:'))
for i in range(n):
    if i!=1:
        print('* '+'  '+'*')
    else:
        print('  '*i+'*')
* 
* * 
* * * 
* * * * 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print('* '*(i+1))


n=int(input())
for  row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input('enter how many rows you want:'))
for i in range(n):
    print((str(i+1)+' ')*n)
    


n=int(input('enter how many rows you want:'))

for i in range(n):
    k=1
    for j in range(n):
        print(k,end=' ')
        k+=1
    print()
1 
2 2 
3 3 3 
4 4 4 4 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print((str(i+1)+' ')*(i+1))

1 
2 3 
4 5 6 
7 8 9 10 

n=int(input('enter how many rows you want:'))
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=' ')
        k+=1
    print()


    1 
  2 3 
4 5 6 

1 2 3 4 
2 4 6 8 
3 4 5 6 
4 6 8 10 
n=int(input('enter how many rows you want:'))
k=1
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(k,end=' ')
        k+=1
    print()

1 2 3 4 
2 4 6 8 
3 4 5 6 
4 6 8 10 

n=int(input('enter how many rows you want:'))
for i in range(n):
    k=i+1
    for j in range(n):
        if (i+1)%2!=0:
            print(k,end=' ')
            k+=1
        else:
            print(k,end=' ')
            k+=2
    print()
    

1 2 3 4 5 
6 5 4 3 
2 3 4 
5 4 
3

1 2 3 4 5 
6 5 4 3 
2 3 4 
5 4 
3
n=int(input('enter how many rows you want:'))
k=1
for i in range(n):
    for j in range(n-i):
        if (i+1)%2!=0:
            print(k,end=' ')
            k+=1
        else:
            print(k,end=' ')
            k-=1
    print()'''

'''
n=int(input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1),end='')
    m=1
    k=i+1
    for j in range(2*i+1):
        d=j+1
        print(m,end=' ')
        if d<=m//2:
            m+=1
        else:
            m-=1
    print()

    
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 

n=int(input('enter how many rows you want:'))
col=1
for i in range(1,n+1):
    print('  '*(n-i),end='')
    k=0
    for j in range(1,col+1):
        if (i>=j):
            k+=1
        else:
            k-=1
        print(k,end=' ')
    print()
    col+=2

1
  3
    5
      7
    6
  4
2

n=int(input('enter how many rows you want:'))
k=1
m=6
for i in range(n):
    print(('  '*i)+str(k))
    k+=2
for j in range(n-1):
    print(('  '*(n-j-2))+str(m))
    m-=2


n=int(input('enter how many rows you want:'))

for i in range(n):
    d=i+1
    k=64
    for j in range(n+1):
        print(chr(k+d),end=' ')
        if d%2!=0:
            k+=1
        else:
            k+=2
    print()

#finding all polodrome substrings in given string
def polindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
def string(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if polindrome(s[i:j+1]):
                print(s[i:j+1])
string('mamata')'''

'''
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
n=int(input('enter anumber:'))
print(sum(n))
#find sum of digits until sum is single digit

def sum_digits(n):
    d=n
    s=0
    while d>0:
        r=d%10
        s+=r
        d=d//10
    return s
n=int(input('enter a number:'))
sum=sum_digits(n)
while sum>9:
    sum=sum_digits(sum)

print(sum)

l=['1','2','3','4','5']
print(tuple(map(int,l)))


print(list(map(int,input().split())))'''
'''

#opps:-


class Bank():
    bank_name='KOTAK'
    bank_roi=5
    bank_ifsc=12345
    bank_address='bangalore'
rajendra=Bank()
kiran=Bank()
#accesing of generic properties by using class
print(Bank.bank_name)
#accesing of generic properties by using object
print(rajendra.bank_roi)
Bank.bank_roi=8
print(Bank.bank_roi)
kiran.bank_ifsc=98876
print(kiran.bank_ifsc)
Bank.bank_mobile=8897628414
print(Bank.bank_mobile)
print(rajendra.bank_mobile)

#specific properties
class Bank():
    bank_name='KOTAK'
    bank_roi=5
    bank_ifsc=12345
    bank_address='bangalore'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
rajendra=Bank('prasad',889762,10000,'chittoor')
kiran=Bank('kumar',38735976,20000,'piler')
print(rajendra.name)
print(Bank.name)




#Bank application

class Bank():
    bank_name='KOTAK'
    bank_roi=5
    bank_ifsc=12345
    bank_address='bangalore'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of customer is {self.name}')
        print(f'account number of customer is {self.account}')
        print(f'balance of customer is {self.balance}')
        print(f'address of customer is {self.address}')
    def withdraw(self):
        amount=int(input('enter how much amount you want to withdrw'))
        if self.balance>=amount:
            self.balance-=amount
            print('successfully withdrawal completed')
            print(f'your cuurent balance is {self.balance}')
        else:
            print('insufficient banlance')
            print(f' your available balance is {self.balance}')
    def deposite(self):
        amount=int(input('enter money how much your going to deposite in to your account'))
        if amount>0:
            self.balance+=amount
            print(f'your cuurent balance is {self.balance}')
        else:
            print('enter amount more than zero(0)')
rajendra=Bank('prasad',889762,10000,'chittoor')
kiran=Bank('kumar',38735976,20000,'piler')
#rajendra.customer_details()
#kiran.customer_details()
#rajendra.withdraw()
kiran.deposite()'''

'''
#decorators
def outer(arg):
    print('outer function is started')
    print(arg)
    def inner():
        print('inner function  is started')
        arg()
        print('inner function id ended')
    print('outer function is ended')
    return inner
@outer
def wish():
    print('wish function is started')
    print('wish fuction is ended')
wish()


#method overriding

class Bank_v1():
    bank_name='SBI'
    bank_ifsc=12345
    bank_roi=4
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of customer is {self.name}')
        print(f'account of customer is {self.account}')
        print(f'balance of customer is {self.balance}')
        print(f'address of customer is {self.address}')
    @staticmethod
    def get_int_value():
        int_value=int(input('enter a int value'))
        return int_value
    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print('withdraw successfully completed ')
            print(f'your balance is {self.balance}')
        else:
            print('insufficient balance')
            print(f'your balance is {self.balance}')
class Bank_v2(Bank_v1):
    bank_address='bangalore'
    bank_mobile=8897628414
    def __init__(self,n,ac,b,ad,p,a):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
        self.pin=p
        self.age=a
    def customer_details(self):
        print(f'name of customer is {self.name}')
        print(f'account of customer is {self.account}')
        print(f'balance of customer is {self.balance}')
        print(f'address of customer is {self.address}')
        print(f'pin of customer is {self.pin}')
        print(f'age of customer is {self.age}')
    @classmethod
    def bank_details(cls):
        print(f'name of bank is {cls.bank_name}')
        print(f'ifsc of bank is {cls.bank_ifsc}')
        print(f'roi of bank is {cls.bank_roi}')
        print(f'address of bank is {cls.bank_address}')
        print(f'mobile of bank is {cls.bank_mobile}')
    def withdraw(self):
        pin=self.get_int_value()
        if self.pin==pin:
            amount=self.get_int_value()
            if self.balance>=amount:
                self.balance-=amount
                print('withdraw successfully completed ')
                print(f'your balance is {self.balance}')
            else:
                print('insufficient balance')
                print(f'your balance is {self.balance}')
        else:
            print('incorrect pin')
    @classmethod
    def modify_roi(cls):
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print(f' modified bank roi is {cls.bank_roi}')
        print('bank roi is succussfully madified')
raj=Bank_v2('rajendra',98745,20000,'chittoor',2022,21)
raj.bank_details()
#raj.withdraw()
raj.customer_details()
print(Bank_v1.bank_roi)
#print(Bank_v2.bank.roi)
Bank_v2.modify_roi()    
        
#chaining along with method ovrriding

class Bank_v1():
    bank_name='SBI'
    bank_ifsc=12345
    bank_roi=4
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_details(self):
        print(f'name of customer is {self.name}')
        print(f'account of customer is {self.account}')
        print(f'balance of customer is {self.balance}')
        print(f'address of customer is {self.address}')
    @staticmethod
    def get_int_value():
        int_value=int(input('enter a int value'))
        return int_value
    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print('withdraw successfully completed ')
            print(f'your balance is {self.balance}')
        else:
            print('insufficient balance')
            print(f'your balance is {self.balance}')
class Bank_v2(Bank_v1):
    bank_address='bangalore'
    bank_mobile=8897628414
    def __init__(self,n,ac,b,ad,p,a):
        #super().__init__(self,a,ac,ad)
        Bank_v1.__init__(self,a,ac,ad)
        self.pin=p
        self.age=a
    def customer_details(self):
        #super().customer_details()
        Bank_v1.customer_details(self)
        print(f'pin of customer is {self.pin}')
        print(f'age of customer is {self.age}')
    @classmethod
    def bank_details(cls):
        print(f'name of bank is {cls.bank_name}')
        print(f'ifsc of bank is {cls.bank_ifsc}')
        print(f'roi of bank is {cls.bank_roi}')
        print(f'address of bank is {cls.bank_address}')
        print(f'mobile of bank is {cls.bank_mobile}')
    def withdraw(self):
        pin=self.get_int_value()
        if self.pin==pin:
            amount=self.get_int_value()
            if self.balance>=amount:
                self.balance-=amount
                print('withdraw successfully completed ')
                print(f'your balance is {self.balance}')
            else:
                print('insufficient balance')
                print(f'your balance is {self.balance}')
        else:
            print('incorrect pin')
    @classmethod
    def modify_roi(cls):
        new_roi=cls.get_int_value()
        cls.bank_roi=new_roi
        print(f' modified bank roi is {cls.bank_roi}')
        print('bank roi is succussfully madified')
        
raj=Bank_v2('rajendra',98745,20000,'chittoor',2022,21)
raj.bank_details()
raj.customer_details()


#TCS question 

n=int(input('enter a number:  '))
if n>=0:
    s=str(n)
    se=0
    so=0
    l=[]
    m=[]
    for i in s:
        k=int(i)
        if k%2==0:
            l.append(k)
            se+=k
        else:
            m.append(k)
            so+=k
    print('even numbers are ',end='')
    for j in l:
        print(j,end=' ')
    print()
    print('odd numbers are ',end='')
    for a in m:
        print(a,end=' ')
    print()
    print('sum of even numbers',se)
    print('sum of odd nembers',so)    
else:
    print('not a integer')'''
'''
l=[1,2,3,4,5,6]
print(' '.join(map(str,l)))'''

#by using user defined iterator printing the numbers of series
'''
class series:
    def __init__(self,fv,lv,up=1):
        self.fv=fv
        self.lv=lv
        self.updation=up
    def __iter__(self):
        print('__iter__is called')
        self.i=self.fv
        return self
    def __next__(self):
        print('__next__is called')
        if self.i<self.lv:
            dummy=self.i
            self.i+=self.updation
            return dummy
        raise StopIteration
s=series(1,5)
for k in s:
    print(k)'''


#printing Fibonacci series by using the custome iterator
'''
class Fibonacci:
    def __init__(self,a,b,n):
        self.a=a
        self.b=b
        self.n=n
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i<=self.n:
            dummy=self.a
            self.a=self.b
            self.b=dummy+self.a
            self.i+=1
            return dummy
        raise StopIteration
f=Fibonacci(2,3,10)
for k in f:
    print(k,end=' ')'''


#exception Handling
'''
print('start')
l=[11,22,33,44]
ip=int(input('enter a index postions of elemnet you wantin given list:'))
try:
    print('try block is stared')
    val=l[ip-1]
    print(val)
    divisor=int(input('enter a divisor:'))
    results=val/divisor
    print('try block is ended')
except Exception as e:
    print(e)
else:
    print(results)
print('end')'''


#exception handling by using raise keyword

'''
a=int(input())
b=int(input())
try:
    if b==0:
        raise ZeroDivisionError('we con not devide a number with zero')
except ZeroDivisionError as ze:
    print(ze)
else:
    print(a/b)'''


#assert keyword
'''
def power(n):
    assert isinstance(n,int),'n should be integer'
    return n**2
try:
    print(power(3))
except AssertionError as e:
    print(e)'''
'''
#json date with dumps
with open('raj.txt','w') as fo:
    import json
    po={'name':'rajendra','age':21,'mobile':89775,'male':True,'female':False,'gf':'yes'}
    jo=json.dumps(po)
    fo.write(jo)
    print(po)
    print(jo)
    


    
#json data eith dump function
    
with open('prasad.txt','w') as fo:
    import json
    po=po={'name':'rajendra','age':21,'mobile':89775,'male':True,'female':False,'gf':'yes'}
    jo=json.dump(po,fo)
print(po)
print(fo)'''

#sql connection by using python
'''
import sqlite3
def connectionobject():
    import sqlite3
    connobj=sqlite3.connect('rajendra.db')
    return connobj
connobj=connectionobject()
def create_table(connobj):
    cursorobject=connobj.cursor()
    cursorobject.execute('create table emp(id integer primary key,name text)')
    connobj.commit()
    print('table is successfully created')
create_table(connobj)'''






'''
s=[1,2,3,4,5,5,2,3,4,5,3,3,9]
d={}
for i in s:
    d[i]=s.count(i)
print(d)
mx=max(d.values())

for k,v in d.items():
    if v==mx:
        print(k,v)'''
'''

s=input('enter string:')
s1=input('enter substring:')
c=0
for i in range(len(s)):
    if s[i:i+len(s1):]==s1:
        c+=1
print(c)'''

'''
s=input('enter a string:')
v='AEIOUaeiou'
s1=''
for i in range(len(s)):
    if s[i] in v:
        s1+=str(i)
    else:
        s1+=s[i]
print(s1)'''

#n times taking input from thr  user
'''
n=int(input('enter a how many numbers you want:'))
l=[]
for i in range(1,n+1):
    value=int(input('enter a value:'))
    l.append(value)
print(l)'''

#printing prime numbers in given range by calling a function inside a for loop
'''
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                print(n ,':not  prime')
                break
        else:
            print(n,':prime')
    else:
        print(n,':not prime')
for  n in range(1,11):
    prime(n)'''

'''
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def sum_digits(n):
    d=n
    sum=0
    while d>0:
        r=d%10
        sum+=r
        d=d//10
    return sum
def replace_vowels(s):
    new=''
    v='aeiouAEIOU'
    for i in range(len(s)):
        if s[i] in v:
            k=i*100
            summ=0
            for n in range(1,k+1):
                if isprime(n):
                    summ+=n
            while summ>9:
                summ=sum_digits(summ)
            new+=str(summ)
        else:
            new+=s[i]
    print(new)
replace_vowels('harshad')'''

#redusing  a number into single digit
'''
def sum_digits(n):
    d=n
    sum=0
    while d>0:
        r=d%10
        sum+=r
        d=d//10
    return sum
n=int(input('enter a number:'))
summ=sum_digits(n)
while summ>9:
    summ=sum_digits(summ)
print(summ)'''


#finding a polimdrome strings in given string
'''

def polindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
def string(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if polindrome(s[i:j+1:]):
                print(s[i:j+1:],end=' ')
string('mamata')'''
'''
l=[2,3,6,7,8,9,10]
def prime(n):
    if n>0:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
print(list(filter(prime,l)))'''

'''
s=input('enter a string:')
d={}
for i in s:
    d[i]=s.count(i)
print(d)
max=max(d.values())
for k,v in d.items():
    if v==max:
        print('{',k,':',v,'}')'''

'''
s=input('enter a string:')
l=s.split()
d={}
for i in l:
    d[i]=len(i)
print(d)
max=max(d.values())
for k,v in d.items():
    if v==max:
        print(k)
        
s=input('enter a string:')
d={}
for i in s:
    if i  not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

l=[11,200,300,505,3,5,1]
for i in range(len(l)):
    n=l[i]
    if n>1:
        for j in range(2,n//2+1):
            if n%j==0:
                if n%2==0:
                    l[i]='even'
                else:
                    l[i]='odd'
                break
        else:
            l[i]='prime'
    else:
        l[i]='odd'
print(l)'''

#output:- ['prime', 'even', 'even', 'odd', 'prime', 'prime', 'odd']

#printing a prime numbers in your phone number
'''
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
n=int(input('enter a number:'))
d=n
c=0
l=[]
while d>0:
    r=d%10
    if isprime(r):
        l.append(r)
        c+=1
    d=d//10
print('prime numbers are:',l)
print('prime numbers in my phone number:',c)'''

'''
n=5
for i in range(n):
    print('  '*(n-i-1)+'*')
    for j in range(n):
        print('  '*i+'*')
print()'''
'''
1 2 3 4 5 
10 9 8 7 6 
11 12 13 14 15 
20 19 18 17 16 
21 22 23 24 25 

n=int(input('enter a number:'))

for i in range(n):
    k=(i+1)
    if k%2!=0:
        t=5*i+1
    else:
        t=5*(i+1)
    for j in range(n):
        print(t,end=' ')
        #if k  in [1,3,5]:
        if k%2!=0:
            t+=1
        else:
            t-=1
    print()'''
'''
n=798278427
def sum_digits(n):
    d=n
    s=0
    while d>0:
        r=d%10
        s+=r
        d=d//10
    return s
sum=sum_digits(n)
while sum>9:
    sum=sum_digits(sum)
print(sum)'''

'''
l=[2,3,5,6,8,9,7]
#output:- [3, 2, 6, 5, 9, 8]
''''''
for i in range(len(l)):
    if i%2!=0:
        l[i],l[i-1]=l[i-1],l[i]
print(l)
    '''
#output:- [9, 8, 6, 5, 3, 2]
'''

n=len(l)
for i in range(n//2):
    l[i],l[n-i-1]=l[n-i-1],l[i]

print(l)'''

#coverting of decimal number to binary number
'''
n=int(input('enter a number:'))
d=n
l=[]
while d>0:
    r=d%2
    l.append(r)
    d=d//2
print(l)
l.reverse()
print(l)
for i in l:
    print(i,end='')


l=[1,2,3,7,5,52]
l1=[]
for i in l:
    r=i%26
    if r==0:
        l1.append('Z')
    else:
        l1.append(chr(64+r))    
print(l)
print(l1)


#output:-['A', 'B', 'C', 'G', 'E', 'Z']
    
l=['A', 'B', 'C', 'D','X']
l1=[]
for i in l:
    k=ord(i)-64
    j=k+3
    r=j%26
    if r==0:
        l1.append('Z')
    else:
        l1.append(chr(64+r))
print(l)
print(l1)'''


#output=['D', 'E', 'F', 'G', 'A']
'''
l=['aa:1','b:12','ccc:121']
d={}
for item in l:
    key,values=item.split(':')
    d[key]=int(values)
print(d)'''

#output:-{'aa': 1, 'b': 12, 'ccc': 121}
'''
s='aaabbcda'
x=''
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        x=x+str(c)+s[i]
        c=1
x=x+str(c)+s[i+1]
print(x)'''

#output:-3a2b1c1d1a
'''
s='3a2b1c1b1a'
x=''
for i in range(len(s)):
    if s[i].isdigit():
        x+=(int(s[i])*s[i+1])
print(x)'''

#output:-aaabbcba

#singleton class

def singleton(arg):
    d={}
    def inner():
        if arg not in d:
            d[arg]=arg()
        return d[arg]
    return inner
@singleton
class vinayaka :
    def __init__(self):
        self.tickets=300
    def booking(self,n):
        
        if self.tickets>=n:
            self.tickets-=n
            print('your tickets succesfully booked')
            print(f'available tickets are {self.tickets}')
        else:
            print('insufficient tickets')
            print(f'available tickets are {self.tickets}')
rajendra=vinayaka()
rajendra.booking(100)

            
        



        
        
        





























































































        
