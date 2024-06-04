class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sumo = sum(nums)
        if sumo % p == 0: 
            return 0 

        remainder = defaultdict(int)
        mino = float('inf')
        t = 0 
        count = 1
        remainder[0] == 0

        for num in nums:
            t = (t + num) % p 
            checker = (t-sumo) % p
            if checker in remainder:
                leno = count - remainder[checker]
                mino = min(mino, leno)
            remainder[t] = count
            count += 1
            
        return -1 if mino == float('inf') or mino == len(nums) else mino