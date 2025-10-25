import math
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache)>self.capacity:
            self.cache.popitem(False)




# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.next = None
#         self.prev = None
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.head = Node(0)
#         self.tail = Node(math.inf)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.cache = {}
#
#     def add_node_in_end(self, value):
#         new_node = Node(value)
#         new_node.prev = self.tail.prev
#         self.tail.prev.next = new_node
#         new_node.next = self.tail
#         self.tail.prev = new_node
#         return new_node
#
#     def delete_node(self, del_node):
#         value = del_node.val
#         del_node.prev.next = del_node.next
#         del_node.next.prev = del_node.prev
#         del del_node
#         return value
#
#     def get(self, key: int) -> int:
#         node = self.cache.get(key)
#         if node:
#             self.delete_node(node)
#             new_node = self.add_node_in_end(node.val)
#             self.cache[key] = new_node
#             return node.val[1]
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         existing_node = self.cache.get(key)
#         if existing_node:
#             self.delete_node(existing_node)
#         elif len(self.cache) == self.capacity:
#             del self.cache[self.delete_node(self.head.next)[0]]
#
#         self.cache[key] = self.add_node_in_end([key, value])



# a = ["LRUCache","put","put","get","put","get","put","get","get","get"]
# b = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# a = ["LRUCache","get","put","get","put","put","get","get"]
# b = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

def print_func(obj):
    print("keys =", obj.cache.keys())
    res = []
    curr = obj.head.next
    while curr != obj.tail:
        res.append(curr.val)
        curr = curr.next
    print("nodes", res)


a = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
b = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

obj = LRUCache(b[0][0])
for i in range(1, len(a)):
    if a[i] == "put":
        obj.put(b[i][0], b[i][1])
    elif a[i] == "get":
        print(obj.get(b[i][0]))