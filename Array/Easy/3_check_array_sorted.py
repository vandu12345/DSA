# Check whether a array is sorted or not

# 10 < 20 < 30 < 40 < 50 - Ascending
# 50 > 40 > 30 > 20 > 10 - Descending

def sorted_check(arr,n):
    
    flag = 1
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            flag = 0
            break
    
    if i!=0:
        return flag
    flag = 1
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            continue
        else:
            flag = 0
            break
    return flag

arr = [10, 20, 30, 40, 50]
n = 5

print(sorted_check(arr,n))
        
        