N = int(input())

money = [500, 100, 50, 10, 5, 1]

rest = 1000 - N
count = 0
M = 0

while rest > 0:
    count += rest // money[M]
    rest %= money[M]
    M += 1
print(count)