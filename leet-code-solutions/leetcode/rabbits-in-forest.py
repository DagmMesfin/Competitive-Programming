class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        counter = Counter(answers)
        for k,count in counter.items():
            ans+= (count - count%(k+1))
            if count%(k+1) > 0:
                ans+=k+1
        return ans