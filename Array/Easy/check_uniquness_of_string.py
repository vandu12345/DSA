
def is_unique(string):
    checker = 0
    for v in string:
        val = ord(v) - ord('a')
        if (checker & (1<<val)) > 0:
            return False
        
        checker =checker | (1<<val)
        
    return True

is_unique("madam")