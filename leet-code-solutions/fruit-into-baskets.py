class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        seto = set()
        maxim = 0

        l = 0

        for r in range(len(fruits)):
            seto.add(fruits[r])
            counter[fruits[r]]+=1

            if len(seto) == 3:
                while l<r:
                    counter[fruits[l]]-=1
                    if counter[fruits[l]] == 0:
                        seto.remove(fruits[l])
                        l+=1
                        break
                    l+=1
            maxim = max(maxim,r-l+1)

        return maxim
            
        