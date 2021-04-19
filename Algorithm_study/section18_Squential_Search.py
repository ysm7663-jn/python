# 순차 탐색(Sequential Search)
"""
탐색 : 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미
데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법
"""
# 문제 1. 

"""
from random import *
list_data = list()
for index in range(10):
    list_data.append(randint(1, 100))
"""

import random

def func(data):
    data_list = random.sample(range(100), 10)
    data_list.sort()
    print(data_list)
    for i in range(len(data_list)):
        if data == data_list[i]:
            return True
        else:
            return False
print(func(5))
"""
시간 복잡도 : O(n)  // 최악의 경우 : 리스트 길이가 n일 경우