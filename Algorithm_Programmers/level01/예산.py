def solution(d, budget):
    answer = 0
    sum = 0

    while True:
        
        sum += d[answer]
        if sum > budget:
            return answer
        elif sum == budget:
            return answer + 1
        else:
            answer += 1

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
print(solution([5, 7, 1, 10], 5))
print(solution([10], 7))
print(solution([7], 7))
print(solution([5], 7))