# Remove Duplicate from sorted Array


import copy


def remove_duplicate(nums):
    if len(nums)<=1:
        return len(nums)
    result = [nums[0]]
    
    for i in range(1, len(nums)):
        if result[len(result)-1] < nums[i]:
            result.append(nums[i])
    
    for i in range(len(result)):
        nums[i] = result[i]
    return len(result)

nums = [1,1,2]
remove_duplicate(nums)
print(nums)