def get_middle(s):
    lengthOfString=len(s)
    if lengthOfString % 2 == 0: 
        startIndex = int((lengthOfString/2)-1)
        endIndex = int((lengthOfString/2)+1)
        return s[startIndex : endIndex]
    else:
        startIndex = int(lengthOfString/2)
        endIndex = int((lengthOfString/2)+1)
        return s[startIndex : endIndex]