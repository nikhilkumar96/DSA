import heapq
class StockPrice:

    def __init__(self):
        self.values = {}
        self.min_val = []
        self.max_val = []
        self.current_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.values[timestamp] = price
        self.current_time = max(timestamp, self.current_time)
        heapq.heappush(self.min_val, (price, timestamp))
        heapq.heappush(self.max_val, (-price, timestamp))

    def current(self) -> int:
        return self.values[self.current_time]

    def maximum(self) -> int:
        while self.max_val:
            temp_val, temp_time = self.max_val[0]
            if self.values[temp_time] == -temp_val:
                return -temp_val
            else:
                heapq.heappop(self.max_val)
        return 0

    def minimum(self) -> int:
        while self.min_val:
            temp_val, temp_time = self.min_val[0]
            if self.values[temp_time] == temp_val:
                return temp_val
            else:
                heapq.heappop(self.min_val)
        return 0

# Your StockPrice object will be instantiated and called as such:

#["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]
#[[],[1,10],[2,5],[],[],[1,3],[],[4,2],[]]
obj = StockPrice()
obj.update(1,10)
obj.update(2,5)
param_2 = obj.current()
param_3 = obj.maximum()
obj.update(1,3)
param_4 = obj.maximum()
obj.update(4,2)
param_5 = obj.minimum()

print(param_2,param_3,param_4, param_5)