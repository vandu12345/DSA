# Quick Sort

# Pick a Pivot
def pivot_picker(arr, low, high):
    # Choice of Pivot Can be
    # 1st element of the array
    # Last element of the array
    # median of the array
    # random element of the array
    # 0,7
    # Taking 1st element of the array
    # arr = [4,6,2,5,7,9,1,3]
    pivot = arr[low]
    i = low + 1
    j = high
    
    # 0,0

    # 2
    
    while True:
        # Pick the lesser element than pivot
        while i<=j and arr[i]<=pivot:
                i+=1
        
        while i<=j and arr[j]>pivot:
                j-=1
        if i<j:
            arr[i],arr[j] = arr[j], arr[i]
            
        else:
            break
            
    arr[low],arr[j]  = arr[j],arr[low]
    
    return j

# 0,8
def quick_sort(arr,low,high):
    if low < high:
        partion_index = pivot_picker(arr,low,high)
        quick_sort(arr,low,partion_index-1)
        quick_sort(arr,partion_index+1,high)      


arr = [4,6,2,5,7,9,1,3]
quick_sort(arr,0,len(arr)-1)

print(arr)
            
    