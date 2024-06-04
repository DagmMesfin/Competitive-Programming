class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        dictoloss = collections.Counter()
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



        