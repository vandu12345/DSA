# Selection Sort Algo

# Select minimum element and place it at the beginning of the array

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        index = i
        for j in range(i,n):
            if arr[index]>=arr[j]:
                index = j
                
        arr[i],arr[index] = arr[index],arr[i]
        
        
arr = [1,3,2,5,4]

selection_sort(arr)

print(arr)
        
        
        
            