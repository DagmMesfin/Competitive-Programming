class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        CrSt = set(nums)
        num = []
        oc = []
        for st in CrSt:
            num.append(st)
            oc.append(nums.count(st))
        for i in range(len(num)-1):
            maxIndex = i
            for j in range(i+1, len(num)):
                if oc[j] > oc[maxIndex]:
                    maxIndex = j
            temp1 = num[i]
            temp2 = oc[i]
            num[i] = num[maxIndex]
            oc[i] = oc[maxIndex]
            num[maxIndex] = temp1
            oc[maxIndex] = temp2
        return num[:k]