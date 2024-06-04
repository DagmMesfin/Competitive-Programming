class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        flag = { i: True for i in fronts}
        front_back = list(zip(fronts,backs))

        min_good = float('inf')
        goodo = float('inf')
        for i in backs:
            if i not in set(fronts):
                goodo = i
            min_good = min(goodo , min_good)
        
        for f,b in front_back:
            if f == b:
                flag[f] = False
        for f,b in front_back:
            if f!=b and flag[f]:
                min_good = min(f , min_good)
            
        
        return min_good if min_good != float('inf') else 0