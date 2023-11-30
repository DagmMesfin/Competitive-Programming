class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        l = 0
        while l < len(command):
            if command[l] == "G":
                res+="G"
                l+=1
            elif command[l] == "(" and command[l+1] == "a":
                res+="al"
                l+=4
            elif command[l] == "(" and command[l+1] == ")":
                res+="o"
                l+=2
        return res