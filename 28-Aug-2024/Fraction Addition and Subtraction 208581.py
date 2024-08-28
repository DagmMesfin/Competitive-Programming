# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def split(self, exp):
        L = [[exp[0]]]
        for i in range(1, len(exp)):
            if exp[i] in "+-":
                L.append([])
            L[-1].append(exp[i])
        return ["".join(x) for x in L]  
    def to_pairs(self, L):
        K = []
        for frac in L:
            n, d = frac.split("/")
            K.append((int(n), int(d)))
        return K
    def evaluate(self, K):
        l = lcm(*[x[1] for x in K])
        num = sum(x[0]*l//x[1] for x in K)
        g = gcd(num, l)
        return str(num//g)+"/"+str(l//g)
    def fractionAddition(self, expression: str) -> str:
        L = self.split(expression)
        K = self.to_pairs(L)
        return self.evaluate(K)  