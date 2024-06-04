class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2): return False

        s1count, s2count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1count[ord(s1[i])-ord("a")] += 1
            s2count[ord(s2[i])-ord("a")] += 1

        matches = 0

        for j in range(26):
            if s1count[j] == s2count[j]: matches+=1

        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2count[index] += 1

            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches-=1
            
            index = ord(s2[l]) - ord("a")
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches-=1

            l+=1
            
        return matches == 26
            

        
        