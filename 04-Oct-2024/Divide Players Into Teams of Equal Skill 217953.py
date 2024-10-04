# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        prev = skills[0] + skills[-1]
        sum = (skills[0]*skills[-1])

        for i in range(1, len(skills)//2):
            if skills[i] + skills[-1-i] != prev:
                return -1
            sum+= (skills[i]*skills[-1-i])
            
        return sum        