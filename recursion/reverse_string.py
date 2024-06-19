

def reverse_string(element):
    if element == "":
        return ""

    return reverse_string(element[1:]) + element[0]


print(reverse_string("hello"))    