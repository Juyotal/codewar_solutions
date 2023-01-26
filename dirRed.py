def dirReduc(arr):
    opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    
    stack = []
    
    for elt in arr:
        if len(stack) == 0 or opposite[elt] != stack[-1]:
            stack.append(elt)
        else:
            stack.pop()
    return stack
            