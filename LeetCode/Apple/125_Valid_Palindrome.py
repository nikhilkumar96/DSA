class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = "".join([i for i in s if i.isalnum()]).lower()
        return True if front == front[::-1] else False

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))