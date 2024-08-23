n=int(input('enter a number'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(' not a prime number')
        else:
            print(' prime number')
else:
     print('not a prime number')