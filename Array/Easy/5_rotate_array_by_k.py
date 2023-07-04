from ast import List


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    result_array = [0]*length
    
    for i in range(length):
        result_array[(i+k)%length] = nums[i]
        
    for i in range(length):
        nums[i] = result_array[i]
        
        
nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)