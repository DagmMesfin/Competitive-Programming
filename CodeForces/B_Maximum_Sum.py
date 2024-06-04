def maxSubArray(nums):
    sumo = nums[0]
    currento = 0
    for num in nums:
        currento = max(currento, 0)
        currento += num
        sumo = max(currento, sumo)
    return sumo

modo = 10**9 + 7
for _ in range(int(input())):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    sumo = sum(arr)
    maxsum = maxSubArray(arr)
    maxsum = maxsum if maxsum >= 0 else 0
    ans = sumo
    ans += maxsum*(pow(2,k,modo) - 1)
    print(ans%(modo))
