'''#To print number times stars(*) 
n=int(input('enter n value: '))
for i in range(n):
    print('*',end='')

    
#to print squarshape with stars
n=int(input('enter a how many rows youn want:'))
for i in range(n):
    print('3 '*n)

    
#to print square with user provided number that is n=some number like 1 or 2 or 3....
n=int(input('enter a number you want in the form of square:'))
for i in range(n):
    print((str(n)+' ')*n)'''



'''#print output like
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
n=int(input('n value: '))
d=1
for i in range(n):
    print((str(d)+' ')*n)
    d+=1
    if d==n+1:
        break
#print output like below
A A A A
A A A A
A A A A
A A A A
n=int(input('enter a no.of rows:'))
for i in range(n):
    print('A '*n)
A
B B
C C C
D D D D

n= int(input('enter no.of rows:'))
for i in range(n):#i=o,1,2,3,...,n
    print((chr(65+i)+' ')*(i+1))
*
* *
* * *
* * * *
n=int(input('enter a no.of rows:'))
for i in range(n):
    print('* '*(i+1))
* * * * 
* * * 
* * 
* 

n=int(input('enter  no.of rows:'))
for i in range(n):
    print('* '*(n-i))
1 2 3 4 
1 2 3 
1 2 
1 

n=int(input('enter  no.of rows:'))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    print()
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

n=int(input('enter a no.of rows'))
for i in range(n):
    for j in range(i+1):
        print(j,end=' ')
    print()
   1 
  2 2 
 3 3 3 
4 4 4 4 

n=int(input('enter a no.of rows: '))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))

n=int(input('enter a no.of rows:'))
for i in range(n):
    for j in range(i+1):
        print(' '*(n-i-1)+(chr(64+n-j)),end='')
    print()
    D 
   D C 
  D C B 
 D C B A 

n=int(input('enter a no of rows:'))
for i in range(n):
    print(' '*(n-i-1),end=' ')
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()
A 
A B 
A B C 
A B C D 
A B C 
A B 
A 
n=int(input('enter a no.of rows:'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()
 A B C D E 
  A B C D 
   A B C 
    A B 
     A 
n=int(input('enter a no.of rows:'))
for i in range(n):
    print(' '*i,end=' ')
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
n=int(input('enter a no.of rows:'))
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n-1):
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print('*',end=' ')
    print()
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
n=int(input('enter a no.of rows:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for j in range(n-1):
    print(' '*(j+1)+'* '*(n-j-1))

* 
* * 
* * * 
* * * * 
* * * 
* * 
* 

n=int(input('enter a no.of rows:'))
for i in range(n):
    print('* '*(i+1))
for j in range(n-1):
    print('* '*(n-j-1))

      * 
    * * 
  * * * 
* * * * 
  * * * 
    * * 
      * 


n=int(input('enter  no.of rows:'))
for i in range(n):
    print('  '*(n-i-1)+'* '*(i+1))
for j in range(n-1):
    print('  '*(j+1)+'* '*(n-j-1))
      * 
    *   * 
  *       * 
*           *

n=int(input('enter a no.of rows:'))
for i in range(n):
    print('  '*(n-i-1)+'* ',end='')
    if i>0:
        print('  '*(2*i-1)+'*',end='')
    print()
*           *
  *       *
    *   *
      * 

n=int(input('enter a no.of rows:'))
for i in range(n):
    print('  '*i+'* ',end='')
    if i!=n-1:
        print('  '*(2*n-2*i-3)+'*',end='')
    print()



A               A
  B           B
    C       C
      D   D
        E 

n=int(input('enter a no.of rows:'))
for i in range(n):
    print('  '*i+chr(65+i),end=' ')
    if i!=n-1:
        print('  '*(2*n-2*i-3)+chr(65+i),end='')
    print()
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 

n=int(input('enter a no.of rows'))
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print((j+1),end=' ')
    print()
for i in range(n-1):
    print('  '*(i+1),end='')
    for j in range(n-i-1):
        print((j+1),end=' ')
    print()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
      * 
    *   *
  *       *
*           *
  *       * 
    *   * 
      * 

n=int(input('enter a no.of rows:'))
for i in range(n):
    print('  '*(n-i-1)+'* ',end='')
    if i>0:
        print('  '*(2*i-1)+'*',end='')
    print()
for i in range(n-1):
    print('  '*(i+1)+'* ',end='')
    if i!=n-2:
        print('  '*(2*(n-1)-2*i-3)+'* ',end='')
    print()

  1 7 12 16 19 21 
  2 8 13 17 20 
3 9 14 18 
4 10 15 
5 11 
6 

   
n=int(input('enter how many rows you want:'))
for i in range(n):
    if i==0 or i==1:
        print('  ',end='')
    k=i+1
    for j in range(n-i):
        print(k,end=' ')
        k+=(n-j)
    print()

    g
   gr
  gro
 grou
group

w='group'
for i in range(len(w)):
    print(' '*(len(w)-i-1)+w[:i+1])



      G
     GR
    GRA
   GRAM
  GRAMP
 GRAMPR
GRAMPRO

s='PROGRAM'
n=len(s)
s1=''
s2=''
for i in range(n):
    if i>2:
        s1+=s[i]
    else:
        s2+=s[i]
s3=s1+s2
print(s3)

for i in range(n):
    print(' '*(n-i-1)+s3[:i+1])
    

#print a numbers from 1 to 100 without using numbers
n=ord('d')
for i in range(n):
    print(i+True,end=' ')
    

1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 

    
n=int(input('enter how many rows you want:'))
for i in range(n):
    #k=i+1
    d=1
    for j in range(i+1):
        print(str(d+j),end=' ')
        if i+1==j+1:
            print('  '*(2*n-2*i-2),end='')
            k=i+1
            for m in range(i+1):
                print(k,end=' ')
                k-=1
    print()
 '''
































    
