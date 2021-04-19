N = int(input())

for i in range(N) :
    M, arr = input().split()
    for j in arr :
        for k in range(int(M)) :
            print(j, end='')
    print()