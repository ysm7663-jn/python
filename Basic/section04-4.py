# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

# 선언
a = {
    'name': 'Kim', 
    'phone': '01012345678', 
    'birth': '870124'
}  
b = {0: 'Hello python!', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4]}
# 리스트, 튜플과 같이 모든 것들을 넣을 수 있음

print('a - ', type(a), a) # <class 'dict'> {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
print('b - ', type(b), b) # <class 'dict'> {0: 'Hello python!'}
print('c - ', type(c), c) # <class 'dict'> {'arr': [1, 2, 3, 4]}

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생 / # Kim
print('a - ', a.get('name'))  # 존재X -> None 처리 / #Kim (안전하게 접근)
print('b - ', b[0]) # Hello Python!
print('b - ', b.get(0)) # Hello Python!
print('c - ', c['arr']) # [1, 2, 3, 4]
print('c - ', c['arr'][3])  # 4
print('c - ', c.get('arr')) # [1, 2, 3, 4]

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'seoul'}
a['rank'] = [1, 2, 3] # 리스트 추가
print('a - ', a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'seoul', 'rank': [1, 2, 3]}
a['rank'] = (1, 2, 3) # 튜플 추가
print('a - ', a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'seoul', 'rank': (1, 2, 3)}

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys()) # a -  dict_keys(['name', 'phone', 'birth', 'address', 'rank'])
print('b - ', b.keys()) # dict_keys([0, 1])
print('c - ', c.keys()) # dict_keys(['arr'])
# print(a.keys()[0]) : 에러 >> 리스트 형태이지만 리스트가 아니기 때문
print('a - ', list(a.keys())) # a - ['name', 'phone', 'birth', 'address', 'rank']
print('a - ', tuple(a.keys())) # a - ('name', 'phone', 'birth', 'address', 'rank')
print('b - ', list(b.keys())) # b - [0, 1]
print('c - ', list(c.keys())) # c - ['arr']

temp = list(a.keys())
print('a - ', temp[1:3]) # ['phone', 'birth']

print('a - ', a.values()) # a -  dict_values(['Kim', '01012345678', '870124', 'seoul', (1, 2, 3)])
print('b - ', b.values()) # b -  dict_values(['Hello python!', 'Hello Coding'])
print('c - ', c.values()) # c -  dict_values([[1, 2, 3, 4]])

print('a - ', list(a.values())) # a -  ['Kim', '01012345678', '870124', 'seoul', (1, 2, 3)]
print('a - ', tuple(a.values())) # a -  ('Kim', '01012345678', '870124', 'seoul', (1, 2, 3))
print('b - ', list(b.values())) # b -  ['Hello python!', 'Hello Coding']
print('c - ', list(c.values())) # c -  [[1, 2, 3, 4]]

# items : (key, value) 와 같이 튜플의 형태를 띔
print('a - ', a.items()) # a -  dict_items([('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', (1, 2, 3))])
print('b - ', b.items()) # b -  dict_items([(0, 'Hello python!'), (1, 'Hello Coding')])
print('c - ', c.items()) # c -  dict_items([('arr', [1, 2, 3, 4])])

print('a - ', list(a.items())) # [('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', (1, 2, 3))]
print('a - ', tuple(a.items())) # (('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', (1, 2, 3)))
print('b - ', list(b.items())) # [(0, 'Hello python!'), (1, 'Hello Coding')]
print('c - ', list(c.items())) # [('arr', [1, 2, 3, 4])]

print('a - ', 'name' in a) # True
print('a - ', 'addr' in a) # False

# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a) # a -  <class 'set'> set()
print('b - ', type(b), b) # b -  <class 'set'> {1, 2, 3, 4}
print('c - ', type(c), c) # c -  <class 'set'> {1, 4, 5, 6}
print('d - ', type(d), d) # d -  <class 'set'> {1, 2, 'Plate', 'Cap', 'Pen'}

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t) # t -  <class 'tuple'> (1, 2, 3, 4)
print('t - ', t[0], t[1:3]) # t- 1 (2, 3) 

# 리스트 변환
l = list(c)
print('l - ', type(l), l) # l -  <class 'list'> [1, 4, 5, 6]
print('l - ', l[0], l[1:3]) # l - 1 [4, 5]

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ', s1 & s2) # l - {4, 5, 6}
print('l - ', s1.intersection(s2)) # l - {4, 5, 6}

# 중복 값은 한 번만 출력
print('l - ', s1 | s2) # l - {1, 2, 3, 4, 5 , 6, 7, 8, 9}
print('l - ', s1.union(s2))

print('l - ', s1 - s2) # l - {1, 2, 3}
print('l - ', s1.difference(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5) 
print('s1 - ', s1) # s1 - {1, 2, 3, 4, 5}

s1.remove(2) # 원소가 제거 / del : index가 제거
print('s1 - ', s1) # s1 - {1, 3, 4, 5}