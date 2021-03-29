arr = input().split()

x = list(map(str, (arr[0])))
y = list(map(str, (arr[1])))

x = list(reversed(x))
y = list(reversed(y))

new_x = []
last_x = 0

new_y = []
last_y = 0

if x > y :
    cnt = 2
    for i in x :
        new_x.append(int(i))
        last_x += int(i) * 10 ** cnt
        cnt -= 1
    print(last_x)

else :
    cnt = 2
    for i in y :
        new_y.append(int(i))
        last_y += int(i) * 10 ** cnt
        cnt -= 1
    print(last_y)






