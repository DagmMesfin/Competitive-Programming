class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t  = 0
        n = len(tickets)
        while tickets[k]:
            for i in range(n):
                if tickets[i]:
                    tickets[i]-=1
                    t+=1
                if tickets[k] == 0:
                    break
        return t
        
