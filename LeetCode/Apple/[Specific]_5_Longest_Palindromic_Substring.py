class Solution:
    def longestPalindrome(self, s: str) -> str:

        # convert each string to odd value     [Specific] -> Study Manachar's Algorithm
        stri = '#'
        for i in s:
            stri += i
            stri += '#'
        s = stri

        palindrome_center = [0] * len(s)

        def find_boundary(i):
            temp = 1
            c = 0
            while i - temp >= 0 and i + temp < len(s):
                if s[i - temp] == s[i + temp]:
                    c += 1
                    temp += 1
                else:
                    break
            palindrome_center[i] = c

        for i in range(len(s)):
            find_boundary(i)

        max_val = max(palindrome_center)
        index = palindrome_center.index(max_val)

        return "".join(s[index - max_val:index + max_val + 1]).replace('#', '')

print(Solution().longestPalindrome("cbbd"))