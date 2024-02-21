class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        sumo = 0
        i=0
        for k,count in counter.items():
            if count%2 == 0:
                sumo+=count
            else:
                if i == 0:
                    sumo+=count
                else:
                    sumo+=count-1
                i+=1
        return sumo