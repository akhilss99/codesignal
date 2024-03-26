import math
def adjacentNumbers(arr):
    n = len(arr)
    '''
    arr[i + 1] % 2 != arr[i] % 2 
    [o, e, o, e]
    [e, o, e, o]
    [1, 4, 2, 7] -> []
    [1, 4/2 = 2, 2/2 = 1, 7/2 = 3/2 = 1/2]
    
    '''
    odd_start = 0
    even_start = 0
    for i in range(1, n):
        if(arr[i - 1] % 2 == arr[i] % 2):
            while arr[i - 1] % 2 != arr[i] % 2:
                arr[i] = math.floor(arr[i]/2)

