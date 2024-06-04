class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        if num >= 0:
            numo = list(str(num)) #Convert the number to list of characters
            numo.sort() #sort the characters in acsending order
            zero = []
            if numo[0] == "0":
                for i in range(1,len(numo)):
                    if numo[i] != "0":
                        numo[i],numo[0] = numo[0],numo[i]
                        break # flips the "0" with the adjacent number (013 -> 103)
            
            numo = "".join(numo) 
        else:
            numo = list(str(num))
            numo = sorted(numo[1:], reverse = True) #sorts the number in descending order (excluding '-')
            numo = "-"+"".join(numo) 
        numo = int(numo)
        return numo