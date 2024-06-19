

def natural_sum(n, total_sum):
    if n == 0:
        return 0
    
    total_sum = n + natural_sum(n-1, total_sum)
    return total_sum

print(natural_sum(10, 0))