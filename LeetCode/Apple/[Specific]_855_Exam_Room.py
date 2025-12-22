from header import *


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seating = SortedList()

    def seat(self) -> int:
        if not self.seating:
            self.seating.add(0)
            return 0

        # assuimg the dist b/w 0 and first seat is highest
        pos, dist = 0, self.seating[0]

        for start, end in zip(self.seating,
                              self.seating[1:]):  # making interval like for [2,10,17] -> [2,10] , [10,17]   [Specific]
            mid = (end - start) // 2
            if mid > dist:
                dist = mid
                pos = start + mid

        # checking b/w last element and last seat is highest

        if self.n - 1 - self.seating[-1] > dist:
            pos = self.n - 1

        self.seating.add(pos)
        return pos

    def leave(self, p: int) -> None:
        self.seating.remove(p)

a =["ExamRoom","seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave","leave","seat","seat","leave","seat","leave","seat","leave","seat","leave","seat","leave","leave","seat","seat","leave","leave","seat","seat","leave"]
b = [[10],[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0],[4],[],[],[7],[],[3],[],[3],[],[9],[],[0],[8],[],[],[0],[8],[],[],[2]]
obj = ExamRoom(b[0][0])

for name, args in zip(a[1:], b[1:]):
    print(getattr(obj, name)(*args))