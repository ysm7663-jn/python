N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

if max(crane) < max(box):
    print(-1)
    exit()

crane.sort(reverse=True)
box.sort(reverse=True)

positions = [0] * N
checked = [False] * M

result = 0
count = 0

while True:

    if count == len(box):
        break

    for i in range(N):
        while positions[i] < len(box):
            print('i',i)
            if not checked[positions[i]] and crane[i] >= box[positions[i]]:
                print(not checked[positions[i]])
                checked[positions[i]] = True
                count += 1
                positions[i] += 1
                print(positions, count, checked)
                break
            positions[i] += 1
            print('positions2', positions)
            print('---')
    result += 1
print(result)



