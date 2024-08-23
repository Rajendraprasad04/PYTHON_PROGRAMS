'''

#exactly  we need to take input for the user
n=int(input('enter how many times input you want:'))
l=[]
for i in range(n):
    value=eval(input('enter a value:'))
    l.append(value)
print(l)


#W A P to print intergers values and add it to the list
#until the given number is negative

l=[]
while True:
    v=int(input('enter value:'))
    if v>=0:
        l.append(v)
    else:
        break
print(l)

#WAP to print first  15 prime numbers
n=1
c=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n,end=',')
            c+=1
    if c==15:
        break
    n+=1
#output:-  2,3,5,7,11,13,17,19,23,29,31,37,41,43,47


#printing nth prime number
c=int(input('enter the number of prime number you want:'))
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
    if pc==c:
        print(n)
        break
    n+=1
#c=10
#output:  29


#WAP to print prime numbers from 6th to 10th

n=1
c=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            if c>=6 and c<=10:
                print(n)
    if c==10:
        break
    n+=1
    
#output:-
13
17
19
23
29
   '''


































































































    
        
