# heapq 라이브러리
# 주로 다익스트라 알고리즘에서 사용(우선순위 큐 기능)
# heapq > PriorityQueue  

# 최소힙으로만 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료 (최상단 원소 = 가장 작은 원소)
# 삽입 : heapq.heappush()
# 출력 : heapq.heappop()

import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
