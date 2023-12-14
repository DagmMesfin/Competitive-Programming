class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freqoc = defaultdict(list)
        

    def add(self, number: int) -> None:
        if self.freq[number]:
            self.freqoc[self.freq[number]].remove(number)
            self.freq[number]+=1
            self.freqoc[self.freq[number]].append(number)
        else:
            self.freq[number]+=1
            self.freqoc[self.freq[number]].append(number)


    def deleteOne(self, number: int) -> None:
        if self.freq[number] != 0:
            self.freqoc[self.freq[number]].remove(number)
            self.freq[number]-=1
            self.freqoc[self.freq[number]].append(number)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqoc[frequency]



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)