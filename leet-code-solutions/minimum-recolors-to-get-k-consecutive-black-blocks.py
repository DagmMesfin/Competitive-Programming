class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dicto = defaultdict(int)

        for i in range(k):
            dicto[blocks[i]] += 1

        min_recolor = dicto["W"]

        for i in range(1, len(blocks)-k+1):
            dicto[blocks[i-1]] -= 1
            dicto[blocks[i+k-1]] += 1
            min_recolor = min(dicto["W"], min_recolor)
        
        return min_recolor






