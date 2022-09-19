def descending_order(num):
    # Bust a move right here
    num_str = str(num)
    digits = []
    
    for i in num_str:
        digits.append(i)
        
    digits.sort(reverse = True)
    
    return int("".join(digits))


def Descending_Order_alternate(num):
    return int("".join(sorted(str(num), reverse=True)))