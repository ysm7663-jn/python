# 과제 1
"""
이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 
인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고, 
target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
출력: True
예시 입력2

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
출력: False
"""
"""
내 답
def searchMatrix(matrix, target):
  if len(matrix) == 1:
    for i in range(len(matrix[0])):
        if matrix[0][i] == target:
            return True
    return False
  elif len(matrix) == 0: 
      return False
  else:
    mid = len(matrix) // 2
    for i in range(len(matrix[mid])):
      if matrix[mid][i] == target:
        return True
      else:
        if matrix[mid][0] > target:
          return searchMatrix(matrix[:mid], target)
        else:
          return searchMatrix(matrix[mid:], target)
    

matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
print(searchMatrix(matrix, 3))
print(searchMatrix(matrix, 13))
"""
def searchMatrix(matrix, target):
    def searchRow(sub_matrix):
        m = len(sub_matrix)
 
        if m == 1:
            return sub_matrix[0]
 
        mid = m // 2
        left = sub_matrix[:mid]
        right = sub_matrix[mid+1:]
 
        if sub_matrix[mid][0] <= target <= sub_matrix[mid][-1]:
            return sub_matrix[mid]
        elif sub_matrix[mid][0] > target:
            return searchRow(left)
        else:
            return searchRow(right)
 
    def searchCol(array):
        n = len(array)
 
        if n == 0:
            return False
 
        if n == 1:
            if array[0] == target:
                return True
            else:
                return False
 
        mid = n // 2
        left = array[:mid]
        right = array[mid+1:]
 
        if array[mid] == target:
            return True
        elif array[mid] > target:
            return searchCol(left)
        else:
            return searchCol(right)
 
    array = searchRow(matrix)
    return searchCol(array)
 
 
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(searchMatrix(matrix, target))
 
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print(searchMatrix(matrix, target))

# 과제 2
"""
두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
가능한 C 중에 가장 긴 문자열을 C로 한다.
위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.

예시입력1
A = 'ababcde'
B = 'ababcde'
출력: 'ababcde'

예시입력2
A = 'ababababab'
B = 'abab'
출력: 'ab'

예시입력3
A = 'abababab'
B = 'abab'
출력: 'abab'

예시입력4
A = 'fast'
B = 'campus'
출력: '
"""
from math import gcd
def gcdString(A, B):
    
    if A+B != B+A:
        return ''

    len_A = len(A)
    len_B = len(B)
    result_gcd = (gcd(len_A, len_B))

    
    if len_A < len_B:
        return A[0 : result_gcd]
    else:
        return B[0 : result_gcd]

print(gcdString('ababcde','ababcde'))
print(gcdString('ababababab','abab'))
print(gcdString('abababab','abab'))
print(gcdString('fast','campus'))
print(gcdString('abc','bcd'))
print(gcdString('abc','abcabc'))
    
# 과제 3
"""
n개의 노드가 있는 그래프가 있다. 각 노드는 1부터 n까지 번호가 적혀있다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성하라.

제한사항

노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

"""
import heapq
 
def solution(n, vertex):
    to_visit = []
    dists = [float('inf')] * (n + 1)
 
    dists[1] = 0
    heapq.heappush(to_visit, (0, 1))
    while len(to_visit) > 0:
        dist, node = heapq.heappop(to_visit)
        adj_list = list(map(lambda x: x[1], filter(lambda x: x[0] == node, vertex)))
        adj_list += list(map(lambda x: x[0], filter(lambda x: x[1] == node, vertex)))
        for adj_node in adj_list:
            if dists[adj_node] > dist + 1:
                dists[adj_node] = dist + 1
                heapq.heappush(to_visit, (dists[adj_node], adj_node))
 
    return dists.count(max(dists[1:]))
 
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))

# 과제 4
"""
마을에 1부터 N의 고유 번호를 가진 사람들이 있다. 소문으로는 마을 사람 중에 마을 판사가 있다고 한다. 마을 판사가 실제로 존재한다면,

마을 판사는 아무도 믿지 않는다.
다른 모든 사람들은 마을 판사를 믿는다.
마을 판사가 있다면 오직 한명 뿐이다.
리스트 trust가 주어졌을 때, trust[i] = [a, b]는 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

마을 판사가 존재한다면 마을 판사의 고유 번호를, 존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.

(단, a가 b를 믿고 b가 c를 믿는다고 할 때, a가 c를 믿는다는 의미는 아니다.)

예시입력

N	trust	출력
2	[[1,2]]	2
3	[[1,3],[2,3]]	3
3	[[1,3],[2,3],[3,1]]	-1
3	[[1,2],[2,3]]	-1
4	[[1,3],[1,4],[2,3],[2,4],[4,3]]	3
"""
def solution(N, trust):
    for i in range(1, N + 1):
        if len(list(filter(lambda x: x[0] == i, trust))) > 0:
            continue
        if len(list(filter(lambda x: x[1] == i, trust))) == N - 1:
            return i
    return -1
 
print(solution(2, [[1,2]])) # 2
print(solution(3, [[1,3],[2,3]])) #3
print(solution(3, [[1,3],[2,3],[3,1]])) #-1
print(solution(3, [[1,2],[2,3]])) #-1
print(solution(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) #3