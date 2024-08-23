'''l=[1,2,'2',4,'hd','4']
s=0
for i in l:
    if isinstance(i,int):
        s+=i
print(s)
        
l=[1,2,2,4,5]
s=0
for i in l:
    s+=i
print(s)
n=int(input('enter a number:'))
i=0
s=0
while n>=i:
    s+=i
    i+=1
print(s)

s=input('kdjsaj:')
v='AEIOUaeiou'
rev=''
for ip in range(len(s)):
    if s[ip] in v:
        rev+=str(ip)
    else:
        rev+=s[ip]
print(rev)
class Book:
    def __init__(self,n,a,p):
        self.bname=n
        self.bauthor=a
        self.bprice=p
    def __add__(self,other):
        return self.bprice+other.bprice
    def __sub__(self,other):
        return self.bprice-other.bprice
python=Book('python','rajendra',100)
django=Book('django','karunakar',200)
print(python-django)
print(python+django)


n=int(input('enter a number:'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,' is not a polindrome')
            break
        else:
            print(f'{n} is a polindrome')
else:
    print(f'{n} is not a polindrome')


a=int(input('enter first number:'))
b=int(input('enter seconf d number:'))
n=int(input('enter how many nubers you want:'))
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



for i in range(1,6):
    for j in  range(1,6):
        print(i,j,end=' ')
        if j==3:
            break

ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)

ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    if n>0:
        s=0
        for i in range(1,n):
            if n%i==0:
               s+=i
        if n==s:
            print(n)

#print armstrong numbers in given range
ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    s=0                
    d=n
    l=len(str(n))
    while d>0:
        rem=d%10
        s=s+rem**l
        d=d//10
    if s==n:
        print(n)

#print disaium numbers in given range
ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    s=0                
    d=n
    l=len(str(n))
    while d>0:
        rem=d%10
        s=s+rem**l
        d=d//10
        l-=1
    if s==n:
        print(n)
#harshad numbers in given range
ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    s=0
    d=n
    while d>0:
        rem=d%10
        s=s+rem
        d=d//10
    if n%s==0:
        print(n)
#strong numbers in given range
ll=int(input('enter a ll limit:'))
ul=int(input('enter a ul limit:'))
for n in range(ll,ul+1):
    s=0
    d=n
    while d>0:
        rem=d%10
        d=d//10
        f=1
        for i in range(1,rem+1):
            f*=i
        s+=f
    if n==s:
        print(n)

n= int (input('enter how many rows you want:'))
for i in range(n):
    print('* '*n)

      *
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
n= int (input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1)+'* '*(2*i+1))
for i in range(n-1):
    print('  '*(i+1)+'* '*(2*(n-1)-2*i-1))

n= int (input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print('  '*(i+1)+'* '*(n-i-1))

   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   *  

        
n= int (input('enter how many rows you want:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-1-i))
    

n= int (input('enter how many rows you want:'))
for i in range(n):
    print(' '*(n-i-1)+'* ',end='')
    if i>0:
        print(' '*(2*i-1)+'* ',end='')
    print()


      * 
    *   *
  *       *
*           *
  *       * 
    *   * 
      * 

        
n= int (input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1)+'* ',end='')
    if i>0:
        print('  '*(2*i-1)+'* ',end='')
    print()
for j in range(n-1):
    print('  '*(j+1)+'* ',end='')
    if j!=2:
        print('  '*(2*(n-1)-2*j-3)+'* ',end='')
    print()
print('*   *')
print('  *  ')
print('*   *')

*   *
  *  
*   *

n=int(input())
for i in range(n):
    if i==1:
        print('  '+'* ',end=' ')
    else:
        print('* '+'  '+'*',end='')
    print()

1 1 1 
2 2 2 
3 3 3 
4 4 4 
n=int(input('enter how many rows you want'))
for i in range(n):
    print((str(i+1)+' ')*3)

4 4 4 4 
4 4 4 4 
4 4 4 4 
4 4 4 4 

n=int(input('enter how many rows you want'))
for i in range(n):
    print((str(n)+' ')*n)
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

n=int(input('enter how many rows you want:'))
for i in range(n):
    for j in range(n):
        print(j+1,end=' ')
    print()

1 2 3 
4 5 6 
7 8 9

n=int(input('enter how many rows you want:'))
d=1
for i in range(n):
    for j in range(n):
        print(d,end=' ')
        d+=1
    print()
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print((str(1)+' ')*n)
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print((str(i+1)+' ')*(i+1))
1 
2 3 
4 5 6 
7 8 9 10 
n=int(input('enter how many rows you want:'))
d=1
for i in range(n):
    for j in range(i+1):
        print(d,end=' ')
        d+=1
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
n=int(input('enter how many rows you want:'))
for i in range(n):
    for j in range(i+1):
        print((j+1),end=' ')
    print()

    1 
  2 3 
4 5 6 

n=int(input('enter how many rows you want:'))
d=1
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(d,end=' ')
        d+=1
    print()
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ') *(i+1))

1
  3
    5
      7
    6
  4
2

n=int(input('enter how many rows you want:'))
d=1
k=6
for i in range(n):
    print(('  '*i)+str(d))
    d+=2
for i in range(n-1):
    print('  '*(n-i-2)+str(k))
    k-=2


      1 
    1 2 3 
  1 2 3 2 1 
1 2 3 2 1 0 -1 
#output is not matched
n=int(input('enter how many rows u want:'))

for i in range(n):
    print('  '*(n-i-1),end='')
    d=1
    for j in range(2*i+1):
        if j<=d//2:
            print(d,end=' ')
            d+=1
        else:
            print(d,end=' ')
            d-=1
    print()

A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 

n=int(input('enter how many rows u want:'))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=' ')
    print()
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    for j in range(n):
        print(chr(d),end=' ')
        d+=1
    print()
A 
A B 
A B C 
A B C D 
A B C D E 

n=int(input('enter how many rows u want:'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()

A A A 
B B B 
C C C 
n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    print((chr(d)+' ')*n)
    d+=1
A A A 
A A A 
A A A 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    print((chr(d)+' ')*n) 

A 
B B 
C C C 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    print((chr(d)+' ')*(i+1))
    d+=1 

n=int(input('enter a number:'))
for i in range(n):
    print(i**i)

n=int(input('enter how many rows you want:'))
for i in range(n):
    d=1
    print('  '*(n-i-1),end='')
    for j in range(2*i+1):
        print(d,end=' ')
        if d
1 2 3 4 
2 4 6 8 
3 4 5 6 
4 6 8 10 

n=int(input('enter how many rows you want:'))
for i in range(n):
    d=i+1
    for j in range(n):
        print(d,end=' ')
        if (i+1)%2==0:
            d+=2
        else:
            d+=1
    print()


n=int(input('enter how many rows you want:'))
for i in range(n):
    d=i+1
    for j in range(n):
        print(d,end=' ')
        if (i+1)%2==0:
            d+=2
        elif (i+1)%3==0:
            d+=3
        elif (i+1)%4==0:
            d+=4
        else:
            d+=1
    print()

1 2 3 4 
2 4 6 8 
3 6 9 12 
4 8 12 16 

n=int(input('enter how many rows you want:'))
for i in range(n):
    d=i+1
    for j in range(n):
        print(d,end=' ')
        d+=(i+1)
    print()

    1 
  1 2 3 
1 2 3 4 5 

n=int(input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1),end='')
    d=1
    for j in range(2*i+1):
        print(d,end=' ')
        d+=1
    print()

n=int(input('enter how many rows you want:'))
for i in range(n):
    print('  '*(n-i-1),end='')
    d=1
    for j in range(2*i+1):
        print(d,end=' ')
        if d<(i+1):
            d+=1
        else:
            d-=1
    print()

      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1

n=int(input('enter how many rows you want:'))
for i in range(1,n+1):
    print('  '*(n-i-1),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(j-1,0,-1):
        print(k,end=' ')
    print()

1 4 7 
2 5 8 
3 6 9 

n=int(input('enter how many rows u want:'))
for i in range(n):
    d=i+1
    for j in range(n):
        print(d,end=' ')
        d+=3
    print()
1 
2 2 
3 3 3 
4 4 4 4 

n=int(input('enter how many rows u want:'))
for i in range(n):
    print((str(i+1)+' ')*(i+1))

1
  3
    5
      7
    6
  4
2

n=int(input('enter how many rows u want:'))
d=1
k=6
for i in range(n):
    print('  '*i+str(d))
    d+=2
for i in range(n-1):
    print('  '*(n-i-2)+str(k))
    k-=2
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 

n=int(input('enter how many rows u want:'))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=' ')
    print()

A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    for j in range(n):
        print(chr(d),end=' ')
        d+=1
    print()
A 
A B 
A B C 
A B C D 
A B C D E 

n=int(input('enter how many rows u want:'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()
A A A A 
B B B B 
C C C C 
D D D D 

n=int(input('enter how many rows u want:'))
for i in range(n):
    print((chr(65+i)+' ')*n)

A A A 
A A A 
A A A 

n=int(input('enter how many rows u want:'))
for i in range(n):
    print((chr(65)+' ')*n)

A 
B B 
C C C 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    print((chr(d)+' ')*(i+1))
    d+=1

A 
B C 
D E F 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    for j in range(i+1):
        print(chr(d),end=' ')
        d+=1
    print()

    A 
  B C 
D E F 

n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(d),end=' ')
        d+=1
    print()

A B C D 
B D F H 
C D E F 

n=int(input('enter how many rows u want:'))

for i in range(n):
    d=65+i
    for j in range(n+1):
        print(chr(d),end=' ')
        if (i+1)%2==0:
            d+=2
        else:
            d+=1
    print()

A B C D 
B D F H 
C F I L 
D H L P 

n=int(input('enter how many rows u want:'))
for i in range(n):
    d=i+1
    for j in range(n):
        print(chr(64+d),end=' ')
        d+=i+1
    print()

A B C D E 
F E D C 
B C D 
E D 
C         
        
n=int(input('enter how many rows u want:'))
d=65
for i in range(n):
    for j in range(n-i):
        print(chr(d),end=' ')
        if (i+1)%2==0:
            d-=1
        else:
            d+=1
    print()

    A 
  A B C 
A B C D E 

n=int(input('enter how many rows u want:'))
for i in range(n):
    print('  '*(n-i-1),end='')
    d=65
    for j in range(2*i+1):
        print(chr(d),end=' ')
        d+=1
    print()

A D G 
B E H 
C F I 


n=int(input('enter how many rows u want:'))
for i in range(n):
    d=65+i
    for j in range(n):
        print(chr(d),end=' ')
        d+=3
    print()

A
  C
    E
  D
B'''

n=int(input('enter how many rows u want:'))
d=65
k=68
for i in range(n):
    print('  '*i+chr(d))
    d+=2
for j in range(n-1):
    print('  '*(n-j-2)+chr(k))
    k-=2

        

    




































































