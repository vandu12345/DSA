# Insertion Sort Algo

# Take an element and place that element in the correct place in present array 

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        while index>0 and arr[index]<=arr[index-1]:
            arr[index],arr[index-1] = arr[index-1],arr[index]
            index-=1
        
arr = [6,8,9,12,14,15,13]

insertion_sort(arr)

print(arr)
        
        
        
            