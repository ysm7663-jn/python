N, M = map(int, input().split())
data_list = list(map(int,input().split()))

count = 0

for i in range(len(data_list)):
    for j in range(i+1, len(data_list)):
        if data_list[i] == data_list[j]:
            pass
        else:
            count += 1
print(count)

"""
# itertools 라이브러리 사용 (combinations(조합))
from itertools import combinations

result = 0

for a, b in list(combinations(data_list, 2)):
    if a != b:
        result += 1

print(result)
"""