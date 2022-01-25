str1 = list(map(str, input()))

if str1[0] == ' ' and str1[len(str1)-1] == ' ' :
    print(str1.count(' ') - 1)
    
elif str1[0] == ' ' or str1[len(str1)-1] == ' ' :
    print(str1.count(' '))
    
else :
    print(str1.count(' ') + 1)