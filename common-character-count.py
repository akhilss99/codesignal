from collections import Counter
def commonCharacterCount(s1, s2):
    s1map = Counter(s1)
    s2map = Counter(s2)
    mutuals = 0
    for i in s1map:
        if i in s2map:
            mutuals += min(s1map[i], s2map[i])
    print(mutuals)
    return mutuals

if __name__ == '__main__':
    assert commonCharacterCount("aabcc", "adcaa") == 3
    assert commonCharacterCount("abc", "aabbcc") == 3
    assert commonCharacterCount("akhihl", "aakjhii") == 4