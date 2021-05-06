def solution(array, commands):

    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]

        temp = list(array[start:end])
        temp.sort()

        find = commands[i][2]-1
        
        answer.append(temp[find])

    return answer 

"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""
"""
for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
"""

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))