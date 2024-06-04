class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        listo = [
            ['a', 'b', 'c'], 
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
            ]
        res = []
        build = []
        poscomindex = []
        for digit in digits:
            if int(digit) >= 2 and int(digit) <= 9:
                poscomindex.append(int(digit) - 2)
        def buildcom(st):
            if st == len(poscomindex):
                res.append("".join(build))
            else:
                for letter in listo[poscomindex[st]]:
                    build.append(letter)
                    buildcom(st+1)
                    build.pop()
        if len(poscomindex) == 0:
            return []
        else:
            buildcom(0)
            return res