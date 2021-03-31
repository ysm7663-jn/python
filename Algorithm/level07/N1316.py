N = int(input())

count = 0

for i in range(N) :
    word = input()
    error = 0
    for j in range(len(word)-1) :
        if word[j] != word[j+1] : # 만약 지금 단어와 다음 단어가 다를 경우, 그룹 단어가 아니다
            new_word = word[j+1]  # 지금 단어 이후의 단어를 새로운 단어로 지정
            if new_word.count(word[j]) > 0 : # 새로운 단어에서 지금 단어와 같은 수가 있는지 확인
                error += 1  # 같은 단어가 있을 경우 ++
    if error == 0 :
        count += 1
print(count)