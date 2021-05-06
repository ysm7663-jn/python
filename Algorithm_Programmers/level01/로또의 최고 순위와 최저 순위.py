def solution(lottos, win_nums):
    answer = []

    count = 0
    # 최저 점수
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
    answer.append(count)

    # 최고 점수
    for i in range(len(lottos)):
        if lottos[i] == 0:
            cnt = 1
            while True:
                if cnt not in lottos:
                    if cnt in win_nums:
                        count += 1
                        break
                    else:
                        cnt += 1
                else:
                    cnt += 1
        
    answer.append(count)

    for i in range(len(answer)):
        if answer[i] <= 1:
            answer[i] = 6
        elif answer[i] == 2:
            answer[i] = 5
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 5:
            answer[i] = 2
        else :
            answer[i] = 1

    answer.sort()
    return answer
"""
rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
"""

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))