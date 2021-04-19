def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = list(set(nums))
    
    for i in nums:
        if answer < length:
            answer += 1
    
    return answer

nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]	

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))