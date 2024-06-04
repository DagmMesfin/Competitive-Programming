class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev = skill[0] + skill[-1]
        sum = (skill[0]*skill[-1])

        for i in range(1, len(skill)//2):
            if skill[i] + skill[-1-i] != prev:
                return -1
            sum+= (skill[i]*skill[-1-i])
            
        return sum        
