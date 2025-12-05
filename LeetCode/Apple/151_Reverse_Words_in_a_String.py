class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [i for i in s.split(" ") if i != ''][::-1]
        return " ".join(arr)

print(Solution().reverseWords("  hello world  "))