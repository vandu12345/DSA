
def rev_arr(arr, i , n):
    if i>=n:
        return
    arr[i],arr[n] = arr[n],arr[i]
    rev_arr(arr,i+1, n-1)

arr = list(range(1,40,2))
rev_arr(arr, 0, len(arr)-1)

print(arr)