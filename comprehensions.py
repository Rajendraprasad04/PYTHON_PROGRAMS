'''l=[]
for i in range(10):
    l.append(i)
print(l)

l=[i for i in range(1,2)]
print(l)

l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)

l=[i for i in range(1,11) if i%2==0]
print(l)

t=[11,22,33,100,200,20]
l=[i for i in t if i%2==0 and i>100]
print(l)

t=[11,22,33,100,200,20]
l=[i  for i in t if i%2==0 or i>30]
print(l)

l=[1,2,3,-88,100,-99,-3,0]
l=[i if i>0 else 0 for i in l]
print(l)

l=[[i]*3 for i in range(1,11)]
print(l)

l=[[i,j,k] for i in range(1,11) for j in range(1,11) for k in range(1,11) if i==j==k]
print(l)

t={i for i in range(1,11)}
print(t)
t=[1,3,4,6,5]
#d={i:i**2 for i in t}
#print(d)

#d={i:t[i] for i in range(len(t))}
#print(d)
d={k:v for k,v in enumerate(t)}
print(d)

t=[1,3,4,6,5]
s='ABCDE'
d={s[i]:t[i] for i in range(len(t))}
print(d)


t=[1,3,4,6,5]
s='ABCDE'
d=list(zip('ABCDE',[1,3,4,6,5]))
print(d)

d={k:v for k,v in zip('ABCDE',[1,3,4,6,5])}
print(d)
s='aBCde'
d={i.upper():i.lower()*len(s) for i in s}
print(d)'''
#single ton class : is a class which have only one object in its lifetime
def singleton(arg):
    d={}
    def inner():
        if arg not in d:
            d[arg]=arg()
        return d[arg]
    return inner
@singleton
class Vinayaka():
    def __init__(self):
        self.tickets=300
    def Booking(self,n):
        self.booking_tickets=n
        if self.tickets>=n:
            self.tickets-=n
            print('tickets are booked successfully')
            print(f'available tickets are{self.tickets}')
        else:
            print('sorry')
            print(f'available tickets are{self.tickets}')
rajendra=Vinayaka()
rajendra.Booking(100)
rajendra.Booking(50)
ram=Vinayaka()
ram.Booking(200)

















































