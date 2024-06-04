class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        output = 0
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            maxfreq = max(maxfreq, counter[s[r]])

            while (r-l+1) - maxfreq > k:
                counter[s[l]] -=1
                l+=1

            output = max(output, r-l+1)
        return output