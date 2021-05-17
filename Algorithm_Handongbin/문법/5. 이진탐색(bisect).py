# 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리 제공
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적
# bisect_left(), bisect_right 메서드가 가장 중요하게 사용
# 시간 복잡도 : O(logN)에 동작

# bisect_left() : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right() : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2(4)
print(bisect_right(a, x)) # 4(8)

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할때 효과적
# left_value <= x <= right_value
# 시간 복잡도 : O(logN)

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value) 
    left_value = bisect_left(a, left_value)
    return right_value - left_value

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6