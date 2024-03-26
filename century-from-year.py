def centuryFromYear(year):
    century = int(year / 100)
    if(year % 100 != 0):
        return century + 1
    return century

if __name__ == '__main__':
    
    assert centuryFromYear(2005) == 21
    assert centuryFromYear(1905) == 20
    assert centuryFromYear(1700) == 17
    print("Success")