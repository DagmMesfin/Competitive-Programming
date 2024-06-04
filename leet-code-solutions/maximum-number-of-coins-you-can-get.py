class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        sum = 0
        for i in range(1, (len(piles) * 2)//3, 2):
            sum+=piles[i]
        return sum