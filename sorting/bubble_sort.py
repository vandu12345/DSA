# Bubble Sort Algo
# Push the maximum at last by adjacent swap
    

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
        
        
arr = [13,24,46,52,20,9]

bubble_sort(arr)

print(arr)
        
        
        
            