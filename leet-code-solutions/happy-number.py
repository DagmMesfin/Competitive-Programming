class Solution:
    def isHappy(self, n: int) -> bool:
        seto = set()
        while(n != 1):
            no = str(n)
            sumo = 0
            for digit in no:
                sumo+= pow(int(digit), 2)
            n = sumo
            if n in seto:
                return False
            seto.add(n)
        return True
            