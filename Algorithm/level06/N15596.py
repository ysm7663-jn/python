# 함수 구현
def solve(arr : list) -> int :
    ans = sum(arr)
    return ans

N = int(input())

arr = list(map(int, input().split()))

print(solve(arr))

# 백준 정답
def solve(num_list) : 
    result = sum(num_list)
    return result