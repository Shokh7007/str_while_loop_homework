def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    a=0
    while len(s)>n:
        if s[n].isupper():
            a+=1
        n+=1
    return a
print(main("aDsdf1S2345"))