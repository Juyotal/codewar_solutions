def tribonacci(signature, n):
    #your code here
    signature = signature[:n]
    while n > 3:
        wind = signature[-3:]
        signature.append(sum(wind))
        n -=1
        
    return signature


def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res