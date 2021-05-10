def solution(n):
    answer = 0

    result = []

    while True:
        x, y = divmod(n, 3)
        if n < 1:
            break
        else:
            result.append(y)
            n = x

    for i in range(len(result)):
        answer += result[i] * (3 ** (len(result) - (i+1)))
        
    return answer

print(solution(45))
print(solution(125))