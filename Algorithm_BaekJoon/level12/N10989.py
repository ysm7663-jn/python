import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

"""
파이썬의 1초 : 2천만개 연산
기본 정렬 라이브러리 시간 복잡도 : N log N

* 데이터의 개수가 많을 때 sys.stdin.readline() 활용

이 문제 유형
데이터의 범위가 작은 경우(범위가 정해저 있는 경우) : 계수 정렬
시간 복작도 : O(N)

pype3 = 시간은 단축되지만 메모리는 많이 잡아 먹음
"""