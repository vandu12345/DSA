

def find_one(nums):
    result = 0
    
    for element in nums:
        result = result ^ element
        
    return result




nums = [2,2,1]
