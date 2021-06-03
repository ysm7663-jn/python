N, M = map(int, input().split())
apple = int(input())

result = 0
now = 1

for i in range(apple):
    fall = int(input())

    while True:
        if fall > now and fall not in range(now, now+M):
            now += 1
            result += 1
        elif fall < now:
            now -= 1
            result +=1
        else:
            break
print(result)