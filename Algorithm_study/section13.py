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