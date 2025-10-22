def maximalSquare(matrix):
    res = 0
    m = len(matrix)
    n = len(matrix[0])
    flag0 = True
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                if flag0:
                    flag0 = False
                res = max([res, int(matrix[i][j])])
                if i - 1 >= 0 and j - 1 >= 0:
                    temp = min(
                        [int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])]) + 1
                    matrix[i][j] = temp
                    res = max([res, matrix[i][j]])
    if flag0:
        return 0
    return res * res


# def maximalSquare(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     res = 0
#
#     # Convert all to integers once
#     for i in range(m):
#         for j in range(n):
#             matrix[i][j] = int(matrix[i][j])
#
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == 1 and i > 0 and j > 0:
#                 matrix[i][j] = min(
#                     matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]
#                 ) + 1
#             res = max(res, matrix[i][j])
#
#     return res * res


print(maximalSquare(matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))