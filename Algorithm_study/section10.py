"""
2. 선택 정렬
for i in range(len(data) - 1) :
    lowest = i
    for j in range(i + 1, len(data)) :
        if data[lowest] > data[j] :
          lowest = j
    swap (lowest, i)
"""
import random
def selection_sort(data):
    for i in range(len(data)-  1) :
        lowest = i
        for j in range(i + 1, len(data)) :
            if data[lowest] > data[j] :
                lowest = j
                data[lowest], data[i] = data[i], data[lowest]
    return data

data_list = random.sample(range(100), 10)

print(selection_sort(data_list))
""" 
시간 복잡도 : O(n^2)
    n * (n - 1) / 2
"""