
class Solution: 
    def select(self, arr, i):
        pass
        # code here 
    
    def selectionSort(self, arr,n):
        #code 
        n = len(arr)
        for i in range(n-1):
            index = i
            for j in range(i,n):
                if arr[index]>=arr[j]:
                    index = j
                arr[i],arr[index] = arr[index],arr[i]

