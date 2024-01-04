class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        sumo = 0
        k_x = set()
        for val,count in counter.items():
            if val!=k/2:
                if k-val not in k_x : 
                    sumo+=min(count,counter[k-val])
            else: 
                sumo+=math.floor(count/2)
            k_x.add(val)
        return sumo