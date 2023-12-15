class ATM(object):

    def __init__(self):
        self.bank_notes = {
            20:0,
            50:0,
            100:0,
            200:0,
            500:0
        }
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(len(banknotesCount)):
            self.bank_notes[self.notes[i]] += banknotesCount[i]
        
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        listo = [0]*5
        original_amt = amount+0
        started_amount = 0
        numo = 0
        for i in range(len(self.notes)-1, -1, -1):
            thecount = amount//self.notes[i]
            if thecount:
                thecount = min(thecount,self.bank_notes[self.notes[i]])
                listo[i] = thecount
                started_amount += (thecount*self.notes[i])
                numo = max(numo,thecount)
                amount -= thecount*self.notes[i]

        if numo and original_amt == started_amount:
            for i in range(len(self.notes)):
                self.bank_notes[self.notes[i]] -= listo[i]
            return listo
        else:
            return [-1]

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)