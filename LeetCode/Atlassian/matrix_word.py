def find(curr, word, m, n, board, visited):
    if curr == "":
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if(find(word[0], word, i, j, board, [[i,j]])):
                        return True
        return False

    if curr == word:
        return True
    a, b, c, d = False, False, False, False

    # below
    if m + 1 < len(board) and [m+1,n] not in visited:
        if board[m + 1][n] == word[len(curr)]:
            visited.append([m + 1, n])
            a = find(curr + board[m + 1][n], word, m + 1, n, board, visited)
            visited.pop()
            # top
    if m - 1 >= 0 and [m-1,n] not in visited:
        if board[m - 1][n] == word[len(curr)]:
            visited.append([m - 1, n])
            b = find(curr + board[m - 1][n], word, m - 1, n, board, visited)
            visited.pop()

            # right
    if n + 1 < len(board[0]) and [m,n+1] not in visited:
        if board[m][n + 1] == word[len(curr)]:
            visited.append([m, n + 1])
            c = find(curr + board[m][n + 1], word, m, n + 1, board, visited)
            visited.pop()

            # left
    if n - 1 >= 0 and [m,n-1] not in visited:
        if board[m][n - 1] == word[len(curr)]:
            visited.append([m, n - 1])
            d = find(curr + board[m][n - 1], word, m, n - 1, board, visited)
            visited.pop()
    return a or b or c or d


def exist(board, word: str) -> bool:
    return find("", word, 0, 0, board, [])

#print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
#print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
#print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(exist(board =
[["a","b"],["a","a"]]
, word =
"aaba"))