class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        stro = ''
        i = 0
        j = 0
        k = 0
        while i != len(word1) and j != len(word2) :
            if k == 0:
                stro+=word1[i]
                i+=1
                k = 1
            elif k == 1:
                stro+=word2[j]
                j+=1
                k=0
        while(i!=len(word1)):
            stro+=word1[i]
            i+=1
        while j!=len(word2):
            stro+=word2[j]
            j+=1
        return stro