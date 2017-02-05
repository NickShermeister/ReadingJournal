import dictionary

def recurse_is_palindrome(wordin2):
    if len(wordin2)>=2:
        if wordin2[0] == wordin2[-1]:
            return recurse_is_palindrome(wordin2[1:-1])
        else:
            return False
    elif len(wordin2) <= 1:
        return True
def palindromes(dict):
    allPals = []
    for x in dict:
        if recurse_is_palindrome(x):
            allPals.append(x)
    return allPals
