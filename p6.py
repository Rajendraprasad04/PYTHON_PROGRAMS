'''n=int(input('enter a number: '))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)
#factorial of  given number
n=int(input('enter a number: '))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
#perfect number or not

n=int(input('enter a number: '))
sd=0
i=1
while i<n:
    if n%i==0:
        sd+=i
    i+=1
print(sd)
if n==sd:
    print(' perfect number')
else:
    print('not a perfect number')
#even numbers
ll=int(input('enter a lower limit'))
ul=int(input('enter a upper limit'))
i=ll
while i<=ul:
    if i%2==0:
        print(i)
    i+=1

l=eval(input('enter a list'))
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)

#replace vowels element with their index positions
s=input('enter a string:')
v='aeiouAEIOU'
for ip in range(len(s)):
    if ip in v:
        

list=eval(input('ente a list:'))
for ip in range(len(list)):
    if list[ip]%2==0:
        list[ip]='even'
    else:
        list[ip]='odd'
print(list)
#replace all digits with 'h'
s=input('enter a string:')
s1=''
for i in s:
    if i.isdigit():
        s1+='h'n                                          
    else:
        s1+=i
print(s1)
#polindrome number or not
n=int(input('enter a number'))
rev=0
dummy=n
while 0<dummy:
    rem=dummy%10
    rev=rev*10+rem
    dummy=dummy//10
print(rev)
if rev==n:
    print('polindrome')
else:
    print('not a polindrome')

n=int(input('enter a number'))
sum=0
dummy=n
l=len(str(n))
while 0<dummy:
    rem=dummy%10
    sum=sum+rem**l
    dummy=dummy//10
print(sum)
if sum==n:
    print('armstrong')
else:
    print('not a armstrong')

n=int(input('enter a number'))
sum=0
dummy=n
l=len(str(n))
while 0<dummy:
    rem=dummy%10
    sum=sum+rem**l
    dummy=dummy//10
    l-=1
print(sum)
if sum==n:
    print('disarium ')
else:
    print('not a disarium')

n=int(input('enter anumber'))
d=n
s=0
while 0<d:
    r=d%10
    s+=r
    d=d//10
print(s)
if n%s==0:
    print('harshad number')
else:
    print('not a harshad number')
    
#prime number or not

n=int(input('enter a number:'))
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=1
print(s)
if s>3:
    print('not a prime number')
else:
    print('prime number')
#prime number or not
n=int(input('enter a number'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(' not a prime number')
        else:
            print(' prime number')
else:
     print('not a prime number')

#fibonacci series
n=int(input('enter how many numbers you want: '))
a=int(input('enter a value: '))
b=int(input('enter b value: '))
if n==1:
    print(a)
elif n==2:
    print(a,end=' ')
    print(b)
else:
    print(a,b,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=' ')
        a,b=b,c
          
          

#fibonnaci series

a=0
b=1
n=int(input("enter the n value:"))
for i in range(1,n+1):
    c=a+b
    #l.append(c)
    print(c,end=' ')
    a,b=b,c
    

a=0
b=1
n=int(input("enter the n value:"))
for i in range(1,n+1):
    c=a+b
    #print(c,end=' ')
    a,b=b,c
    if i==5:
        print(c)
        break
for i in range(1,6):
    for j in range(1,6):
        if i==j and i+j==6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#prime numbers in given range
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
#perfect number in given range
ll=int(input('ll'))
ul=int(input('ul'))
for n in range(ll,ul+1):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    if s==n:
        print(n)
# armstrong numbers in given range
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    d=n
    s=0
    l=len(str(d))
    while d>0:
        r=d%10
        s=s+r**l
        d=d//10
    if s==n:
        print(n)'''
#disarium numbers in given range
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    d=n
    s=0
    l=len(str(n))
    while d>0:
        r=d%10
        s=s+r**l
        d=d//10
        l-=1
    if s==n:
        print(n)
# strong numbers in  given range
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    if n>0:
        d=n
        s=0
        while d>0:
            r=d%10
            fact=1
            for i in range(1,r+1):
                fact*=i
            s=s+fact
            d=d//10
        if s==n:
            print(n)
        
        
    


       
        




























    
        

