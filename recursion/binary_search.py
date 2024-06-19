
def binary_search(arr, left, right, number):
    
    if left > right :
        return -1
    
    mid = (left+right)//2
    
    if number == arr[mid]:
        return mid
    
    if number > arr[mid]:
        return binary_search(arr, mid+1, right, number)
    
    
    return binary_search(arr, left, mid-1, number)
    
arr = [1,2,3,5,7,8]
print(binary_search(arr, 0, len(arr)-1, 3))
    
        