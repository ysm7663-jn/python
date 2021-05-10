def solution(N, stages):
    
    # stages에 있는 값들의 개수 구하기
    stage = {}
    for i in stages:
        stage[i] = stage.get(i, 0) + 1

    # 실패율
    failure = [0] * N
    num = len(stages)
    for i in range(1, N+1):
        if stage.get(i, 0) != 0:
            failure[i-1] = stage[i] / num
            num -= stage[i]

    # 정렬
    answer = []
    num = len(failure)
    for i, item in enumerate(failure):
        m = item
        idx = i
        for j, _item in enumerate(failure[::-1]):
            if _item >= m:
                m = _item
                idx = num-1-j
        answer.append(idx+1)
        failure[idx] = -1

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
#print(solution(4, [4, 4, 4, 4, 4]))