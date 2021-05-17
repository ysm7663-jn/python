# 내 답안
"""
data = input()
int_data = []
for i in data:
    int_data.append(int(i))

result = 0

if int_data[0] == 0:
    result = int_data[1]
    for i in range(2, len(int_data)):
        result *= int_data[i]
else:
    result = int_data[0]
    for i in range(1, len(int_data)):
        result *= int_data[i]

print(result)

# >> 처음 0 일때는 정답이 나오지만, 그 이후 자리에 0이 나올경우 0이 곱해져 결과가 0이 나옴 (ex 02503)

"""
# 모범 답안
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)