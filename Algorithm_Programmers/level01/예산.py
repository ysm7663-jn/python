def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
print(solution([5, 7, 1, 10], 5))
print(solution([10], 7))
print(solution([7], 7))
print(solution([5], 7))