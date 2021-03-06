# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
#print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))   # ['C', 'a', 'p']

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
# c = [1, 2, 3, 4]
print('#=====#')
c[0] = 4
print('c - ', c)
# [4, 2, 3, 4]
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
# [4, 'a', 'b', 'c', 3, 4]
c[1] = ['a', 'b', 'c']
print('c - ', c)
# [4, ['a', 'b', 'c'], 'b', 'c', 3, 4]
c[1:3] = [] # 초기화
print('c - ', c)
# c -  [4, 'c', 3, 4]
del c[3]    # 해당 위치 원소 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)    # [5, 2, 3, 1, 4]
a.append(6) # 끝부분에 삽입
print('a - ', a)    # [5, 2, 3, 1, 4, 6]
a.sort()    # 정렬 (오름차순)
print('a - ', a)    # [1, 2, 3, 4, 5, 6]
a.reverse() # 역정렬 (내림차순)
print('a - ', a)    # [6, 5, 4, 3, 2, 1]
print('a - ', a.index(5))   # 1
a.insert(2, 7)  
print('a - ', a)    # [6, 5, 7, 4, 3, 2, 1]
a.reverse()         # [1, 2, 3, 4, 7, 5, 6]
a.remove(1) # 해당 값을 제거 / del(1) : 1번 인덱스를 제거
print('a - ', a) # [2, 3, 4, 7, 5, 6]
print('a - ', a.pop())  # 6 [2, 3, 4, 7, 5]
# 스택(LIFO) pop() : 맨 마지막 원소를 출력하고 제거
print('a - ', a.pop())  # 5 [2, 3, 4, 7]
a.append(5)
print('a - ', a)    # [2, 3, 4, 7]
print('a - ', a.count(4))   # 4의 개수 : 1
ex = [8, 9]
a.extend(ex)    #.extend() : 연장(원소만 추가가 된다.)
print('a - ', a)    # [2, 3, 4, 7, 8, 9]
a.append(ex)
print('a - ', a)    # [2, 3, 4, 7, 8, 9]
# a.append(ex)  # [2, 3, 4, 7, [8, 9]] : 리스트 자체가 추가가 된다

# 리스트 컴프리헨션
list_comp = [i for i in range(10)]
print(list_comp) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_comp2 = [i for i in range(10) if i % 2 == 0]
print(list_comp2) # [0, 2, 4, 6, 8]

list_comp3 = [i * i for i in range(10)]
print(list_comp3) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# n * m 크기의 2차원 리스트 초기화
n = 4
m = 3
list_comp4 = [[0] * m for _ in range(n)]
print(list_comp4) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


# 삭제 remove(해당 원소를 제거), pop(마지막 원소 출력 후 제거), del(인덱스)

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)

# 튜플 자료형(순서O, 중복O, 수정X, 삭제X)
# 변경되지 않는 중요한 정보들을 저장할 때 사용

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#')
print('d - ', type(d), d) # (10, 100, 'Pen', 'Cap', 'Plate')
print('d - ', d[1]) # 100
# print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])    # 'Plate'
print('e - ', e[-1][1]) # 'Cap'
# print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))   # ['C', 'a', 'p']
print('e - ', tuple(e[-1][1]))   # ('C', 'a', 'p')

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])   # (10, 100, 'Pen')
print('d - ', d[2:])    # ('Pen', 'Cap', 'Plate')
print('e - ', e[2][1:3])# ('Cap', 'Plate')

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)    # (1, 2, 3, 4, 10, 100, 'Pen', 'Cap', 'Plate')
print('c * 3 - ', c * 3)    # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))    # hi1

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)    # (5, 2, 3, 1, 4)
print('a - ', a.index(5)) # 3 원소의 index : 0
print('a - ', a.index(3)) # 3 원소의 index : 2
print('a - ', a.count(4)) # 4의 개수 : 1
