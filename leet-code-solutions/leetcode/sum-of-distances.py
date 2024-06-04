class Solution(object):
    def distance(self, nums):
        n = len(nums)
        arr = [0]*n
        indexo_pre_sum = defaultdict(list)
        numcounter = defaultdict(int)
        counto = Counter(nums)
        for i in range(n):
            indexo_pre_sum[nums[i]].append(i)
        for num,indexlist in indexo_pre_sum.items():
            presum = []
            sumo = 0
            for idx in indexlist:
                sumo+=idx
                presum.append(sumo)
            indexo_pre_sum[num] = presum

        for i in range(n):
            allsum = indexo_pre_sum[nums[i]][-1]
            curr_oc_idx = numcounter[nums[i]]
            all_count = counto[nums[i]]
            if all_count == 1:
                arr[i] = 0
            else:
                if curr_oc_idx == 0:
                    arr[i] = allsum - (indexo_pre_sum[nums[i]][curr_oc_idx] * all_count)
                else:
                    fwd = (allsum - indexo_pre_sum[nums[i]][curr_oc_idx]) - ((indexo_pre_sum[nums[i]][curr_oc_idx] - indexo_pre_sum[nums[i]][curr_oc_idx - 1]) * (all_count - 1 - curr_oc_idx))
                    bck = ((indexo_pre_sum[nums[i]][curr_oc_idx] - indexo_pre_sum[nums[i]][curr_oc_idx - 1]) * (curr_oc_idx + 1)) - (indexo_pre_sum[nums[i]][curr_oc_idx])
                    arr[i] = fwd + bck

            numcounter[nums[i]] += 1

        return arr
        