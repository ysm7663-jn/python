input_str = list(input().upper())

alpha_dict = {
    '1' : '2',
    'A' : '3',
    'B' : '3',
    'C' : '3',
    'D' : '4',
    'E' : '4',
    'F' : '4',
    'G' : '5',
    'H' : '5',
    'I' : '5',
    'J' : '6',
    'K' : '6',
    'L' : '6',
    'M' : '7',
    'N' : '7',
    'O' : '7',
    'P' : '8',
    'Q' : '8',
    'R' : '8',
    'S' : '8',
    'T' : '9',
    'U' : '9',
    'V' : '9',
    'W' : '10',
    'X' : '10',
    'Y' : '10',
    'Z' : '10',
    '0' : '11'
}

new_alpha_keys = list(alpha_dict.keys())
new_alpha_values = list(alpha_dict.values())

idx = 0
sum = 0

for i in input_str :
    for j in new_alpha_keys :
        if i == j :
            idx = new_alpha_keys.index(j)
            sum += int(new_alpha_values[idx])
print(sum)