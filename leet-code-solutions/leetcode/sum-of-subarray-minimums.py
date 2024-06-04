class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev_small = [-1]*n
        next_small = [-1]*n
        monstk = []
        sumo = 0

        for i in range(n):
            while monstk and arr[monstk[-1]] >= arr[i]:
                next_small[monstk.pop()] = i
            if monstk:
                prev_small[i] = monstk[-1]
            monstk.append(i)

        for i in range(n):
            lefto = 0
            righto = 0
            lefto = i+1 if prev_small[i] == -1 else i-prev_small[i]
            righto = n-i if next_small[i] == -1 else next_small[i]-i

            sumo += arr[i]*lefto*righto
            sumo%=1000000007


        return sumo