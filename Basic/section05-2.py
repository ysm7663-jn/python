# Section05-2
# 파이썬 흐름제어(제어문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10): # 0 ~ 9
    print("v2 is :", v2)

for v3 in range(1, 11):
    print("v3 is :", v3) # 1 ~ 10

for v4 in range(1, 11, 2): # 1, 3, 5, 7, 9
    print("v4 is :", v4)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1) # 5050
print('1 ~ 100 합 : ', sum(range(1, 101)))  # sum(리스트) / 5050
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 3))) # 1717

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1 / 리스트
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name) 

# 예제2 / 리스트
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Your number", number)

# 예제3 / 문자열
word = 'dreams'

for s in word :
    print('word : ', s)

# 예제4 / 딕셔너리
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}
# 기본 값은 키
for key in my_info:
    print('key : ', key)
"""
key :  name
key :  age
key :  city
"""
# 키
for keys in my_info.keys():
    print('keys : ', keys)
"""
keys :  name
keys :  age
keys :  city
"""
# 값
for val in my_info.values():
    print('value : ', val)
"""
value :  Kim
value :  33
value :  Seoul
"""
# 키와 값
for k, v in my_info.items():
    print('items : ', k, v)

"""
items :  name Kim
items :  age 33
items :  city Seoul
"""

# 예제5
name = 'KennRY'

for n in name:
    if n.isupper(): # 대문자면 
        print(n)  # 그대로 출력
    else:
        print(n.upper())  # 소문자면 대문자로 바꿔서 출력

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break
for num in numbers:
    if num == 33: # 33 이면 
        print("found : 33!") # 출력 후
        break # for문 종료
    else:
        print("not found : ", num) # 아닐 경우 그냥 출력

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float: # 실수면
        continue # 다음 순회로 넘어감

    print("type:", type(v)) 
    print("multiply by 2:", v * 3)
    """
    type: <class 'str'>
    multiply by 2: 111
    type: <class 'int'>
    multiply by 2: 6
    type: <class 'int'>
    multiply by 2: 15
    type: <class 'bool'>
    multiply by 2: 3
    type: <class 'complex'>
    multiply by 2: (12+0j)
    """

# for-else 실습
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:  # 45
        print("found : 33!")
        break
    else:
        print("not found : ", num)
else:
    print("Not Found 39...")

# flag 사용

f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)

# else 구문 정리(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1

i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
else:
    print('else block run!')

# 예제2
j = 1
while j <= 10:
    print('j : ', j)
    if j == 11:
        break
    j += 1
else:
    print('else block run!')

# 중첩 for 문 구구단 출력

for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end='')
    print()

# 자료 구조 변환 예제
name = 'Niceman'
print('reversed : ', reversed(name)) # reversed :  <reversed object at 0x000002711B0604C0>
print('list : ', list(reversed(name))) # list :  ['n', 'a', 'm', 'e', 'c', 'i', 'N']
print('tuple : ', tuple(reversed(name))) # tuple :  ('n', 'a', 'm', 'e', 'c', 'i', 'N')
print('set : ', set(reversed(name)))  # 순서X / set :  {'i', 'c', 'N', 'a', 'm', 'e', 'n'} / 작동시마다 랜덤으로 작동