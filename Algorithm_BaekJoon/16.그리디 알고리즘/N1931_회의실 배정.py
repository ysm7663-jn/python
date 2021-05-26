import sys

n = int(sys.stdin.readline())

data = []

"""
# 내 풀이 >> 시간 초과
# 접근 방식은 맞았지만 lambda를 활용한 각각의 정렬을 따로 해줘야할 듯
for i in range(n) :
    data.append(list(map(int, sys.stdin.readline().split())))
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

data.sort()
# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]

result = []
num = 0
while True:
    count = 1   
    start = data[num][0]
    end = data[num][1]
    for j in range(num+1, len(data)):
        if data[j][0] >= end:
            start = data[j][0]
            end = data[j][1]
            count += 1
    result.append(count)
    num += 1

    if num == len(data):
        break

print(max(result))
"""
for i in range(n):
    first, second = map(int, input().split())
    data.append([first, second])

s = sorted(data, key = lambda x : x[1]) # 종료 시간에 대한 오름차순 정렬
print(s) # [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
# s = sorted(data, key = lambda x : x[0]) # 시작 시간에 대한 오름차순 정렬 
# print(s) [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
# s = sorted(data, key = lambda x : x[1]) # 종료 시간에 대한 오름차순 정렬
# print(s) [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

last = 0
cnt = 0

for i, j in s:
    if i >= last:
       cnt += 1
       last = j
print(cnt) 