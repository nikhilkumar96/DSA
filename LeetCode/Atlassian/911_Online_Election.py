from collections import Counter
from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = []
        leader, leader_votes = None, 0
        count_votes = Counter()

        for i in range(len(persons)):
            count_votes[persons[i]]+=1
            if count_votes[persons[i]]>leader_votes:
                self.votes.append([times[i], persons[i]])
                leader = persons[i]
            leader_votes = count_votes[leader]

    def q(self, t: int) -> int:
        left =0
        right = len(self.votes)-1
        while left<right:
            mid = (left+right)//2
            if self.votes[mid][0] < t:
                left = mid+1
            else:
                right = mid
        return self.votes[left][1]



# class TopVotedCandidate:
#
#     def __init__(self, persons: List[int], times: List[int]):
#         self.times = times
#         self.votes = [None for i in range(len(persons))]
#         for i in range(len(persons)):
#             if i == 0:
#                 self.votes[0] = [persons[i]]
#             else:
#                 self.votes[i] = [persons[i]] + self.votes[i - 1]
#
#     def q(self, t: int) -> int:
#
#         i = 0
#         while i < len(self.times) and self.times[i] <= t:
#             i += 1
#         count_no = Counter(self.votes[i - 1])
#
#         max_key = None
#         max_value = 0
#
#         for k, v in count_no.items():
#             if v > max_value:
#                 max_value = v
#                 max_key = k
#         return max_key

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

a = [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]

obj = TopVotedCandidate(a[0][0], a[0][1])

for i in range(1, len(a)):
    print(obj.q(a[i][0]))