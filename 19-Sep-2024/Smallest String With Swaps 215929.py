# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        parent = {i:i for i in range(len(s))}
        size = {i:1 for i in range(len(s))}
        seto = defaultdict(list)
        res = []
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        
        def union(x, y):
            root1 = find(x)
            root2 = find(y)
            
            if root1 != root2:
                if size[root2] > size[root1]:
                    parent[root1] = root2
                    size[root2]+=size[root1]
                else:
                    parent[root2] = root1
                    size[root1]+=size[root2]
        def connected(x,y):
            return find(x) == find(y)
            
        for x,y in pairs:
            union(x,y)
        for i in range(len(s)):
            seto[parent[find(i)]].append(i)
        for i in seto:
            seto[i].sort(key = lambda l: s[l], reverse = True)

        for i in range(len(s)):
            parento = find(i)
            if parento == i and size[parento] ==1:
                res.append(s[i])
            else:
                res.append(s[seto[parento].pop()])

        return "".join(res)