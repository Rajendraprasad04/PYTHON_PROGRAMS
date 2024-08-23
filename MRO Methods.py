'''class employee:
    cname='accenture'
    caddress='bangalore'
    empcount=0
    def __init__(self,n,i,s):
        self.ename=n
        self.eid=i
        self.salary=s
        employee.empcount+=1
    def __del__(self):
        employee.empcount-=1
raj=employee('rajendra',1234,10000)
dev=employee('devaraj',3667,20000)
print('The no.of employees join in compony:',employee.empcount)
del raj
print('The no.of employees join in compony:',employee.empcount)
print(dev.empcount)
print(raj.empcount)

n=int(input('enter a number:'))
d=n
rev=0
while d>0:
    rem=d%10
    rev=rev*10+rem
    d=d//10
print(rev)
if rev==n:
    print('polindrome')
else:
    print('not a polindrome')

class Book:
    def __init__(self,n,a,p):
        print('object is created so interpreter has called me')
        self.bname=n
        self.author=a
        self.price=p
    def __str__(self):
        return self.bname
    def __del__(self):
        print(f'{self} object is deleted so interpreter has called')
python=Book('python','van guido rossum',100)
django=Book('django','simon willison',200)
del python
print (django)'''


n=int(input('enter no.of rows you want:'))
for i in range(n):
    r=i
    for j in range(n):
        print(chr(65+i),end=' ')
        r+=i
    print()
    
    
        


































