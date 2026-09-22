def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    res = []
    # if len(a) == 0:
    #     return 0

    row = len(a)
    col = len(a[0])

    for colindex in range(col):
        l =[]
        for rowindex in range(row):
            l.append(a[rowindex][colindex])
        res.append(l)

    return res


    #pass