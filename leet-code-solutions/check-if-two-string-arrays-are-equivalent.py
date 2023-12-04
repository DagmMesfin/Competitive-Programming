class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        stro1 = ""
        stro2 = ""
        for i in range(len(word1)):
            for j in range(len(word1[i])):
                stro1+=word1[i][j]
        for i in range(len(word2)):
            for j in range(len(word2[i])):
                stro2+=word2[i][j]
        return stro1 == stro2