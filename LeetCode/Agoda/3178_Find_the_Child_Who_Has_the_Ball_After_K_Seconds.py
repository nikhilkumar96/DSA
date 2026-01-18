class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return n-1-(k%(n-1)) if (k//(n-1))%2!=0 else (k%(n-1))

print(Solution().numberOfChild(5,6))