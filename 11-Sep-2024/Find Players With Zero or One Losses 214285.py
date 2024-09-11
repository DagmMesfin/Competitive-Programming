# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictoloss = Counter()
        theplayer = set()
        for i in range(len(matches)):
            dictoloss[matches[i][1]] += 1
            theplayer.add(matches[i][1])
            theplayer.add(matches[i][0])
        result = [[],[]]
        for player in theplayer:
            if dictoloss[player] == 0:
                result[0].append(player)
            elif dictoloss[player] == 1:
                result[1].append(player)
        result[0].sort()
        result[1].sort()
        return result