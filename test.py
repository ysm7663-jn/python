"""
1번 문제.

user_input = input()

data = []
list = []
list.append(int(user_input))
num = user_input
while True:
    

    for i in range(len(num)):
        
        data.append(int(num[i]) ** 2)

    num = sum(data)
    

    if num in(list):
        print(user_input + " is Unhappy Number.")
        break

    elif num == 1:
        print(user_input + " is Happy Number.")
        break

    else:
        list.append(num)
        data = []
        num = str(num)
"""
""" 
2번 문제.
"""
user_input = input()

N, a, b = map(int, input().split())

list = []
result = []

answer = 0

k = 1983

for i in range(1, N):
    a, b = divmod(k *(a + b), 20090711)
    list.append(b)
    if len(list) % 2 == 0:
        mid = len(list) // 2 - 1
    else: 
        mid = len(list) // 2
    result.append(list[mid])
    

    print(result)

answer = sum(result)
print(answer)

