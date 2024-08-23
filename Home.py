'''
#wap to print square of  given number

n=int(input('enter a number:'))
print('square of number:',n**2)

#wap to count no. of vowels and consonants

s=input('enter astring:')
v='AEIOUaeiou'
cv=0
cc=0
for i in s:
    if i in v:
        cv+=1
    if i.isalpha() and i not in v:
        cc+=1
print('count of vowels:',cv)
print('count of consonats:',cc)

#wap to convert fahrenheit into celsius
t=eval(input('enter a temparature:'))
celsius=(t-32)*1.8
fahrenheit=(t+32)*1.8
print('celsius tempatarute is :',celsius)
print('fahrenheit temparatureis :',fahrenheit)'''

#wap to remove all the blanck spaces from the string
'''
s=input('enter astring:')
r=''
for i in s:
    if i!=' ':
        r+=i
print(r)
'''

#wap to calculate the simple interest and principle

def interest():
    p=int(input('enter principle amount:'))
    t=eval(input('enter time span:'))
    r=eval(input('enter  rate of interest:'))
    interest=(p*t*r)/100
    print('rate of interest is :',interest)
    print('total amount of principle:',p+interest)
interest()








































































