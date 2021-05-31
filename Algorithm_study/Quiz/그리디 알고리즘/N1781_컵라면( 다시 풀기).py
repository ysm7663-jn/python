import heapq

N = int(input())

list = []
result = 0

for i in range(N):
    x, y = map(int,input().split())
    list.append((x, y))

list.sort()

queue = []

for i in list:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
print(sum(queue))