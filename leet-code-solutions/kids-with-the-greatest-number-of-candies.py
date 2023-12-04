class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxo = max(candies)
        boolo = []
        for i in range(len(candies)):
            boolo.append(candies[i]+extraCandies>=maxo)
        return boolo