class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        unique = set()
        min_score = float('inf')

        for r in range(len(cards)):
            if cards[r] in unique:
                while cards[r] in unique and l!=r:
                    unique.remove(cards[l])
                    l+=1
                min_score = min(min_score,r-l+2)
            unique.add(cards[r])
            
        return min_score if min_score != float('inf') else -1