import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    a=0
    while len(s)>n:
        if s[n] in string.punctuation:
            a+=1
        n+=1
    return a
print(main("asdf!!@#$12345"))



