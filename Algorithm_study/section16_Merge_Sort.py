# 5. 병합 정렬 (merge sort)
"""
재귀용법을 활용한 정렬 알고리즘
    1. 리스트 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
    2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
    3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
"""

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1: left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 : left만 남았을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 : right만 남았을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

def merge_split(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)
    left = merge_split(data[:medium])
    right = merge_split(data[medium:])
    return merge(left, right)

import random

data_list = random.sample(range(100), 15)

print(merge_split(data_list))

"""
시간복잡도
각 단계별 : O(n)
총 단계 : O(log n)
∴ 단계별 시간 복잡도  = O(n) * O(log n) = O(n log n)