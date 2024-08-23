'''
00000000010
000000009
00000008
0000007
000006
00005
0004
003
02
1

n=int(input('enter how many rows you want:'))
k=n
for i in range(n):
    print((str(0)+'')*(n-i-1)+str(k))
    k-=1'''

'''
n=int(input('enter a number:'))
l=len(str(n))
sum=0
if l>1:
    d=n
    while d>0:
        r=d%10
        sum+=r
        d=d//10
    if sum>7:
        print('True')
    else:
        print('False')

A=input('enter first string:')
B=input('enter a second string:')
result=A.endswith(B)
print(result)

A=input('enter a  first number:')
B=input('enter a second number:')
for i in range(len(A)):
    for j in range(len(B)):
        if i==0 and j==len(B)-1:
            if int(A[i])<int(B[j]):
                print('True')
            else:
                print('False')
                


s=input('enter a string:')
n=int(input('enter a number:'))
if n>1:
    if s[0:n:]==s[(len(s)-n)::]:
        print('True')
    else:
        print('false')
else:
    print('False')'''
'''
n=int(input('enter a number:'))

if 2<=n<=10:
    l=list(map(int,input('enter a list:').split()))
    max=max(l)
    k=l.count(max)
    for i in range(k):
        l.remove(max)
    maxx=0
    for i in l:
        if i>maxx:
            maxx=i
    print(maxx)
#else:
   # print('enter a number greater than 1 and below 11')
    


n=int(input())
l=[]
for i in range(n):
    names=input()
    marks=int(input())
    a=[names,marks]
    l.append(a)
print(l)    
d={}
for i in l:
    d[i[0]]=i[1]
print(d)
for j,k in d.items():
    
    



n=int(input('enter a number:'))
l=[]
g=[]
for i in range(n):
    names=input('enter name:')
    grades=eval(input('enter grades:'))
    l.append([names,grades])
    g.append(grades)
#print(l)
list=list(set(g))
a=list.sort()
print(a)

for i in l:
    if i[1]==sec:
        print(i[0])'''


def reverse(x):
    d=abs(x)
    rev=0
    while d>0:
        r=d%10
        rev=rev*10+r
        d=d//10
    return rev
x=int(input())

if x>0:
    print(reverse(x))
else:
    print(f'-{reverse(x)}')


       



            
        
        
