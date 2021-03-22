"""
    1번.
    *
    **
    ****
    *****
    *******
    ********
    출력
"""

for i in range(1, 9):
    if (i % 3 != 0):
        print(i * '*')
        

"""
2번.
다음은 map함수에 대한 설명이다. map 함수와 lambda 함수를 이용하여, 10진수 숫자가 문자열로 작성된 리스트 a의 각 원소의 값을 1씩 증가시킨 문자열로 변경하는 프로그램을 한 줄의 코드로 작성하시오.

map(func, iter) 함수는 두 개의 입력을 받는다.
첫 번째 입력 func은 하나의 입력을 받는 함수이며, 반드시 출력이 존재한다.
map 함수는 두 번째 입력 iter를 순회하면서 각 원소 elem을 func의 입력으로 하여, func(elem)을 출력하는 iterative object를 출력한다.
map의 출력은 일회성으로 동작하는 iterative object이며, list() 또는 tuple()을 이용하여 여러번 참조할 수 있도록 변환할 수 있다
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
<이곳에 들어갈 한 줄의 코드를 작성하시오.>
print(a)
"""
a2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a2 = list(range(1, 10))
print(a2)

"""
3번.
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
basket ball 7
base ball 6
soccer 6 
출력
"""
# def func_count():



a3 = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
baseball = a3.count('base ball')
basketball = a3.count('basket ball')
soccer = a3.count('soccer')





"""
4번.
0 1 2 3 4 5  6  7  8   9   10  11
0 1 2 4 8 16 32 64 128 256 256 256
반복문과 print() 함수 사용하여 출력
"""

# def print()

# for i in 12 :

a7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b7 = lambda num: num ** 2
c7 = list()
for elem in a7:
    c7.append(b7(elem))
print(c7)

a9 = [1, 2, 3, 4]
b9 = [3, 4, 5, 6]
c9 = list(set(a9).intersection(set(b9)))
print(c9)

a6 = ['파', '이', '썬', '썬', '썬', '썬', '즐', '즐', '즐', '거', '운']
last = None
for elem in a6:
    if elem == last:
        continue
    print(elem, end="")
    last = elem



