class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        dicto = {i:"" for i in range(1,len(s)+1)}

        for word in s:
            ordero = int(word[-1]) 
            word = word[:-1]
            dicto[ordero] = word
        
        return " ".join(dicto.values())