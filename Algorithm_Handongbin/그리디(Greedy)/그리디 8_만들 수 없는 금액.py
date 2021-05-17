N = int(input())
data = list(map(int, input().split()))
"""
sum_list = []
count = 0
answer = 0
sum = 0

for i in range(len(data)):
    sum_list.append(data[i])
    sum = data[i]
    for j in range(i+1, len(data)):
        sum_list.append(data[i]+data[j])
        sum += data[j]
        sum_list.append(sum)

while True:
    count += 1

    if count not in sum_list:
        answer = count
        break

print(answer)
"""

data.sort()
target = 1

for i in data:
    print(i, target)
    if i > target:
        break
    target += i
print(target)

"""
주어진 화폐로 해당 금액을 만들 수 있을까?
"""

M = int(input())
pays = list(map(int,input().split()))
coin = int(input()) # 만들어야하는 금액

pays.sort()

target = 1
start = 0

for x in pays:
    if x > target:
        start = x       # target 보다 x 값이 크다면 x ~ x + target -1 는 만들 수 있음
    target += x

    if target > coin:
        break

if start <= coin < target:
    print('yes')
else:
    print('no')

# 입력 예시
# M = 3 / pays = 1, 3, 5 / coin = 9   >>> yes
# M = 3 / pays = 1, 2, 4 / coin = 9   >>> no