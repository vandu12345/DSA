

def dectobin(number, result):
    if number == 0:
        return result
    
    result = str(number % 2) + result
    return dectobin(number//2, result)


print(dectobin(333, ""))