class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)-1):
            swaps = False
            for j in range(len(heights)-1 - i):
                if heights[j] < heights[j+1]:
                    swaps = True
                    temp = heights[j+1]
                    heights[j+1] = heights[j]
                    heights[j] = temp
                    tempo = names[j+1]
                    names[j+1] = names[j]
                    names[j] = tempo
            if not swaps:
                break
        return names