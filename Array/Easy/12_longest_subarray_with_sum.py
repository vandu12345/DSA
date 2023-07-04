
def subarray_with_sum(k,nums):
    left = 0
    right = 0
    max_len = 0
    sum = 0
    n = len(nums)
    
    while right < n:
        while left <= right and sum >k :
            sum-=nums[left]
            left+=1
        
        if sum==k:
            max_len = max(max_len,right-left+1)
        
        right+=1
        if right<n:
            sum+=nums[right]
            
    return max_len
    
# nums = [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6]
   
            
            
        
        




nums = [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6]
k = 15


print(subarray_with_sum(k,nums))