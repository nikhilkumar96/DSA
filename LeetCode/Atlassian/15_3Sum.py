from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p = set()
        n = set()
        z = []

        p_list = []
        n_list = []

        res = set()

        for item in nums:
            if item > 0:
                p.add(item)
                p_list.append(item)
            elif item < 0:
                n.add(item)
                n_list.append(item)
            else:
                z.append(item)

        if z:
            for neg in n:
                if -1 * neg in p:
                    res.add((neg, 0, -1 * neg))
        if len(z) >= 3:
            res.add((0, 0, 0))

        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                if -1 * (p_list[i] + p_list[j]) in n:
                    res.add(tuple(sorted([p_list[i], p_list[j], -1 * (p_list[i] + p_list[j])])))

        for i in range(len(n_list)):
            for j in range(i + 1, len(n_list)):
                if -1 * (n_list[i] + n_list[j]) in p:
                    res.add(tuple(sorted([n_list[i], n_list[j], -1 * (n_list[i] + n_list[j])])))

        fin = []
        for item in res:
            fin.append(list(item))

        return fin


a = [-1,0,1,2,-1,-4]

print(Solution().threeSum(a))