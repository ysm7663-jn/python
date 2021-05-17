s = input()
"""
# 내 풀이 (런타임오류)
result = 0

for i in range(1, len(s)):
    num = int(s[i])

    if s[0] == '0':
        if num == 0:
            pass
        else:
            if s[i+1] == '0':
                result += 1
    
    else: 
        if num == 1:
            pass
        else:
            if s[i+1] == '1':
                result += 1
            
print(result)
"""
            
count0 = 0
count1 = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

print(min(count0, count1))