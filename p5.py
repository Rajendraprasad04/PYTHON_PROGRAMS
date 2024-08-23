class School():
    school_name='high school'
    school_hm='Rajendra'
    school_address='v.kota'
    school_type='private'
    def __init__(self,n,a,c,s):
        self.name=n
        self.age=a
        self.classs=c
        self.section=s
A=School('kiran',15,10,'X')
B=School('prasanth',14,9,'Y')
print(A.name)
print(B.name)
print(School.school_name)
A.name='harish'
print(A.name)
