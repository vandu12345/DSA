
def merge(arr, start, mid, end):
    temp_array = [0]*(end-start+1)
    
    i = start
    j = mid+1
    k = 0
    
    while i <=mid and j <=end:
        if arr[i] < arr[j]:
            temp_array[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_array[k] = arr[j]
            k+=1
            j+=1
    
    while i <= mid:
        temp_array[k] = arr[i]
        k+=1
        i+=1
    
    while j <=end:
        temp_array[k] = arr[j]
        k+=1
        j+=1
    
    
    for i in range(start, end+1):
        arr[i] = temp_array[i-start]

def merge_sort(arr, start, end):
    
    if start < end :
        mid = (end + start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

arr = [1,5,2,4,3,-9,6]
merge_sort(arr, 0, 6)
print(arr)
        
a = N
         