from header import *

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


# class RandomizedSet:
#
#     def __init__(self):
#         self.s = set()
#         self.l = []
#
#     def insert(self, val: int) -> bool:
#         if val in self.s:
#             return False
#         self.s.add(val)
#         self.l.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         if val not in self.s:
#             return False
#         self.s.remove(val)
#         self.l.remove(val)
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self.l)
#
#
# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()

obj = RandomizedSet()
a =["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
b = [[],[1],[2],[2],[],[1],[2],[]]
func_call_with_two_lists(a, b , obj)