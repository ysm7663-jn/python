def solution(s):
    num_list = [['zero', 0], ['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9]]
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = []
    str_str = ''
    answer = 0

    for i in range(len(s)):
        # 숫자인 경우
        if s[i] in number_list:
            result.append(int(s[i]))
        # 문자열인 경우
        else:
            str_str += s[i]
            for j in range(len(num_list)):
                if str_str in num_list[j]:
                    result.append(num_list[j][1])
                    str_str = ''

    for i in range(len(result)):
        answer += result[i] * 10 ** (len(result) - (i+1))

    return answer

print(solution('one4seveneight'))
print(solution('1234'))
print(solution('23four5six7'))
print(solution('1zerotwozero3'))