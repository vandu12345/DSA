

def fibo(n):
    if n == 1 or n == 0:
        return n
    
    return fibo(n-1) + fibo(n-2)

print(fibo(5))