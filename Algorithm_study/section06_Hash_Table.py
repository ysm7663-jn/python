"""
6. 해쉬 테이블 (Hash Table)
: 키에 데이터를 저장하는 데이터 구조
    - Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
    - 파이썬 딕셔너리 타입이 해쉬 테이블의 예 >> Key를 가지고 바로 데이터(Value)를 꺼냄
    - 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용(공간과 탐색 시간을 맞바꾸는 기법)
    - 단, 파이썬에서는 해쉬를 별도로 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨

1) 용어
해쉬 : 임의 값을 고정 길이로 변환하는 것
해쉬 테이블 : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조(해쉬 값 + 슬롯)
해싱 함수 : Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
해쉬 값(해쉬 주소) : Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
슬롯 : 한 개의 데이터를 저장할 수 있는 공간
저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

2) 해쉬 테이블 생성
"""
"""
hash_table = list([0 for i in range(10)])   # list-Comprehension
print(hash_table)

# Division 방식
def hash_func(key) :
    return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() : 문자의 아스키코드를 리턴
# unicode
print(ord(data1[0]))    # 65 A
print(ord(data2[0]))    # 68 D
print(ord(data3[0]))    # 84 T

print(ord(data1[0]))    # 65 A
print(hash_func(ord(data1[0])))    # ord() : 키 값(65) / data1[0] : 데이터 값(0)

def storage_data(data, value) :
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy', '01011112222')
storage_data('Dave', '01033334444')
storage_data('Trump', '01055556666')

def get_data(data) :
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy')) # 01011112222
"""
"""
2) 장/단점
장점 
    - 데이터 저장/읽기 속도가 빠르다
    - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
단점
    - 일반적으로 저장공간이 좀 더 많이 필요하다
    - 여러 키에 해당하는 주소가 동일한 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
주요 용도
    - 검색이 많이 필요한 경우
    - 저장, 삭제, 읽기가 빈번한 경우
    - 캐쉬 구현시 (중복 확인이 쉽기 때문)
"""

# 연습 1: 리스트 변수를 활용해서 해쉬 테이블 구현
hash_table = list([i for i in range(8)])

def get_key(data) :
    return hash(data)

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data) :
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('ABC', '0123456789')
save_data('def', '9876543210')
print(read_data('ABC'))
print(read_data('def'))

""" 
3) 충돌(Collision) 해결 알고리즘
3-1) Chaining 기법
    - 개방 해슁(Open Hashing) : 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
    > 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법\
"""

# 3-1 연습
hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 들어가 있다
        for index in range(len(hash_table[hash_address])) :
            if hash_table[hash_address][index][0] == index_key :
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])                
    else :
        hash_table[hash_address] = [[index_key, value]]

def read_data(data) :
    index_key = get_key(data)
    print(index_key)
    hash_address = hash_function(index_key)
    print(hash_address)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key :
                return hash_table[hash_address][index][1] 
        return None
    else :
        return None


print(hash('David') % 8)
print(hash('Dd') % 8)

print('----------')
save_data('Dd', '1201023010')
save_data('David', '3301023010')

print(hash_table)
print(read_data('Dd'))
print(read_data('David'))

print('---------------------')
""" 
3) 충돌(Collision) 해결 알고리즘
3-2)  Linear Probing 기법
    - 폐쇄 해슁(Close Hashing) : 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
    : 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
    > 저장공간 활용도를 높이기 위한 기법
"""
hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 들어가 있다
        for index in range(hash_address, len(hash_table)) :
            if hash_table[index] == 0 :
                hash_table[index] = [[index_key, value]]
                return
            elif hash_table[index][0] == index_key :
                hash_table[index][1] = value
                return
    else :
        hash_table[hash_address] = [index_key, value]

def read_data(data) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 존재한다면
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None

            elif hash_table[index][0] == index_key :
                return hash_table[index][1]
    else : # 데이터가 존재하지 않음
        return None

print(hash('dk') % 8)
print(hash('da') % 8)
print(hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '33333333333')
print(read_data('dc'))
print(read_data('dk'))
print(read_data('da'))

"""
3) 충돌(Collision) 해결 알고리즘
3-3) 빈번한 충돌을 개선하는 기법
    해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대

* 해쉬 함수와 키 생성 함수
SHA1 : 고정된 길이의 해쉬 함수 제공
SHA256 : SHA1 보다 더 긴 해쉬 공간 제공
>> 블록체인에 사용됨
"""
"""
import hashlib
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.updata(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

import hashlib
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.updata(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
"""

import hashlib

hash_table = list([0 for i in range(8)])

def get_key(data) :
    hash_object = hashlib.sha256()
    hash_object.object.hexdigest()
    return int(he_dig, 16)

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 들어가 있다
        for index in range(hash_address, len(hash_table)) :
            if hash_table[index] == 0 :
                hash_table[index] = [[index_key, value]]
                return
            elif hash_table[index][0] == index_key :
                hash_table[index][1] = value
                return
    else :
        hash_table[hash_address] = [index_key, value]

def read_data(data) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 데이터가 존재한다면
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None

            elif hash_table[index][0] == index_key :
                return hash_table[index][1]
    else : # 데이터가 존재하지 않음
        return None

print(get_key('db') % 8)
print(get_key('da') % 8)
print(get_key('dh') % 8)

"""
6. 시간 복잡도
    - 일반적인 경우(충돌이 없는 경우) : O(1) / 보통 O(1) 이라고 한다.
    - 최악의 경우(충돌이 있는 경우) : O(n)
"""