from header import *

class Solution:
    def isHappy(self, n: int) -> bool:
        if(n==1 or n==7):
            return True
        elif(n<10):
            return False
        else:
            sum =0
            while(n>0):
                temp = n%10
                sum += temp*temp
                n= n//10
            return self.isHappy(sum)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#
#         visited = set()
#
#         def happy_calc(num):
#             if num in visited:
#                 return False
#             visited.add(num)
#             num_li = list(num)
#             temp = 0
#             for item in num_li:
#                 temp += math.pow(int(item), 2)
#             temp = str(int(temp))
#             if temp == '1':
#                 return True
#             return happy_calc(temp)
#
#         return happy_calc(str(n))

print(Solution().isHappy(19))