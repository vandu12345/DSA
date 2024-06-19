def first_n_sum(n, sum):
    if n<1:
        return sum
    
    sum = n + first_n_sum(n-1, sum)
    return sum


print(first_n_sum(10,0))