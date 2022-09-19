def digital_root(n):
    # ...    
    n_str = str(n)
    
    if len(n_str) == 1:
        return n
    
    n = get_sum(n)
    
    return digital_root(n)
    
def get_sum(n):
    print(1)
    sum = 0
    n_str = str(n)
    
    for i in n_str:
        sum += int(i) 
    return sum