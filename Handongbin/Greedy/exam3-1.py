"""
그리디 알고리즘(Greedy)
- 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 그리디 해법은 그 정당성 분석이 중요
    - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토

- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다
- 코테에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제된다.
"""
# 3-1 거스름돈
# 가장 큰 화폐 단위부터 거슬러 준다
# 화폐의 종류가 K일 때, 소스코드의 시간 복잡도는 O(K)
"""
N = 1260
cnt = 0
arr = [500, 100, 50, 10]

for coin in arr :
    cnt += N // coin
    N %= coin
print(cnt)
"""
# 3-2 1이 될 때까지
# 내 풀이
"""
N, K = map(int, input().split())

cnt = 0

while N != 1 :

    if N % K == 0 :
        N /= K
        cnt += 1
    else :
        N -= 1
        cnt += 1
print(cnt)
"""
# 수업 풀이
# 실행 시간이 (O(logN)) 으로 줄어든다
"""
a, b = map(int, input().split())

result = 0

while True :
    # a이 b로 나누어 떨어지는 수가 될 때까지 빼기
    target = (a // b) * b
    result += (a - target)
    a = target

    # a이 b보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if a < b :
        break

    # b로 나누기
    result += 1
    a //= b

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (a - 1)
print(result)
"""
# 3-3 곱하기 혹은 더하기
"""
arr = input()

result = int(arr[0])

for i in range(1, len(arr)) :
    num = int(arr[i])

    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num

print(result)
"""
# 3-4 모험가 길드
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 그룹 수
count = 0 # 현재 그룹에 참여한 수

for i in data :
    count += 1
    if count >= i :
        result += 1
        count = 0
print(result)
"""
# 3-5 큰 수의 법칙
"""
n, m, k = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

cnt = 0
sum = 0

first = num[-1]
second = num[-2]
while True :

    for i in range(k) :
        if m == 0 :
            break
        sum += first
        m -= 1
    if m == 0 :
        break    
    sum += second
    m -= 1
print(sum)
"""
# 3-6 숫자 카드 게임
"""
n, m = map(int,input().split())

result = 0
for i in range(n) :
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
"""
"""
내가 입력한 값
min_list = []
for i in range(n) :
    for j in range(m) :
        min_list.append(min(data[i]))
result = 0

for i in min_list :
    result = max(min_list)
print(result)
"""

# 3-7 문자열 뒤집기
"""
data = input()

count0 = 0
count1 = 0

if data[0] == '1' :
    count1 += 1
else :
    count0 += 1

for i in range(len(data)-1) :
    if data[i] != data[i+1] :
        if data[i+1] == '1' :
            count0 += 1
        else :
            count1 += 1
print(min(count0, count1))
"""
