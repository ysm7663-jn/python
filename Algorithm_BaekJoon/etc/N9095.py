# 1, 2, 3 더하기
N = int(input())

def func(data) :
    if data == 1:
        return 1

    elif data == 2:
        return 2

    elif data == 3:
        return 4

    elif data > 3:
        return func(data - 1) + func(data - 2) + func(data - 3)

    else :
        return

for i in range(N) :
    print(func(int(input())))
