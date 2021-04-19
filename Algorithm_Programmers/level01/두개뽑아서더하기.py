def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = sorted(list(set(answer)))

    return answer

numbers1 = [2, 1, 3, 4, 1]
numbers2 = [5, 0, 2, 7]
print(solution(numbers1))
print(solution(numbers2))