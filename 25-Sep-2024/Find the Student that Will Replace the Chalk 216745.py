# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalks_reqd=0
        for piece in chalk:
            chalks_reqd+=piece

        if k%chalks_reqd==0:
            return 0

        elif k%chalks_reqd!=0:
            rem=k%chalks_reqd

            for i in range(len(chalk)):
                if chalk[i]>rem:
                    return i
                rem-=chalk[i]