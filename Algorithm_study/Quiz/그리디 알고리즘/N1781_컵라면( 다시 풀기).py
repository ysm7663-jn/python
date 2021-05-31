import heapq

N = int(input())

array = []

for _ in range(N):
    x, y = map(int,input().split())
    array.append((x, y))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
print(sum(queue))