def check_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    assert check_palindrome("aabaa") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("aka") == True
    assert check_palindrome("akka") == True
    assert check_palindrome("a") == True
    assert check_palindrome(" ") == True
    assert check_palindrome("") == True