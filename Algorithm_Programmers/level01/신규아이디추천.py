def solution(new_id):

    # 1번
    new_id = new_id.lower()

    answer = ''

    # 2번
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3번
    while '..' in answer:
        answer = answer.replace('..','.')

    # 4번
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    # 5번
    answer = 'a' if answer == "" else answer

    # 6번
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7번
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))