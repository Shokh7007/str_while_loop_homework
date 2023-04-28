def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    k=0
    while a<len(s):
       k+=int(s[a])
       a+=1
    return k
print(main("12345987654321"))
