from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = {}
        total_len = len(votes[0])
        for vote in votes:
            rank_value = total_len
            for i, team in enumerate(vote):
                if team not in ranks:
                    ranks[team] = [0] * len(vote)
                ranks[team][i] += 1
        sorted_teams = sorted(votes[0])
        return "".join(sorted(sorted_teams, key=lambda x: ranks[x], reverse=True))

print(Solution().rankTeams(["ABC", "BCA","CAB","CBA","ACB","BAC"]))