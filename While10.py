def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    k=0
    while a<len(s):
        if int(s[a])%2==1:
            k+=int(s[a])
        a+=1
    return k
print(main("123457"))
