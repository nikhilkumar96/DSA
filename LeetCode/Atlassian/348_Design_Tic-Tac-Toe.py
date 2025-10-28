
class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = {1:[0 for i in range(n)],
                      2: [0 for i in range(n)]}
        self.column = {1:[0 for i in range(n)],
                      2: [0 for i in range(n)]}
        self.diagonal = {1: 0,
                          2: 0}
        self.anti_diagonal = {1: 0,
                          2: 0}

    def move(self, row: int, col: int, player: int) -> int:

        self.rows[player][row]+=1
        self.column[player][col]+=1

        if row == col:
            self.diagonal[player]+=1
        if row == self.size-col-1:
            self.anti_diagonal[player]+=1

        return self.check_win(player)

    def check_win(self, player):

        row =  any([True for i in self.rows[player] if i==self.size])
        col = any([True for i in self.column[player] if i==self.size])
        dia = self.diagonal[player] == self.size or self.anti_diagonal[player] == self.size
        if row or col or dia:
            return player
        return 0
        # class TicTacToe:
#
#     def __init__(self, n: int):
#         self.size = n
#         self.mat = [[0 for i in range(self.size)] for j in range(self.size)]
#
#     def move(self, row: int, col: int, player: int) -> int:
#         self.mat[row][col] = player
#
#         if self.check_win(player):
#             return player
#         return 0
#
#     def check_win(self, player):
#         return self.check_row(player) or self.check_column(player) or self.check_diagonal(player)
#
#     def check_row(self, player):
#         for i in range(self.size):
#             row = True
#             for j in range(self.size):
#                 if self.mat[i][j] != player:
#                     row = False
#             if row:
#                 return True
#         return False
#
#     def check_column(self, player):
#         for i in range(self.size):
#             column = True
#             for j in range(self.size):
#                 if self.mat[j][i] != player:
#                     column = False
#             if column:
#                 return True
#         return False
#
#     def check_diagonal(self, player):
#         left, right = True, True
#         for i in range(self.size):
#             if self.mat[i][i] != player:
#                 left = False
#                 break
#         for i in range(self.size):
#             if self.mat[i][self.size-i-1]!= player:
#                 right = False
#                 break
#         return left or right


# a = ["TicTacToe","move","move","move"]
# b = [[2],[0,1,1],[1,1,2],[1,0,1]]

a = ["TicTacToe","move","move","move","move","move","move","move"]
b = [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]

obj = TicTacToe(b[0][0])

for i in range(1, len(b)):
    print(obj.move(b[i][0], b[i][1], b[i][2]))