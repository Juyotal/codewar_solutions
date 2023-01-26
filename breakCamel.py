def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
    

def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr