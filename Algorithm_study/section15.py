""" 
4. 퀵 정렬 (quick sort)
: 기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right)으로 모으는 함수를작성
: 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
: 함수는 왼쪽 + 기준점 + 오른쪽
"""
# qsort가 하나 이상일 때
def qsort(data):

    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot] + qsort(right)

import random

data_list = random.sample(range(100), 10)

print(qsort(data_list))

# list comprehension 사용
def qsort_list(data):

    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

data_comprehension = random.sample(range(100), 10)

print(qsort_list(data_comprehension))

"""
알고리즘 분석
시간복잡도 : O(n log n)
    - 최악의 경우 : O(n^2)