def deriveString(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    if(n1 > n2):
        return False
    
    i = 0
    j = 0
    matching = ""
    while(i < n1 and j < n2):
        if(s1[i] == s2[j]):
            matching += s1[i]
            i += 1
            j += 1
        else:
            j += 1
        
    if(matching == s1):
        return True
    
    return False


if __name__ == "__main__":
    assert deriveString("abcd", "abcdh") == True
    assert deriveString("akhil", "a") == False
    assert deriveString("hello", "world") == False

