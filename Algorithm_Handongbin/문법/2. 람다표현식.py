# 람다 표현식
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다

# 효과적인 사용 
# 함수 자체를 입력으로 받는 또 다른 함수, 함수를 한 번정도로만 사용할 경우, 함수가 매우 간단한 경우

def add(a, b):
    return a + b

print(add(3, 7)) # 10

print((lambda a, b: a + b)(3, 7)) # 10
# (lambda 입력 받을 매개변수: 함수의 반환 값)(매개변수)

# 예시 1 : 내장 함수에서 자주 사용되는 람다 함수(정렬)
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key)) # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
print(sorted(array, key=lambda x: x[1])) # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]

# 예시 2 : 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# map : 각각의 원소에 함수를 적용하고 싶을때  
result = map(lambda a, b: a + b, list1, list2)

print(list(result)) # [7, 9, 11, 13, 15]