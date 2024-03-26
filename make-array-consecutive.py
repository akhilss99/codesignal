def make_array_consecutive_2(statues):
    st = set(statues)
    min_value = float("inf")
    max_value = float("-inf")
    for i in st:
        min_value = min(min_value, i)
        max_value = max(max_value, i)
    counter = 0
    for i in range(min_value, max_value + 1):
        if i not in st:
            counter += 1
    return counter

if __name__ == "__main__":
    assert make_array_consecutive_2([6, 2, 3, 8]) == 3
    assert make_array_consecutive_2([1, 3, 5]) == 2
    assert make_array_consecutive_2([2, 4, 1000]) == 996
    assert make_array_consecutive_2([1, 2, 3]) == 0
    assert make_array_consecutive_2([45]) == 0