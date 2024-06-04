class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dicto = defaultdict(int)
        maxo =0
        l = 0

        for i in range(len(answerKey)):
            dicto[answerKey[i]] += 1

            while (dicto["T"]>k and dicto["F"] > k) and l<i:
                dicto[answerKey[l]]-=1
                l+=1
            
            maxo = max(maxo, i-l+1)

        return maxo
            
            

            