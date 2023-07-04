
def find_union(a,b,n,m):
    
    result = []
    
    i = 0
    j = 0
    
    while i<=n-1 and j<=m-1:
        if a[i] <= b[j]:
            if len(result)==0 or result[len(result)-1]!=a[i]:
                result.append(a[i])
            i+=1
        
        else:
            if len(result)==0 or result[len(result)-1]!=b[j]:
                result.append(b[j])
            j+=1
                
        
            
    while i<=n-1:
        if len(result)==0 or result[len(result)-1]!=a[i]:
            result.append(a[i])
        i+=1
    
    while j<=m-1:
        if len(result)==0 or result[len(result)-1]!=b[j]:
            result.append(b[j])
        j+=1
        
    print(list(result))
    
    
a = [2,2,3,4,5]
b = [1,1,2,3,4]

find_union(a,b,len(a),len(b))
        
            