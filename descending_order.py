def descending_order(num):
    # Bust a move right here
    num_str = str(num)
    digits = []
    
    for i in num_str:
        digits.append(i)
        
    digits.sort(reverse = True)
    print(digits)
    
    return int("".join(digits))