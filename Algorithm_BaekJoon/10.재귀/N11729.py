k = int(input())

def hanoi(k, a, b, c):
    if k == 1:
        print(a, c)
    else:
        hanoi(k - 1, a, c, b)
        print(a, c)
        hanoi(k - 1, b, a, c)

sum = 1
for i in range(k-1):
    sum = sum * 2 + 1
print(sum)

hanoi(k, 1, 2, 3)