# Find Second largest element


def print2largest(arr, n):
    if n==1:
        return arr[0]
    
    array_set = set(arr)
    array = list(array_set)
    diff = len(arr) - len(array)
    
    for i in range(2):
        for j in range(n-i-1):
            if array[j]>=array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                
                
    return array[n-2-diff]

arr = [12,35,1,10,34,1]
second_max = print2largest(arr,6)
print(second_max)