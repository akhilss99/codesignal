def matrixElementsSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    s = 0
    for j in range(n):
        for i in range(m):
            if(matrix[i][j] == 0):
                break
            s += matrix[i][j]
            i+=1
        j+=1

    print(s)
    return s

if __name__ == "__main__":
    assert matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]) == 9
    assert matrixElementsSum([[1, 3, 1, 2], [1, 5, 1, 10], [2, 0, 3, 3]]) == 32
    assert matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]) == 9
    assert matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]) == 9

