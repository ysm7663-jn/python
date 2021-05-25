N = int(input())

data = list(map(int,input().split()))

result = []
num = 0

while True:

    if num > len(data):
        break

    count = 0

    for i in range(num + 1, len(data)):
        if data[num] > data[i]:
            count += 1
        else:
            break
    num += 1
    result.append(count)
    
print(max(result))