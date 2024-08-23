
def upper_case(s):
    c=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            c+=1
    return c
s=input('enter a string:')
print(upper_case(s))

'''
s=input('enter a string:')
c=0
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        c+=1
print(c)'''
