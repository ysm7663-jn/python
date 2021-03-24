"""
for i in range (1,100) :
    for j in range(1, i) :
        ship = j // 10
        ill = j % 10

        if i == j + ship + ill :
            print(i)

    # 생성자가 있는 경우
"""

arr = set(range(1, 10001))  # 중복 값을 제거하고 1 ~ 10000까지 수를 담음
num = set()

for i in range(1, 10001) :
    for j in str(i) : # i의 값을 나누기 위해 str로 형변환 / i = ['8', '5', '0']
        i += int(j) # i = i + int(j) >> 850 + 8 >> 858 + 5 >> 863 + 0 >> 863
    num.add(i) # 863

# num : set 형
self_num = sorted(arr - num) # 1 ~ 10001사이에 num에 들어있는 값들은 빼고 저장
# sorted : 해당 값을 리스트형에 오름차순으로 저장
# self_num : list형태
for i in self_num :
    print(i)
    