def solution(a, b):
    answer = 1234567890

    result = []

    for i in range(len(a)):
        result.append(a[i]*b[i])
    
    answer = sum(result)

    return answer

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
print(solution(a, b))

c = [-1, 0, 1]
d = [1, 0, -1]
print(solution(c, d))