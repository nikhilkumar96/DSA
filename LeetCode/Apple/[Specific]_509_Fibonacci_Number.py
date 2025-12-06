class Solution:
    def fib(self, n: int) -> int:
        val = {
            0: 0,
            1: 1
        }

        def recur(i):
            if i in val:
                return val[i]

            val[i] = recur(i - 1) + recur(i - 2)
            return val[i]

        return recur(n)

print(Solution().fib(10))