class A:
    x=90
    _y=89
    __z=899
    def display(self):
        print('public display method')
    def _cycling(self):
        print('cycling is protected method')
    def __driving(self):
        print('driving is private method')
print(A.x)
print(A._y)
print(A._A__z)
OA=A()
OA.display()
OA._cycling()
OA._A__driving()