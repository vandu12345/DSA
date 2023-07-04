
def move_zeroes(nums):
    result_array = []
    
    for element in nums:
        if element!=0:
            result_array.append(element)
            
    
    result_array.extend([0]*(len(nums)-len(result_array)))
    
    for i in range(result_array):
        nums[i] = result_array[i]
        
    
    print(result_array)
        




nums = [0,1,0,3,12]
move_zeroes(nums)