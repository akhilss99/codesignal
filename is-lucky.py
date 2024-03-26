def isLucky(n):
    '''
    len(n) % 2 == 0

    '''
    s = str(n)
    i = 0
    j = len(s) - 1
    first_sum = 0
    second_sum = 0
    while(i < j):
        first_sum += int(s[i])
        second_sum += int(s[j])
        i+=1
        j-=1
    return first_sum == second_sum

if __name__ == '__main__':
    assert isLucky(1230) == True
    assert isLucky(239017) == False
