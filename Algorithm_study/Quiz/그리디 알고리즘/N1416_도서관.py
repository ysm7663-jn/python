# 문제 중점
# 1. 양수와 음수 부분을 나눠 계산
# 2. 절대값이 가장 큰 부분은 편도로 보낼 수 있도록 미리 설정

# 강의에선 heapq를 활용했지만, 다른 풀이 방법도 존재

import heapq 

N, M = map(int,input().split())

array = list(map(int,input().split()))

plus = []
minus = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), -min(array))

# 최대 힙(Max Heap)을 위해 원소를 음수로 구성
for i in array:
    if i > 0:
        heapq.heappush(plus, -i)
        print('plus',plus)
    else:
        heapq.heappush(minus, i)
        print('minus',minus)

result = 0

while plus:
    # 한 번에 m개씩 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(plus)
    print('plus result', result)
    for _ in range(M - 1):
        if plus:
            a = heapq.heappop(plus)
            print('plus heappop', a)
    
while minus:
    # 한 번에 m개씩 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(minus)
    print('minus result', result)
    for _ in range(M - 1):
        if minus:
            b = heapq.heappop(minus)
            print('minus heappop', b)

# 일반적으로 왕복 거리를 계산하지만, 가장 먼 곳은 편도로 한 번만 계산
print(-result * 2 - largest)