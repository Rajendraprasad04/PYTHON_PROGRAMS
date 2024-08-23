'''
s='this is weekend'
new_string=' '.join(s.split()[::-1])
print(new_string)


'''



s='this is weekend'
new_string=(s.split()[::-1])
s1=''
for i in new_string:
    s1+=i+' '
print(s1)

#output:-'weekend is this'

