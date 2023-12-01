class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        excepto = {
            'I' : ['V', 'X'],
            'X' : ['L', 'C'],
            'C' : ['D', 'M']
        }

        prev = s[-1]
        sum = roman_int[prev]
        
        for i in range(len(s)-2, -1, -1):
            if prev in excepto.get(s[i], []):
                sum -= roman_int[s[i]]
            else:
                sum += roman_int[s[i]]
            prev = s[i]
        return sum

        