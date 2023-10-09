def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len (s):
        if int(s[i])%2==0:
            a+=1
        i+=1
    return a
print(main("56786543250"))