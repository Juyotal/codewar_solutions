def rot13(message):
    result = ''
    for char in message:
        if char.isalpha() and char.isupper():
            result += chr((((ord(char) - 65) + 13) % 26) + 65)
        elif char.isalpha() and char.islower():
            result += chr((((ord(char) - 97) + 13) % 26) + 97)
        else:
            result += char
    return result

