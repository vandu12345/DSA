# Insertion Sort Algo

# Take an element and place that element in the correct place in present array 

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         index = i
#         while index>0 and arr[index]<=arr[index-1]:
#             arr[index],arr[index-1] = arr[index-1],arr[index]
#             index-=1


def insertion_sort(arr,itr,length):
    if length == itr:
        return
    
    index = itr
    while index>0 and arr[index]<=arr[index-1]:
        arr[index],arr[index-1] = arr[index-1],arr[index]
        index-=1
        
    insertion_sort(arr,itr+1,length)
        
# arr = [6,8,9,12,14,15,13]
arr = [13,24,46,52,20,9]

insertion_sort(arr,0,len(arr))

print(arr)
        
        
        
            