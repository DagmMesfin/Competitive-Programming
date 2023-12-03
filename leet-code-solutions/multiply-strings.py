class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numo1 = 0
        numo2 = 0
        for i in range(len(num1)):
            numo1 += (ord(num1[-1-i]) - ord("0")) * int(pow(10,i))
        for i in range(len(num2)):
            numo2 += (ord(num2[-1-i]) - ord("0")) * int(pow(10,i))
        prod = numo1 * numo2
        if prod == 0:
            return "0"
        prodo = ""
        while prod != 0:
            prodo += chr(prod%10 + ord("0"))
            prod = prod//10
        return prodo[::-1]
