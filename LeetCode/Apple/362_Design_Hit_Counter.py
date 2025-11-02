import heapq

class HitCounter:

    def __init__(self):
        self.minheap = []

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.minheap, timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.minheap and timestamp - self.minheap[0] >= 300:
            heapq.heappop(self.minheap)
        return len(self.minheap)


a = ["HitCounter","hit","hit","hit","getHits","getHits","getHits","getHits","getHits","hit","getHits"]
b = [[],[2],[3],[4],[300],[301],[302],[303],[304],[501],[600]]

obj = HitCounter()

for name, args in zip(a[1:], b[1:]):
    print(getattr(obj, name)(*args))