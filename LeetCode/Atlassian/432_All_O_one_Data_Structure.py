from os import remove


class Node:
    def __init__(self, count):
        self.count = count
        self.strs = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.strings = {}
        self.str_count = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, prev, count, key):
        new_node = Node(count)
        new_node.prev = prev
        new_node.next = prev.next
        prev.next = new_node
        new_node.next.prev = new_node
        new_node.strs.add(key)
        return new_node


    def del_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def inc(self, key: str) -> None:
        old_count = self.strings.get(key)
        new_count = old_count+1 if old_count else 1
        old_node = self.str_count.get(old_count)
        new_node = self.str_count.get(new_count)
        self.strings[key] = new_count

        if new_node:
            new_node.strs.add(key)
        else:
            new_node = self.add_node(old_node or self.head, new_count, key)
            self.str_count[new_count] = new_node

        if old_node:
            old_node.strs.remove(key)
            if not old_node.strs:
                self.del_node(old_node)
                del self.str_count[old_count]

    def dec(self, key: str) -> None:
        old_count = self.strings.get(key)
        new_count = old_count-1
        old_node = self.str_count.get(old_count)

        if new_count>0:
            self.strings[key] = new_count
            new_node =  self.str_count.get(new_count)
            if new_node:
                new_node.strs.add(key)
            else:
                new_node = self.add_node(old_node.prev, new_count, key)
                self.str_count[new_count] = new_node
        else:
            del self.strings[key]

        old_node.strs.remove(key)
        if not old_node.strs:
            self.del_node(old_node)
            del self.str_count[old_count]

    def getMaxKey(self) -> str:
        if self.str_count:
            return next(iter(self.tail.prev.strs))
        return ""

    def getMinKey(self) -> str:
        if self.str_count:
            return next(iter(self.head.next.strs))
        return ""



# from sortedcontainers import SortedDict
#
# class AllOne:
#
#     def __init__(self):
#         self.strings = {}
#         self.str_count = SortedDict()
#
#     def inc(self, key: str) -> None:
#         if key not in self.strings:
#             self.strings[key] = 1
#             if 1 not in self.str_count:
#                 self.str_count[1] = set()
#             self.str_count[1].add(key)
#         else:
#
#             temp_val = self.strings[key]
#             self.strings[key] += 1
#
#             if len(self.str_count[temp_val]) == 1:
#                 del self.str_count[temp_val]
#             else:
#                 self.str_count[temp_val].remove(key)
#
#             if temp_val + 1 not in self.str_count:
#                 self.str_count[temp_val + 1] = set()
#             self.str_count[temp_val + 1].add(key)
#
#
#     def dec(self, key: str) -> None:
#         temp_val = self.strings[key]
#         self.strings[key] -= 1
#         if temp_val  == 1:
#             del self.strings[key]
#
#         if len(self.str_count[temp_val]) == 1:
#             del self.str_count[temp_val]
#         else:
#             self.str_count[temp_val].remove(key)
#         if temp_val-1:
#             if temp_val - 1 not in self.str_count:
#                 self.str_count[temp_val - 1] = set()
#             self.str_count[temp_val - 1].add(key)
#
#     def getMaxKey(self) -> str:
#         if self.str_count:
#             return next(iter(self.str_count.peekitem(-1)[1]))
#         return ""
#
#     def getMinKey(self) -> str:
#         if self.str_count:
#             return next(iter(self.str_count.peekitem(0)[1]))
#         return ""

#a = ["AllOne","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","dec","dec","dec","dec","dec","dec","inc","inc","inc","inc","getMaxKey","getMinKey","inc","inc","getMaxKey","getMinKey","inc","dec","getMaxKey","getMinKey"]
#b = [[],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],[],[],["k"],["l"],[],[],["a"],["j"],[],[]]

# a = ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
# b = [[],["hello"],["hello"],[],[],["leet"],[],[]]

# a = ["AllOne","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","dec","dec","dec","dec","dec","dec","inc","inc","inc","inc","getMaxKey","getMinKey","inc","inc","getMaxKey","getMinKey","inc","dec","getMaxKey","getMinKey"]
# b = [[],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],[],[],["k"],["l"],[],[],["a"],["j"],[],[]]

a= ["AllOne","inc","inc","inc","inc","inc","inc","inc","inc","inc","inc","dec","dec","getMaxKey"]
b = [[],["hello"],["l"],["l"],["l"],["k"],["k"],["k"],["j"],["j"],["j"],["j"],["k"],[]]

obj = AllOne()
#print("null")
for i in range(1, len(a)):
    if a[i] == "inc":
        obj.inc(b[i][0])
        #print("null")
    elif a[i] == "dec":
        obj.dec(b[i][0])
        #print("null")
    elif a[i] == "getMaxKey":
        print(obj.getMaxKey())
    elif a[i] == "getMinKey":
        print(obj.getMinKey())

# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()