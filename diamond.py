def diamond(n):
    if not n%2 or n<1: return None
    d = [" "*i+"*"*(n-2*i)+"\n" for i in range(n/2,0,-1)]
    return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])