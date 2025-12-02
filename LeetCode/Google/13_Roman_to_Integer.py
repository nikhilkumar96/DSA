class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I": 1, "V" :5, "X" :10, "L" :50, "C" :100, "D" :500, "M":1000}

        if not s:
            return 0

        last = s[-1]
        num = rom[last]
        for i in s[:-1][::-1]:
            if rom[last]>rom[i]:
                num-=rom[i]
            else:
                num+=rom[i]
            last = i

        return num

print(Solution().romanToInt("MCMXCIV"))