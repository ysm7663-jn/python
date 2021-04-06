N = int(input())

answer = 0

for i in range(N) :
    word = input()
    for j in range(len(word)) :
        if j != len(word) - 1: # 마지막 단어가 아니면
            if word[j] == word[j+1] : # 다음 단어가 같은 단어
                pass
            elif word[j] in word[j+1:] : # 그 뒤로 같은 단어가 있다면 종료
                break
        else :
            answer += 1
print(answer)
