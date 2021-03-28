class Foo:
    a = 10
    def __init__(self, name) :
        self.name = name
    
    def speak(self) :
        a = 20
        print('I am ' + self.name)
        print(a)

class Bar(Foo):
    a = 10
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        a = 20
        print('You are ' + self.name)
        print(a)

bar = Bar('John')
bar.speak()

print('----')
"""
def int_sum(*args):
    try:
        for n in args :
            sum += n
    except:
        print('error')
    return sum

int_sum('str')
"""
abc = ['1', '2', '3']

abc = list(map(int, abc))

print(abc)

