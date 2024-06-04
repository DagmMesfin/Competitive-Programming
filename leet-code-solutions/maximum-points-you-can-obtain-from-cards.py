class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_pts = sum(cardPoints)
        window_sub = sum(cardPoints[:n-k])
        score = total_pts - window_sub
        
        for i in range(1,k+1):
            window_sub+=cardPoints[i+(n-k)-1] - cardPoints[i-1]
            score = max(score, total_pts - window_sub)

        return score

