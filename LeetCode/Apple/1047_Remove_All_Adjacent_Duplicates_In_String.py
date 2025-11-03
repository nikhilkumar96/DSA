
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)



# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         i = 0
#         while i < len(s):
#             if stack and stack[-1] == s[i]:
#                 stack.pop(-1)
#                 s = s[:i - 1] + s[i + 1:]
#                 i-=1
#             else:
#                 stack.append(s[i])
#                 i += 1
#         return s


print(Solution().removeDuplicates("abbaca"))