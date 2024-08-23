def girls():
    print('girls started barking')
    yield 23
    print('girls are again barking')
    yield 'hai'
g=girls()
print(g)
print(next(g))
print(next(g))
print(next(g))
    
