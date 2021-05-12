# itertools : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

data = ['A', 'B', 'C']

# 1) permutations(순열) >> 리스트 or iterable 객체에서 r개의 데이터를 뽑아 일렬로 나여하는 경우를 계산
from itertools import permutations
result1 = list(permutations(data, 3))
print(result1) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 2) combinations(조합) >> 리스트 or iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 일렬로 나열하는 경우를 계산
from itertools import combinations
result2 = list(combinations(data, 2))
result2_1 = list(combinations(data, 3))
print(result2) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(result2_1) # [('A', 'B', 'C')]

# 3) product(순열, 중복 허용) >> 리스트 or iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산(단, 원소를 중복하여 뽑는다)
from itertools import product
result3 = list(product(data, repeat=2))
result3_1 = list(product(data, repeat=3))
print(result3) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(result3_1) # [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'A', 'C'), ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'), ('C', 'A', 'A'), ('C', 'A', 'B'), ('C', 'A', 'C'), ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'), ('C', 'C', 'A'), ('C', 'C', 'B'), ('C', 'C', 'C')]

# 4) combinations_with_replacement(조합, 중복 허용) >> 리스트 or iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 일렬로 나열하는 경우를 계산(단, 원소를 중복하여 뽑는다)
from itertools import combinations_with_replacement
result4 = list(combinations_with_replacement(data, 2))
print(result4) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]