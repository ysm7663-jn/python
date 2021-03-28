"""
# 1번 문제

import csv

with open('./resource/a.csv', 'r') as f :
    reader = csv.reader(f)


    

    arr = list(map(int, arr))
    print(arr)
    print(type(arr))

    

"""
10,60,20,33,55,25,64,83,523,54,87,84,56,84
"""
"""
# 2번 문제
class Median:
    
    arr = []
    result = 0.0

    def __init__(self):
        pass
 
    def get_item(self, item):
        Median.arr.append(item)
 
        arr = sorted(Median.arr)
        
        middle = int(len(arr) / 2)
        
        if (len(arr) % 2 == 0) :
            Median.result = (arr[middle] + arr[middle] - 1) / 2.0
        else :
            Median.result = arr[middle]
    def clear(self):
        Median.arr = []
         
    def show_result(self):
        print(Median.result)
            

median = Median()

for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()

for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()


# 3번 문제
class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self) :
        print(self.name + ' cannot speak.')

    def move(self) :
        print('%s moves like a jagger' % self.name)
 
class Retriever(Dog):
    def __init__(self, name):
        super().__init__(name)

    def speak(self) :
        print(self.name + ' is smart enough to speak.')

    def move(self) :
        print('%s moves like a jagger' % self.name)
    
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()
"""
---------- 출력 -----------------
Nancy cannot speak.
Nancy moves like a jagger.
Michael is smart enough to speak.
Michael moves like a jagger.
---------------------------------
"""
"""
# 4번   
class Foo:

    def __init__(self) :
        pass

    def bar(self) :
        print(str(A))
 
print(Foo.bar)       # A 출력

#print(Foo().bar)     # B 출력
#print(Foo.Bar.bar)   # C 출력
#print(Foo.Bar().bar) # D 출력
"""
