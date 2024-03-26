def allLongestStrings(arr):
    m = -10000000000000
    for i in arr:
        m = max(m, len(i))
    
    a = list(filter(lambda x: len(x) >= m, arr))
    print(a)
    return a

if __name__ == '__main__':
    assert allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]) == ["aba", "vcd", "aba"]