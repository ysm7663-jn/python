n, k = map(int, input().split())

money = []

for i in range(n) :
    money.append(int(input()))

money.reverse()

count = 0

for j in money :
    if n >= 0 :
        count += k // j
        k %= j 
print(count)