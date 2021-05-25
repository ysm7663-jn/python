N = int(input())

list = input()

result = 0

if list.count('L') >= 1:
    result = (list.count('L') // 2) + list.count('S') + 1
else:
    result = list.count('S')
print(result)
"""
N = int(input()) 
member = input() 
count = member.count('LL') 

if (count <= 1): 
    print(len(member)) 

else: 
    print(len(member) - count + 1)
"""
