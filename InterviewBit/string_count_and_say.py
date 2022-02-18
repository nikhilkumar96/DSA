"""

https://www.interviewbit.com/problems/count-and-say/

Problem Description

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11. 11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2, the sequence is 11.

"""


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        res = ['1']
        if A ==0:
            return None
        for i in range(1, A):
            temp = res[-1]
            temp_res =''
            temp_ele = temp[0]
            temp_count = 1
            for j in range(1, len(temp)):
                if temp[j] == temp_ele:
                    temp_count+=1
                else:
                    temp_res+=str(temp_count)
                    temp_res+=str(temp_ele)
                    temp_ele = temp[j]
                    temp_count=1
            temp_res+=str(temp_count)
            temp_res+=str(temp_ele)
            res.append(temp_res)
        return int(res[-1])

print(Solution().countAndSay(2))


"""
Fastest Solution

seq = ["","1", "11","21"]
class Solution:
    def countAndSay(self, A):
        
        global seq
        if A >= len(seq):
            seq.append(self.genSeq(self.countAndSay(A-1)))

        return seq[A]


    def genSeq(self, seq):
        ct = 0
        prev = ""
        pre = ""

        for i in seq:
            if i == prev:
                ct += 1
            else:
                if ct >0:
                    pre += str(ct) + prev

                prev = i
                ct = 1
        pre += str(ct) + prev
        return pre


"""