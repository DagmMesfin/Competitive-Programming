class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {arr2[i]:0 for i in range(len(arr2))}
        rest = []
        res = []

        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                rest.append(arr1[i])
            else:
                counter[arr1[i]] += 1

        for num,count in counter.items():
            res.extend([num for i in range(count)])

        rest.sort()
        res.extend(rest)

        return res
