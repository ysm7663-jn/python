
# 1번 문제

import csv
 
sum = 0
with open('./resource/a.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        for elem in line:
            sum += int(elem)
print(sum)
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
    def move(self):
        print(self.name + ' moves like a jagger.')
 
 
class Retriever(Dog):
    def speak(self):
        print(self.name + ' is smart enough to speak.')
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()


# 4번   
class Foo:
    bar = 'A'
    def __init__(self):
        self.bar = 'B'
 
    class Bar:
        bar = 'C'
        def __init__(self):
            self.bar = 'D'
 
print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력