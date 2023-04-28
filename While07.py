def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    k=0
    while a<len(s):
        if int(s[a])%2==0:
            k+=1
        a+=1
    return k
print(main("123456789"))