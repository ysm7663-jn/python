def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))

arr = [2, 36, 1, 3]
divisor = 1
print(solution(arr, divisor))

arr = [3, 2, 6]
divisor = 10
print(solution(arr, divisor))