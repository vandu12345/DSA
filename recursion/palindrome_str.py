

def palindrome_str(element):
    if len(element) == 0 or len(element) == 1:
        return True
    
    if element[0] == element[len(element) -1]:
        return palindrome_str(element[1:len(element) -1])

    return False

print(palindrome_str("mad"))