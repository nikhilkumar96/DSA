class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = stack.pop()
                while temp[0] != "[":
                    temp= stack.pop()+ temp
                num = stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                numin = int(num)
                stack.append("".join(temp[1:] for i in range(numin)))
        return "".join(stack)


# print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("100[leetcode]"))