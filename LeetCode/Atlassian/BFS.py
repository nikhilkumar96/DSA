from collections import deque

def min_dice_throws(N, teleport):
    visited = [False] * N
    q = deque([(0, 0)])  # (cell, throws)
    visited[0] = True

    while q:
        cell, throws = q.popleft()
        if cell == N - 1:
            return throws

        for roll in range(1, 7):
            next_cell = cell + roll
            if next_cell >= N:
                continue

            # Apply teleporter if exists
            if next_cell in teleport:
                next_cell = teleport[next_cell]

            if not visited[next_cell]:
                visited[next_cell] = True
                q.append((next_cell, throws + 1))

    return -1


print(min_dice_throws(10, {2:8}))


#You are given a 1D game board with N cells numbered 0 to N-1. You start at cell 0. On each move you roll a 6-sided die and move forward by 1..6 cells. Some cells contain teleporters that instantly transport you to another cell (forward or backward). Teleporters are applied immediately when you land on that cell (you do not roll again for the teleporter).

#Write a function min_dice_throws(N, teleport: Dict[int,int]) -> int that returns the minimum number of dice throws to reach cell N-1. If it’s not reachable, return -1.