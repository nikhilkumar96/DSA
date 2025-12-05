from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = SortedDict({timestamp: value})
        else:
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                i = self.store[key].bisect_left(timestamp)     #[IMP]
                if i:
                    return self.store[key][self.store[key].keys()[i - 1]]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
a = ["TimeMap","set","get","get","set","get","get"]
b = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
obj = TimeMap()

for name, args in zip(a[1:], b[1:]):
    print(getattr(obj, name)(*args))