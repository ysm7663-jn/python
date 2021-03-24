def solve(arr : list) -> int :
    ans = sum(arr)
    return ans

N = int(input())

arr = list(map(int, input().split()))

print(solve(arr))

def solve(num_list) : 
    result = sum(num_list)
    return result