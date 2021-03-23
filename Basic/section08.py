# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 패키지 : 모듈들을 디렉토리를 구조적으로 관리(폴더)
# 모듈   : 

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex1 : ", Fibonacci.fib2(400)) # ex1 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print("ex1 : ", Fibonacci().title) # ex1 :  fibonacci


# 사용2(클래스)
# 메모리 많이 차지, 권장x
from pkg.fibonacci import *

Fibonacci.fib(400) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

print("ex2 : ", Fibonacci.fib2(500)) # ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print("ex2 : ", Fibonacci().title) # ex2 :  fibonacci


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(500) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

print("ex3 : ", fb.fib2(600)) # ex3 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print("ex3 : ", fb().title) # ex3 :  fibonacci


# 사용4(함수) : 파일 Alias
import pkg.calculations as c

print("ex4 : ", c.add(10,10)) # ex4 :  20
print("ex4 : ", c.mul(10,4)) # ex4 :  40


# 사용5(함수)
from pkg.calculations import div as d

print("ex5 : ", int(d(100,10))) # ex5 :  10

# 사용6
import pkg.prints as p
import builtins # 파이썬에서 기본으로 제공하는 패키지

p.prt1() # I'm Niceboy!
p.prt2() # I'm Goodboy!
print(dir(p)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'prt1', 'prt2']
print(dir(builtins))
