import string
def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a=0
    k=0
    while a<len(s):
        if s[a]=='o' or s[a]=='u' or s[a]=='a' or s[a]=='e' or s[a]=='i':
            k+=1
        a+=1
    return k
print(main('7uh6ygt5ftujj87fhef7igj'))
