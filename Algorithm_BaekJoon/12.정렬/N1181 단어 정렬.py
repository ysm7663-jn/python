N = int(input())

data_list = []

for i in range(N):
    x = str(input())
    y = len(x)
    data_list.append((x, y))
# 중복 제거
data_list = list(set(data_list))
# 단어 숫자 정렬 > 단어 알파벳 정렬
data_list.sort(key=lambda word : (word[1], word[0]))

for word in data_list:
    print(word[0])