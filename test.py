from math import gcd
def gcdString(A, B):
    
    if A+B != B+A:
        return ''

    len_A = len(A)
    len_B = len(B)
    result_gcd = (gcd(len_A, len_B))

    
    if len_A < len_B:
        return A[0 : result_gcd]
    else:
        return B[0 : result_gcd]


print(gcdString('ababcde','ababcde'))
print(gcdString('ababababab','abab'))
print(gcdString('abababab','abab'))
print(gcdString('fast','campus'))
print(gcdString('abc','bcd'))
print(gcdString('abc','abcabc'))