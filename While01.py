def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    n=0
    a=0
    while len(s)>n:
        if s[n].isdigit():
            a+=1
        n+=1 
    return a
print(main("diyo1111r"))