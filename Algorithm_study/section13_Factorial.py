# 재귀함수
# n! 함수 구현
def factorial(num) :
    if num > 1 :
        return num * factorial(num - 1)
    else :
        return num
for i in range(10) :
    print(factorial(i))

print('-----')

def factorial2(num) :
    if num <= 1 :
        return num
    return_value = num * factorial2(num - 1)
    return return_value
for i in range(10) :
    print(factorial(i))
print('-----')

"""
factorial(n) = n - 1번의 factorial() 함수를 호출해서, 곱셈을 함
    - 일종의 n - 1번 반복문을 호출하는 것과 동일
    - factorial() 함수를 호출할 때마다, 지역변수 n이 생성됨
시간 복잡도 : O(n-1) >> O(n)
공간 복잡도 : O(n-1) >> O(n)
"""
"""
재귀 호출의 일반적인 형태
def function1(입력) :
    if 입력 > 일정값 : # 입력이 일정 값 이상이면
        return function(입력 - 1)
    else :
        return 일정값, 입력값, 또는 특정값  # 재귀 호출 종료

def function2(입력) :
    if 입력 <= 일정값 :     # 입력이 일정 값보다 작으면
        return 일정값, 입력값, 또는 특정값  # 재귀 호출 종료
    function(입력보다 작은 값)
    return 결과값
"""
""" 
재귀 호출은 스택의 전형적인 예
: 함수는 내부적으로 스택처럼 관리된다.
    - 파이썬에서 재귀 함수는 깊이가 1000회 이하가 되어야 함
"""
def multiple(data) :
    if data <= 1 :
        return data
    return data * multiple(data - 1)

print(multiple(10))

print('-----')

import random

def sum_list(data) :
    if len(data) <= 1 :
        return data[0]
    return data[0] + sum_list(data[1:])

data = random.sample(range(100), 10)
print(sum_list(data))

print('-----')

# 회문 문제
def palindrome(string) :
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1] :
        return palindrome(string[1:-1])
    else :
        return False
print(palindrome('Dave'))
print(palindrome('level'))

print('-----')

def func(data) :
    if data == 1 :
        return data  
    
    if data % 2 == 0 :
        print(data // 2)
        func(data // 2)
    else :
        print(3 * data + 1)
        func(3 * data + 1)
func(3)

print('-----')

def func(n) :
    if n == 1 :
        return 1
    
    elif n == 2 :
        return 2
    
    elif n == 3:
        return 4

    elif n > 3:
        return func(n-1) + func(n-2) + func(n-3)
    
    else :
        return 

print(func(5))


