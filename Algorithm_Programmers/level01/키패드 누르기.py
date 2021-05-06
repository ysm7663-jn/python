def solution(numbers, hand):
    answer = ''

    left_hand = 10
    right_hand = 12

    for i in numbers:
        if i in [1, 4, 7]: 
            answer += 'L'
            left_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_hand = i
        else:
            i = 11 if i == 0 else i

            absL = abs(i - left_hand)
            absR = abs(i - right_hand)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right_hand = i
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                left_hand = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = i
                else:
                    answer += 'L'
                    left_hand = i

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))