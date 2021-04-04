# 1번

for i in range(1, 9):
    if (i % 3 != 0):
        print(i * '*')
        
# 2번
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(lambda x: str(int(x) + 1), a))
print(a)

# 3번
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
for sport in set(a):
    print(sport, a.count(sport))

# 4번
x = 0
for _ in range(12):
    print(x, end=' ')
    if x == 0:
        x += 1
    elif x < 256:
        x *= 2