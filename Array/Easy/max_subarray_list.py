from typing import List


def maxSubsequence(nums: List[int], k: int) -> List[int]:
    # nums = sorted(nums)
    result = []

    n = len(nums)
    
    summ = 0
    maxx = 0
    if n>k:
        for i in range(k):
            summ+=nums[i]
            result.append(nums[i])
    else:
        return nums
    
    maxx = summ

    for i in range(k,n):
        summ = summ+nums[i]-nums[i-k]
        if summ>maxx:
            maxx=summ
            result.pop(0)
            result.append(nums[i])

    return result

print(maxSubsequence([-1,-2,3,4],3))
