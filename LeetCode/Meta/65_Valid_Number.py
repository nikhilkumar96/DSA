class Solution:
    def isNumber(self, s: str) -> bool:
        poss = ["inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity", "nan", "-nan", "+nan"]
        if s in poss:
            return False
        try:
            float(s)
        except:
            return False
        return True


print(Solution().isNumber("123"))