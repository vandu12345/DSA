
def consecutive_one(nums):
    max = 0
    count = 0
    for element in nums:
        if element==1:
            count+=1
        
        else:
            if count>=max:
                max = count
                count = 0
                
    if count>=max:
        max = count
    print(max)
        

nums = [1,1,0,1,1,1]
consecutive_one(nums)