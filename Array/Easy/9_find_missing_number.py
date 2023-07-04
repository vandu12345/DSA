# FInd Missing number


def find_missing(nums):
    sum = 0
    length = len(nums)
    result = length*(length+1)//2
    
    for element in nums:
        sum+=element
        
    print(result - sum)
    

nums = [3,0,1]

find_missing(nums)