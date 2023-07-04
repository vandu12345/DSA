# Merge Sort Algo


def merge(arr,low,mid,high):
    left = low
    right = mid+1
    result = []
    
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            result.append(arr[left])
            left+=1
        else:
            result.append(arr[right])
            right+=1
            
    while left <= mid:
        result.append(arr[left])
        left+=1
            
    while right <= high:
        result.append(arr[right])
        right+=1
        
    for i in range(low,high+1):
        arr[i] = result[i-low]
            
        
           

def merge_sort(arr,low,high):
    if low == high:
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
        
arr = [6,8,9,12,14,15,13]

merge_sort(arr,0,len(arr)-1)

print(arr)
        
        
        
