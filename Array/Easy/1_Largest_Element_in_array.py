# Largest Element in the Array/List
import sys
def largest(arr, size):
    max = -sys.maxsize -1
    
    for i in range(size):
        if max<=arr[i]:
            max = arr[i]
            
    return max