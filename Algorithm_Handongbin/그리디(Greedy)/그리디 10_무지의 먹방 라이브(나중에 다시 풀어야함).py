def solution(food_times, k):
    answer = 0
    count = 0

# 15, 20, 29, 30, 32 통과
    while True:

        if sum(food_times) <= 0:
            return -1

        for i in range(len(food_times)):
            num = i
            print('num',num)
            if count < k:
                if food_times[i] != 0:
                    food_times[i] -= 1
                    count += 1
                else:
                    continue
            else:
                if num != 0:
                    return num
                else:
                    for j in range(len(food_times)):
                        if food_times[j] != 0:
                            return j + 1
       

print(solution([3, 1, 2], 5))
print(solution([5, 3, 3], 5))
print(solution([5, 3, 3], 7))
print(solution([1, 1, 1], 5))
