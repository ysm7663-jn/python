# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError..
# 문법적으로 에러가 없지만 코드 실행(런타임) 프로세스에서 발생하는 예외 처리 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('test) SyntaxError: EOL while scanning string literal
# print('Hello')) SyntaxError: unmatched ')'
# if True SyntaxError: invalid syntax
#   pass
# a = 20; b = 30; a+ = b SyntaxError: invalid syntax
# x => y SyntaxError: invalid syntax

# NameError : 참조 변수 없음

a = 10
b = 15

# print(c) NameError: name 'c' is not defined


# ZeroDivisionError : 0 나누기 에러

# print(10 / 0) ZeroDivisionError: division by zero


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

# print(x[1])
# print(x[3]) # 예외 발생 / IndexError: list index out of range
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 예외 발생 / IndexError: pop from empty list
# print(x.pop(50)) # 예외 발생


# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

#print(dic['hobby'])     # 키가 존재하지 않으면 예외 / KeyError: 'hobby'
print(dic.get('hobby')) # 안전 / None / dict에서 요소 찾을시 사용


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# import time
# print(time.time()) # NameError: name 'time' is not defined / time import가 없음
# print(time.month()) # 예외 발생 / NameError: name 'time' is not defined

x = [1, 2, 3]
# print(x.append(4)) AttributeError: 'list' object has no attribute 'add'
# print(x.add(10)) AttributeError: 'list' object has no attribute 'add'


# ValueError : 참조 값이 없을 때 예외

x = [1, 5, 9]

# x.remove(5)
# print(x) / [1, 9]

# x.remove(100)
# print(x) # 예외 발생 / ValueError: list.remove(x): x not in list

t = (10, 100, 1000)

print(t.index(100))
# print(t.index(7)) # 예외 발생 / ValueError: tuple.index(x): x not in tuple


# FileNotFoundError

# f = open('test.txt') # 얘외 발생 / FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 예외 발생 / TypeError: can only concatenate list (not "tuple") to list  
# print(x + z) # 예외 발생 / TypeError: can only concatenate list (not "str") to list
# print(y + z) # 예외 발생 / TypeError: can only concatenate tuple (not "str") to tuple       
# print(sum([1,2,3],10,1)) # 예외 발생 / TypeError: sum() takes at most 2 arguments (3 given)

# print(x + list(y)) # [1, 2, 1, 2]
# print(x + list(z)) # [1, 2, 't', 'e', 's', 't']


# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행


# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else: # try가 정상적으로 작동했을 경우만 작동, except일 경우는 작동하지 않음
    print('ok! else!')

print()

# 예제2

try:
    z = 'Kim'  # 'park' 예외 발생 / Not found it! - Occurred ValueError!
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:  # 모든 에러를 처리(Exception) / 에러의 종류를 잘 모를경우 사용
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else: # 정상 작동했을 경우만 작동
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨 / try가 성공하던 except가 수행되던 상관없이 수행됨

"""
Kim Found it! 1 in name
ok! else!
ok! finally!
"""

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

"""
try
finally
"""
print()

# 예제5
# 에러가 예측 가능한 경우 try에서의 코드 순서대로 위에서부터 그에 해당하는 에러except 작성
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError:
    print('Raise! Occurred ValueError')
except IndexError:
    print('Courred IndexError')
except Exception: # == except :   같은 역할
    print('Occurred Exception')
else:
    print('ok! else!')

# a = 'Part' Raise! Occurred ValueError
# a = 'Kim' Ok! pass ok! else!
