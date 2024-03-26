def adjacentElementsProduct(arr):
    largest = -1000000000
    for i in range(0, len(arr) - 1):
        largest = max(largest, arr[i] * arr[i + 1])
    return largest

if __name__ == '__main__':

    assert adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21
    assert adjacentElementsProduct([1, 2, 3]) == 6
    assert adjacentElementsProduct([0, -1, -1]) == 1
    assert adjacentElementsProduct([0, 0]) == 0
