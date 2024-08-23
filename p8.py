class School():
    school_name='high school'
    school_hm='rajendra'
    school_address='v.kota'
    school_mobile=12345
    def __init__(self,name,age,standard,mobile):
        self.name=name
        self.age=age
        self.standard=standard
        self.mobile=mobile
    def student_details(self):
        print(f'name of student {self.name}')
        print(f'age of student {self.age}')
        print(f'standard of student {self.standard}')
        print(f'mobile of student {self.mobile}')
    def update_mobile(self):
        new_mobile=int(input('enter a new  mobile bobile number'))
        self.mobile=new_mobile
        print(f'new mobile numbes is {self.mobile}')
    def get_fullname(self):
        first_name=input('enter a first name')
        second_name=input('enter a second name')
        self.name=first_name+second_name
        print(f'full name is {self.name}')
kiran=School('kiran kumar',15,10,98765)
deva=School('devaraj',14,9,56789)
#kiran.student_details()
#School.student_details(deva)
kiran.get_fullname()
deva.update_mobile()
