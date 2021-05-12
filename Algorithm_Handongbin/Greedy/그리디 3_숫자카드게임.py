import time

start = time.time()
N, M = map(int, input().split())
"""
result = []

for i in range(N):
    data_list = list(map(int, input().split()))
    result.append(min(data_list))
print(max(result))
# 1620795634.2265186
"""
result = 0 
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(time.time())
# 1620795709.0895853