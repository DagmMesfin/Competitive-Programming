class Solution:
    def printVertically(self, s: str) -> List[str]:
        listo = s.split()
        maxo = 0
        for i in range(len(listo)):
             maxo = max(maxo, len(listo[i]))
        outputo = [""] * maxo
        for i in range(len(listo)):
            for j in range(maxo):
                if j < len(listo[i]): 
                    outputo[j] += listo[i][j]
                elif j >= len(listo[i]):
                    outputo[j] += " "
        for i in range(maxo):
            outputo[i] = outputo[i].rstrip()

        return outputo
