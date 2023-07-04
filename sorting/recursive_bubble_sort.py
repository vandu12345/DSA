# Bubble Sort Algo
# Push the maximum at last by adjacent swap
    

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j]>=arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]


def bubble_sort(arr,length):
    if length == 1:
        return
    
    swap = 0
    for j in range(length-1):
        if arr[j]>=arr[j+1]:
            swap = 1
            arr[j],arr[j+1] = arr[j+1],arr[j]
    
    if swap == 0:
        return
            
    bubble_sort(arr,length-1)
    
    
                
                
                
        
        
arr = [13,24,46,52,20,9]

bubble_sort(arr,len(arr))

print(arr)