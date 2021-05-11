import sys
from collections import Counter

N = int(sys.stdin.readline())

data_list = []
for i in range(N):
    data_list.append(int(sys.stdin.readline()))

data_list.sort()
# 1번
print(round(sum(data_list) / N))

# 2번
print(data_list[N // 2])

# 3번
# Counter(list) : 데이터 개수를 셀 때 사용, 딕셔너리 형태
# most_common : 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
nums_s = Counter(data_list).most_common()

if len(nums_s) > 1: # 빈도수가 높은 데이터의 개수가 2개 이상인 경우
    if nums_s[0][1] == nums_s[1][1]: # 첫 번째와 두번째 데이터의 빈도가 같은 경우
        print(nums_s[1][0]) # 두 번째 데이터 출력
    else:
        print(nums_s[0][0]) # 첫 번째 데이터 출력
else:
    print(nums_s[0][0]) # 빈도수가 높은 데이터의 개수가 1개인 경우, 가장 높은 데이터 출력

# 4번
print(data_list[-1] - data_list[0])