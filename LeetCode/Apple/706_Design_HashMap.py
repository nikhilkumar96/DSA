class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        flag = True
        for i, kv in enumerate(self.hashmap):
            if kv[0] == key:
                self.hashmap[i] = [key, value]
                flag = False
        if flag:
            self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for k,v in self.hashmap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.hashmap):
            if kv[0] == key:
                self.hashmap.pop(i)


a=["MyHashMap","put","put","get","get","put","get","remove","get"]
b=[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]

obj = MyHashMap()

for name, args in zip(a[1:], b[1:]):
    print(getattr(obj, name)(*args))