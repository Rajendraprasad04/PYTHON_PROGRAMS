'''s=input('enter a string:')
v='aeiouAEIOU'
cv=0
cc=0
for i in s:
    if i.isalpha() and i in v:
        cv+=1
    if i.isalpha() and i  not in v:
        cc+=1
print(cv)
print(cc)

s=input('enter a string:')
ce=0
co=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ce+=k
        else:
            co+=k
print(ce)
print(co)
print(abs(ce-co))


s=input('enter a string:')
c=0
for i in s:
    if not i.isalnum():
        c+=1
print(c)

l=input('enter a list:')
s=0
for i in l:
    if i.isdigit():
        k=int(i)
        s+=k
print(s)


l=[1,2,49,20,90]
import funtools
print(funtools.reduce(lambda x,y:x if x>y else y,l))


l=eval(input('enter a list:'))
max=0
for i in l:
    if i>max:
        max=i
print(max)



ll=int(input('enter a lower limit: '))
ul=int(input('enter a upper limit: '))
sum=0
for n in range(ll,ul+1):
    sum+=n
print(sum)

#factorial of number
n=int(input('enter a number :'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#perfect number
n=int(input('enter a number :'))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
print(sum)
if sum==n:
    print('perfect number')
else:
    print('not a perfect number')

#even numbers in given range
ll=int(input('enter a lower limit: '))
ul=int(input('enter a upper limit: '))
c=0
for i in range(ll,ul+1):
    if i%2==0:
        c+=1
        if c%2!=0:
            print(i)
            
ll=int(input('enter a lower limit: '))
ul=int(input('enter a upper limit: '))
l=[]
for i in range(ll,ul+1):
    if i%2==0:
        l.append(i)
print(l)
print(l[::2])

#for loop with range and CDT
#ip of consonants
s='hello'
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip].isalpha() and s[ip] not in v:
        print(ip,'is index position of',s[ip])

# sum of integers
s=input('enter a string:')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        sum+=ip
print(sum)
# sum of even digits  present in odd ip

s=input('enter a string:')
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0 and ip%2==0:
            sum+=ip
print(sum)

s=input('enter a string:')
s1=input('enter a substring:')
c=0
for i in s:
    if i==s1:
        c+=1
print(c)

s=input('enter a string:')
s1=input('enter a substring:')
c=0
for ip in range (len(s)):
    if s[ip:ip+len(s1):]==s1:
        c+=ip
print(c)'''

l=eval(input('enter a list:'))
for ip in range (len(l)):
    if l[ip]%2==0:
        l[ip]='even'
    else:
        l[ip]='odd'
print(l)


















































