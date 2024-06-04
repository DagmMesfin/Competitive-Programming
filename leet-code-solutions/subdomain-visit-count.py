class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = defaultdict(int)
        lastresult = []
        for i in range(len(cpdomains)):
            inputo = cpdomains[i].split()
            inputo[0] = int(inputo[0])
            inputo[1] = inputo[1].split('.')
            print(inputo)

            for i in range(len(inputo[1])-1, -1, -1):
                result[inputo[1][i]] += inputo[0]
                if i != 0:
                    inputo[1][i-1]+='.'+inputo[1][i]
        for key,val in result.items():
            lastresult.append(str(val)+" "+key)
        return lastresult