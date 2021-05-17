# 유용한 자료구조를 제공해주는 표준 라이브러리

# deque
# 큐 구현에 사용됨

# 리스트 자료형 : 중간의 특정한 원소를 삽입하는것이 가능
# deque : 인덱싱, 슬라이싱 기능 사용할 수 없음

# 리스트 자료형 : 삽입(append()), 삭제(pop()) >> 가장 뒤쪽 원소 기준
# deque : 가장 앞쪽 삽입(appendleft()), 가장 뒤쪽 삽입(append()), 가장 앞쪽 삭제(leftpop()), 가장 뒤쪽 삭제(pop())

"""
                            리스트      deque
가장 앞쪽에 원소 추가         O(N)         O(1)
가장 뒤쪽에 원소 추가         O(1)         O(1)
가장 앞쪽에 있는 원소 제거    O(N)         O(1)
가장 뒤쪽에 있는 원소 제거    O(1)         O(1)
"""

from collections import deque

data = deque([2, 3, 4])

# 가장 앞쪽에 데이터 삽입
data.appendleft(1)

# 가장 뒤쪽에 데이터 삽입
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) # [1, 2, 3, 4, 5]

# 가장 뒤쪽의 데이터 삭제
data.pop()
print(data) # deque([1, 2, 3, 4])

# 가장 앞쪽의 데이터 삭제
data.popleft()
print(data) # deque([2, 3, 4])


# Counter
from collections import Counter

counter = Counter(['blue', 'red', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(counter['white']) # 0  >> 없는 경우 0 return
print(dict(counter)) # {'blue': 3, 'red': 2, 'green': 1}  >> 오름차순, 내림차순이 아닌 원소의 순서에 따라 반환