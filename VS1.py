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