class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        modstr = []
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                modstr.append(" ")
            modstr.append(s[i])
        return "".join(modstr)

        