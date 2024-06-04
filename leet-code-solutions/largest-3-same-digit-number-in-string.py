class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        numo = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        indexo = -1
        for i in range(len(numo)):
            if numo[i] in num:
                indexo = max(indexo, i)
        return numo[indexo] if indexo != -1 else ""





        