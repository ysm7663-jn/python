N, M, K = map(int, input().split())

data_list = list(map(int, input().split()))

data_list.sort(reverse=True)

result = 0

first = data_list[0]
second = data_list[1]

while True:
    for i in range(K):
        if M == 0:
            break
        else:
            result += first
            M -= 1
    if M == 0:
        break
    else:
        result += second
        M -= 1
print(result)
