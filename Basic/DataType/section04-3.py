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
print('e - ', list(e[-1][1]))

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
del c[3]    # 삭제
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
print('a - ', a)    # [2, 3, 4, 7]
print('a - ', a.count(4))   # 4의 개수 : 1
ex = [8, 9]
a.extend(ex)    #.extend() : 연장(원소만 추가가 된다.)
print('a - ', a)    # [2, 3, 4, 7, 8, 9]
# a.append(ex)  # [2, 3, 4, 7, [8, 9]] : 리스트 자체가 추가가 된다


# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)

# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))
