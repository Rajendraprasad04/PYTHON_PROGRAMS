#if u want to print the output then you have to use
#print statments before the regular expression
'''
import re
s='hai python'
print(re.match('h',s))
<re.Match object; span=(0, 1), match='h'>
import re
s='hai python'
re.match('h',s)
<re.Match object; span=(0, 1), match='h'>
re.match('hai',s)
<re.Match object; span=(0, 3), match='hai'>
re.match('py',s)
print(re.match('py',s))
None
re.search('h',s)
<re.Match object; span=(0, 1), match='h'>
re.search('k',s)
print(re.search('k',s))
None
re.findall(' ',s)
[' ']
re.findall('h',s)
['h', 'h']
re.findall('po',s)
[]
re.match('p',s)
re.search('p',s)
<re.Match object; span=(4, 5), match='p'>
re.search('^p',s)
re.findall('p',s)
['p']
re.findall('^p',s)
[]
re.find('n$',s)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    re.find('n$',s)
AttributeError: module 're' has no attribute 'find'
re.findall('n$',s)
['n']
re.findall('n',s)
['n']
s='hi@789%.bye'
re.findall('.',s)
['h', 'i', '@', '7', '8', '9', '%', '.', 'b', 'y', 'e']
s='hai heep hep heep hp hello'


s='apple apple'
re.sub('p','k',s)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    re.sub('p','k',s)
NameError: name 're' is not defined. Did you forget to import 're'?
import
SyntaxError: invalid syntax
import re
re.sub('p','k',s)
'akkle akkle'
re.sub('p','k',s,2)
'akkle apple'
re.subn('p','k',s)
('akkle akkle', 4)
s='apple'
re.findall('[a-m]',s)
['a', 'l', 'e']
s='raj934yj128dhdh38u1282u87ygh76tgdwe'
re.findall('/d',s)
[]
re.findall('\d',s)
['9', '3', '4', '1', '2', '8', '3', '8', '1', '2', '8', '2', '8', '7', '7', '6']
s='hai python'
s.findall('^h',s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.findall('^h',s)
AttributeError: 'str' object has no attribute 'findall'
re.findall('^h',s)
['h']
re.findall('^p',s)
[]
re.findall('n$',s)
['n']
re.findall('p$',s)
[]
re.findall('.',s)
['h', 'a', 'i', ' ', 'p', 'y', 't', 'h', 'o', 'n']
s='hai pytho\nn'
re.findall('.',s)
['h', 'a', 'i', ' ', 'p', 'y', 't', 'h', 'o', 'n']
s='hai py\thon'
re.findall('.',s)
['h', 'a', 'i', ' ', 'p', 'y', '\t', 'h', 'o', 'n']
s='hp hep heep heeep heeeep'
re.findall('he*p',s)
['hp', 'hep', 'heep', 'heeep', 'heeeep']
re.findall('h*p',s)
['hp', 'p', 'p', 'p', 'p']
m='hp heehp heep phhp'
re.findall('h*p',s)
['hp', 'p', 'p', 'p', 'p']
re.findall('h*p',m)
['hp', 'hp', 'p', 'p', 'hhp']
re.findall('he+p',s)
['hep', 'heep', 'heeep', 'heeeep']
re.findall('he?p',s)
['hp', 'hep']
re.findall('he{2}',s)
['hee', 'hee', 'hee']
re.findall('he{3}p',s)
['heeep']

           
SyntaxError: unterminated string literal (detected at line 1)
re.findall('hp/hep',s)
           
[]
re.findall('hp|hep',s)
           
['hp', 'hep']
ord('d')
           
100
re.findall('(hp)',s)
           
['hp']
re.findall('\Ah',s)
           
['h']
re.findall('\Ap',s)
           
[]
re.findall('\ah',s)
           
[]
re.findall('\ap',s)
           
[]
re.findall('\',s)
           
SyntaxError: unterminated string literal (detected at line 1)
re.findall('\bh',s)
           
[]
re.findall(r'bh',s)
           
[]
re.findall(r'\bh',s)
           
['h', 'h', 'h', 'h', 'h']
re.findall('\bh',s)
           
[]
re.findall(r'\Be',s)
           
['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
re.findall(r'\Bh',s)
           
[]
s='hai how are you'
           
re.findall('\d',s)
           
[]
s='hai h038 are9,y4oy'
           
re.findall('\d',s)
           
['0', '3', '8', '9', '4']
re.findall('\d+',s)
           
['038', '9', '4']
s='hai 121 142 h153 k2 5 67 50'
           
re.findall('\d+',s)
           
['121', '142', '153', '2', '5', '67', '50']
re.findall('\D',s)
           
['h', 'a', 'i', ' ', ' ', ' ', 'h', ' ', 'k', ' ', ' ', ' ']
re.findall('\D+',s)
           
['hai ', ' ', ' h', ' k', ' ', ' ', ' ']
re.findall('\s',s)
           
[' ', ' ', ' ', ' ', ' ', ' ', ' ']
re.findall('\S',s)
           
['h', 'a', 'i', '1', '2', '1', '1', '4', '2', 'h', '1', '5', '3', 'k', '2', '5', '6', '7', '5', '0']
re.findall('\S+',s)
           
['hai', '121', '142', 'h153', 'k2', '5', '67', '50']
re.findall('\w',s)
           
['h', 'a', 'i', '1', '2', '1', '1', '4', '2', 'h', '1', '5', '3', 'k', '2', '5', '6', '7', '5', '0']
re.findall('\W',s)
           
[' ', ' ', ' ', ' ', ' ', ' ', ' ']
re.findall('50\Z',s)

s='hai python'
re.findall('[arn]',s)
['a', 'n']
re.findall('[a-f]',s)
['a']
re.search('[a-f]',s)
<re.Match object; span=(1, 2), match='a'>
print(re.search('[a-f]',s))
<re.Match object; span=(1, 2), match='a'>
p=re.search('[a-f]',s)
print(p)
<re.Match object; span=(1, 2), match='a'>
re.findall('[a-n]',s)
['h', 'a', 'i', 'h', 'n']
re.findall('[0123]',s)
[]
s='apple123945'
re.findall('[0-4]',s)
                       
['1', '2', '3', '4']
re.findall('[0-9]',s)
                       
['1', '2', '3', '9', '4', '5']
s='123456789'
re.findall('[0-5][0-9]',s)
['12', '34', '56']
s='hai python'
re.findall('[a-zA-Z]',s)
['h', 'a', 'i', 'p', 'y', 't', 'h', 'o', 'n']




#validation of indian phone number by using Regular Expressions

data=['hello','harshad','+11-76543','+91-9989896562','98 765432456','+91-7330730990']
#indian phone number first have the '+'
#indian phone number have 91 after +
#its have '-' after + and 91
#after, the first number should be a 6 0r 7 or 8 or 9
#after indian phone number have any 9 digits from 0 to 9

#by using match function

import re
mp='[+]91-[6-9]\d{9}'
for i in data:
  if re.match(mp,i):
    print(i)

    
#by using findall function
import re
s='hello harshad +11-76543 +91-9989896562 98 765432456 +91-7330730990'

vp=re.findall('[+]91-[6-9]\d{9}',s)
print(vp)
for i in vp:
  print(i)

#validation of emails
#1. it can be alphabets or numbers from 1 to 9
#2. it can be 0 to n alphabets and numbers
#3. '.' can present 0 or 1 time
#4. it can be 1 or more times of alphabets and digits
#5. @ should be there 
#6. gmail
#7. .
#8. com should be there

 # by using match function function
import re
mp='[a-zA-Z0-9]\w*[.]?\w+@gmail[.]com'

data=['harshad@gmail.com','harshad','rajendra82364ghd@gmail.com','2gsadg@gmail.com','krajendraprasad553@gmail.com']

for i in data:
  if re.match(mp,i):
    print(i)
  
# by using findall function

import re
mp='[a-zA-Z0-9]\w*[.]?\w+@gmail[.]com'
s='harshad@gmail.com harshad rajendra82364ghd@gmail.com 2gsadg@gmail.com krajendraprasad553@gmail.com'
ve=re.findall(mp,s)
print(ve)
for i in ve:
  print(i)
  '''

# wap to find all the odd numbers sum from given string like 121,153,5,67

import re
s='hai 121 142 h153 k2 5 67 50'
l=re.findall('\d+',s)
#print(l)
sum=0
for i in l:
  k=int(i)
  if k%2!=0:
    sum+=k
print(sum)

    


           

































































           

