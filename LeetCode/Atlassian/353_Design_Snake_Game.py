from typing import List
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.maxwidth = width
        self.maxheight = height
        self.food = food
        self.score = 0
        self.snake = [[0 ,0]]


    def move(self, direction: str) -> int:
        proposed_move = []
        if direction == 'L':
            proposed_move = [self.snake[-1][0], self.snake[-1][1]-1]
        elif direction== 'R':
            proposed_move = [self.snake[-1][0], self.snake[-1][1] + 1]
        elif direction == 'U':
            proposed_move = [self.snake[-1][0]-1, self.snake[-1][1]]
        elif direction == 'D':
            proposed_move = [self.snake[-1][0] +1, self.snake[-1][1]]

        if proposed_move[0]< 0 or proposed_move[0]>=self.maxheight or proposed_move[1]<0 or proposed_move[1]>=self.maxwidth or proposed_move in self.snake[1:]:
            return -1
        elif self.food and proposed_move == self.food[0]:
            self.score+=1
            self.food.pop(0)
        else:
            self.snake.pop(0)
        self.snake.append(proposed_move)
        return  self.score


#
# a = ["SnakeGame","move","move","move","move","move","move"]
# b = [[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]

# a = ["SnakeGame","move","move"]
# b = [[2,2,[[0,1]]],["R"],["D"]]

b = [[3,3,[[2,0],[0,0],[0,2],[2,2]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["D"]]

obj = SnakeGame(b[0][0], b[0][1], b[0][2])

for i in range(1, len(b)):
    print(obj.move(b[i][0]))
