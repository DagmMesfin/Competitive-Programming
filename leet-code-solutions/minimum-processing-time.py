class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        timo = 0
        processorTime.sort()
        tasks.sort(reverse = True)
        for i in range(0, len(tasks), 4):
            curPro = processorTime[i//4]
            time = max(curPro+tasks[i], curPro+tasks[i+1], curPro+tasks[i+2], curPro+tasks[i+3])
            timo = max(time, timo)
        return timo