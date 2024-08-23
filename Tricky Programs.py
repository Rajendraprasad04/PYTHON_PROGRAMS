#multiplication of two numbers without using multiplication operator(*)
'''def multiply(x,y):
    result=0
    for i in range(y):
        result+=x
    print(result)
x=int(input('enter a first number:'))
y=int(input('enter a socond number:'))
multiply(x,y)
      
print(max(2,3))

#maximum digit in given number
def maximum(n):
    d=n
    max=0
    while d>0:
        r=d%10
        d=d//10
        if r>max:
            max=r
    print(max)
n=int(input('enter a niumber:'))
maximum(n)



def string_to_integer(s):
    result=0
    for i in s:
        result=result*10+ord(i)-ord('0')
    print(result)    
s=input('enter a string:')
string_to_integer(s)'''

def string_to_int(s):
    result = 0
    for c in s:
        result = result * 10 + ord(c) - ord('0')
    return result

input_str = "12345"
print(f"The integer representation of '{input_str}' is {string_to_int(input_str)
      +++++++++}")



    

