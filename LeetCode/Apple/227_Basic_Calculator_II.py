
class Solution:
    def calculate(self, s: str) -> int:
        a = []
        last_ele = None
        curr_ele = ''
        last_op = '+'
        for i in s+"+":
            if i == " ":
                continue
            elif i.isdigit():
                curr_ele+=i
            else:
                if last_op == "+":
                    last_ele = int(curr_ele)
                    a.append(last_ele)
                elif last_op=="-":
                    last_ele = -int(curr_ele)
                    a.append(last_ele)
                elif last_op=="*":
                    a.pop()
                    last_ele*=int(curr_ele)
                    a.append(last_ele)
                elif last_op == "/":
                    a.pop()
                    last_ele = int(last_ele/int(curr_ele))
                    a.append(last_ele)
                curr_ele = ''
                last_op = i

        return sum(a)




#print(Solution().calculate("32+10*2"))
#print(Solution().calculate("0-2147483647"))
print(Solution().calculate("2*3+4"))