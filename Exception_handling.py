'''print('start')
try:
    print('try is started')
    print(a)
    print('try is ended')
except NameError as ne:
    print(ne)
print('end')

print('satrt')
l=[11,22,33,44]
ip=int(input('enter which element you want:'))
try:
    print('try is started')
    n=l[ip]
    d=int(input('enter a divisor:'))
    result=n/d
    print('try is ended')
except IndexError as ie:
    print(ie)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(result)
print('end')




print('satrt')
l=[11,22,33,44]
ip=int(input('enter which element you want:'))
try:
    print('try is started')
    try:
        n=l[ip]
    except Exception as e:
        print(e)
    try:
        d=int(input('enter a divisor:'))
        result=n/d
    except Exception as e:
        print(e)
    print('try is ended')
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print('finally block is a block which get executed irrespective of error occurance')
print('end')

#handler in current function
def f1():
    print('f1 is started')
    try:
        n=10/0
    except Exception as e:
        print(e)
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
print('main is started')
f2()
print('main is ended')

#haldler in caller function (where we are calling f1)
def f1():
    print('f1 is started')
    n=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    try:
        f1()
    except Exception as e:
        print(e)
    print('f2 is ended')
print('main is started')
f2()
print('main is ended')'''



#handler in where we are called the caller function(main space)


def f1():
    print('f1 is started')
    n=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
print('main is started')
try:
    f2()
except Exception as e:
    print(e)
print('main is ended')


#now are going to see the what is raise keyword and how it is going to work



















































































































































































































