T = int(input())

time = [300, 60, 10]

count = [0 for i in range(3)]
num = T
for i in  range(len(time)):
    count[i] += num // time[i]
    num %= time[i]

sum = 0
for i in range(len(count)):
    sum += count[i] * time[i]

if sum == T:
    for i in count:
        print(i, end=' ')
else:
    print(-1)