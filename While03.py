def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len(s):
        if s[i].isalpha():
            a+=1
        i+=1
    b=0
    j=0
    while j<len(s):
        if s[j].isdigit():
            b+=1
        j+=1
    return len(s)-a-b
print(main("#hashtag@$"))