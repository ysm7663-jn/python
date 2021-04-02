N = int(input())

# 알파벳 빈 배열
alpha = []
for i in range(97, 123) :
    alpha.append(chr(i))

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if alpha.find(word[j]) :  # alpha 배열에 j 단어가 있을 경우
            new_word = 
            print('있다')
            alpha.index(word[j]) = 0 # 해당 단어의 위치를 0으로 초기화
        else :
            print('없다')
            break




