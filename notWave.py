def wave(people):
    arr = []
    
    for i in range(len(people)):
        result = ""
         
        if people[i] != " ":
            result = people[:i] + people[i].upper() + people[(i+1):]
            arr.append(result)
        
    return arr

def wAve(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]