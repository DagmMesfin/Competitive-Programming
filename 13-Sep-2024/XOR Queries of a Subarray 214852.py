# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefsum  = [0]
        ans  = []
        sumo = 0

        for val in arr:
            sumo ^= val
            prefsum.append(sumo)

        for query in queries:
            ans.append(prefsum[query[0]] ^ prefsum[query[1] + 1])

        return ans